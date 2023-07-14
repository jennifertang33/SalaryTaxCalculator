import pandas as pd
import streamlit as st

def tax_payable_function(status, net_chargeable_income):    
    standard_tax = net_chargeable_income*0.15
    
    if net_chargeable_income <= 50000:
        tax = net_chargeable_income*0.02
    elif net_chargeable_income <= 100000:
        tax = 1000 + (net_chargeable_income-50000)*0.06
    elif net_chargeable_income <= 150000:
        tax = 4000 + (net_chargeable_income-100000)*0.1
    elif net_chargeable_income <= 200000:
        tax = 9000 + (net_chargeable_income-150000)*0.14
    else:
        tax = 16000 + (net_chargeable_income-200000)*0.17
        
    if status == 1: # -> "Single / Separated / Divorced / Widowed"        
        if tax < standard_tax:
            return tax
        else:
            return standard_tax
    else:
        return tax 

status = st.sidebar.selectbox("Marital Status", ["Single / Separated / Divorced / Widowed", "Married"])

if status == "Single / Separated / Divorced / Widowed":
    st.header("Salary Tax Calculator for 2023/24")
    st.caption("For Single / Separated / Divorced / Widowed, tax payable is calculated by the lowest of progressive tax and standard tax.")

    st.divider()
    st.subheader("Part 1 - Income")
    st.markdown("1. Income")
    i1 = st.number_input("Please input value:", min_value=0.0)
    st.markdown("2. Value of all places of residence provided by employer or associated corporation")
    i2 = st.number_input("Note: The value of all places of residence provided cannot exceed 10% of your income. Please input value:", min_value=0.0, max_value=i1*0.1)

    st.divider()
    st.subheader("Part 2 - Deductions")
    st.markdown("1. Self Education Expenses")
    d1 = st.number_input("Please input value from HKD 0 - HKD 100,000:", min_value=0.0, max_value=100000.0)
    st.markdown("2. Approved Charitable Donations")
    d2 = st.number_input("Note: The deductible Approved Charitable Donations cannot exceed 35% of your income. Please input value:", min_value=0.0, max_value=(i1+i2)*0.35)
    st.markdown("3. Mandatory Contributions to Recognized Retirement Schemes")
    d3 = st.number_input("Please input value from HKD 0 - HKD 18,000:", min_value=0.0, max_value=18000.0)
    st.markdown("4. Tax Deductible MPF Voluntary Contributions")
    d4 = st.number_input("Please input value from HKD 0 - HKD 60,000:", min_value=0.0, max_value=60000.0)
    st.markdown("5. Qualifying Annuity Premiums")
    d5 = st.number_input("Note: Total deductible MPF Voluntary Contributions and Annuity Premiums cannot exceed HKD 60,000. Please input value:", min_value=0.0, max_value=60000.0-d4)
    st.markdown("6. Domestic Rental Expenses")
    d6 = st.number_input("Note: If you are married for the full year, the total Domestic Rental Expenses claimed by you and your spouse cannot exceed $100,000. Please input value from HKD 0 - HKD 100,000:", min_value=0.0, max_value=100000.0)
    st.markdown("7. Home Loan Interest")
    d7 = st.number_input("Please input value from HKD 0 - HKD 100,000:", min_value=0.0, max_value=100000.0, key="d7")
    st.markdown("8. Qualifying Health Insurance Premiums")
    d8 = st.number_input("Note: Maximum for self is HKD 8,000. Amount paid for self:", min_value=0.0, max_value=8000.0)
    d9 = st.selectbox("No. of specified relative(s):", list(range(5)))
    d10 = st.number_input("Note: Maximum for each relative is HKD 8,000. Amount paid for specified relative(s):", min_value=0.0, max_value=d9*8000.0)
    st.markdown("9. Elderly Residential Care Expenses")
    d11 = st.selectbox("No. of dependant(s) resided in residential care home:", list(range(5)))
    d12 = st.selectbox("No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(d11+1)))
    d13 = st.number_input("Note: Maximum is HKD 100,000. Amount paid to residential care home:", min_value=0.0, max_value=100000.0)
    st.markdown("Allowances")
    d14 = st.selectbox("Eligible to claim Personal Disability Allowance", ['No', 'Yes'])

    st.divider()
    st.subheader("Part 3 - Allowances")
    st.markdown("Other Allowances Claimed")
    st.markdown("1. No. of dependent children Born in the year")
    a1 = st.selectbox("Please select input:", list(range(10)))
    a2 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a1+1)))
    st.markdown("2. No. of dependent children NOT Born in the year")
    a3 = st.selectbox("Please select input:", list(range(10)), key="a3")
    a4 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a3+1)), key="a4")
    st.markdown("3. Single Parent Allowance")
    a5 = st.selectbox("Please select input:", ['No', 'Yes'])
    st.markdown("4. No. of dependent brothers / sisters")
    a6 = st.selectbox("Please select input:", list(range(10)), key="a6")
    a7 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a6+1)), key="a7")
    st.markdown("5. Dependent parents/grandparents aged 60 or over, or aged under 60 but eligible to claim Government's Disability Allowance")
    a8 = st.selectbox("Case 1 - No. of dependent parents/grandparents Resided with you", list(range(5)), key="a8")
    a9 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a8+1)), key="a9")
    a10 = st.selectbox("Case 2 - No. of dependent parents/grandparents NOT Resided with you", list(range(5)), key="a10")
    a11 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a10+1)), key="a11")
    st.markdown("6. Dependent parents/grandparents aged 55 or over but under 60")
    a12 = st.selectbox("Case 1 - No. of dependent parents/grandparents Resided with you", list(range(5)), key="a12")
    a13 = st.selectbox("Case 2 - No. of dependent parents/grandparents NOT Resided with you", list(range(a12+1)), key="a13")

    #################### calculation
    total_income = i1+i2
    deductions = d1+d2+d3+d4+d5+d6+d7+d8+d10+d13
    basic = 132000
    no_of_disabled_dependants = d12+a2+a4+a7+a9+a11
    other_allowances = a1*260000 + a3*130000 + a6*37500 + a8*100000 + a10*50000 + a12*50000 + a13*25000

    personal_disability_allowance = 0
    if d14 == 'Yes': personal_disability_allowance += 75000

    disabled_dependants_allowances = 75000*no_of_disabled_dependants
    
    single_parent_allowance = 0
    if a5 == 'Yes': single_parent_allowance += 132000
    
    total_allowances = basic + other_allowances + disabled_dependants_allowances + personal_disability_allowance + single_parent_allowance
    net_chargeable_income = total_income - deductions - total_allowances

    if net_chargeable_income < 0: net_chargeable_income = 0

    tax = tax_payable_function(1, net_chargeable_income)

    #################### display result
    st.divider()
    st.markdown("Computation of Estimated Salaries Tax Liabilities")
    value = [int(total_income), int(deductions), int(total_allowances), int(net_chargeable_income), int(tax)]
    index = ["Total Income", "Deductions", "Total Allowances", "Net Chargeable Income", "Tax Payable"]
    df = pd.DataFrame(value, index=index, columns=["HKD"])
    st.table(df)

elif status == "Married":
    st.header("Salary Tax Calculator for 2023/24")
    st.caption("For Married, tax payable is ONLY calculated under Joint Assessment Scheme in which progressive tax is adopted.")

    st.divider()
    st.subheader("Part 1.1 - Self Income")
    st.markdown("1. Income")
    i1 = st.number_input("Please input Self value:", min_value=0.0)
    st.markdown("2. Value of all places of residence provided by employer or associated corporation")
    i2 = st.number_input("Note: The value of all places of residence provided cannot exceed 10% of your income. Please input Self value:", min_value=0.0, max_value=i1*0.1)
    st.subheader("Part 1.2 - Spouse Income")
    st.markdown("1. Income")
    i3 = st.number_input("Please input Spouse value:", min_value=0.0)
    st.markdown("2. Value of all places of residence provided by employer or associated corporation")
    i4 = st.number_input("Note: The value of all places of residence provided cannot exceed 10% of your income. Please input Spouse value:", min_value=0.0, max_value=i1*0.1)

    st.divider()
    st.subheader("Part 2.1 - Self Deductions")
    st.markdown("1. Self Education Expenses")
    d1 = st.number_input("Please input Self value from HKD 0 - HKD 100,000:", min_value=0.0, max_value=100000.0)
    st.markdown("2. Approved Charitable Donations")
    d2 = st.number_input("Note: The deductible Approved Charitable Donations cannot exceed 35% of your income. Please input Self value:", min_value=0.0, max_value=(i1+i2)*0.35)
    st.markdown("3. Mandatory Contributions to Recognized Retirement Schemes")
    d3 = st.number_input("Please input Self value from HKD 0 - HKD 18,000:", min_value=0.0, max_value=18000.0)
    st.markdown("4. Tax Deductible MPF Voluntary Contributions")
    d4 = st.number_input("Please input Self value from HKD 0 - HKD 60,000:", min_value=0.0, max_value=60000.0)
    st.markdown("5.Qualifying Annuity Premiums")
    d5 = st.number_input("Note: Total deductible MPF Voluntary Contributions and Annuity Premiums cannot exceed HKD 60,000. Please input Self value:", min_value=0.0, max_value=60000.0-d4)
    st.markdown("6. Domestic Rental Expenses")
    d6 = st.number_input("Note: If you are married for the full year, the total Domestic Rental Expenses claimed by you and your spouse cannot exceed $100,000. Please input Self value from HKD 0 - HKD 100,000:", min_value=0.0, max_value=100000.0)
    st.markdown("7. Home Loan Interest")
    d7 = st.number_input("Please input Self value from HKD 0 - HKD 100,000:", min_value=0.0, max_value=100000.0, key="d7")
    st.markdown("8. Qualifying Health Insurance Premiums")
    d8 = st.number_input("Note: Maximum for self is HKD 8,000. Amount paid for self. Please input Self value:", min_value=0.0, max_value=8000.0)
    d9 = st.selectbox("No. of specified relative(s). Please input Self value:", list(range(5)))
    d10 = st.number_input("Note: Maximum for each relative is HKD 8,000. Amount paid for specified relative(s). Please input Self value:", min_value=0.0, max_value=d9*8000.0)
    st.markdown("9. Elderly Residential Care Expenses")
    d11 = st.selectbox("No. of dependant(s) resided in residential care home. Please input Self value:", list(range(5)))
    d12 = st.selectbox("No. of dependant(s) eligible for Disabled Dependant Allowance. Please input Self value:", list(range(d11+1)))
    d13 = st.number_input("Note: Maximum is HKD 100,000. Amount paid to residential care home. Please input Self value:", min_value=0.0, max_value=100000.0)
    st.markdown("Allowances")
    d14 = st.selectbox("Eligible to claim Personal Disability Allowance. Please input Self value:", ['No', 'Yes'])

    st.subheader("Part 2.2 - Spouse Deductions")
    st.markdown("1. Self Education Expenses")
    d15 = st.number_input("Please input Spouse value from HKD 0 - HKD 100,000:", min_value=0.0, max_value=100000.0)
    st.markdown("2. Approved Charitable Donations")
    d16 = st.number_input("Note: The deductible Approved Charitable Donations cannot exceed 35% of your income. Please input Spouse value:", min_value=0.0, max_value=(i1+i2)*0.35)
    st.markdown("3. Mandatory Contributions to Recognized Retirement Schemes")
    d17 = st.number_input("Please input Spouse value from HKD 0 - HKD 18,000:", min_value=0.0, max_value=18000.0)
    st.markdown("4. Tax Deductible MPF Voluntary Contributions")
    d18 = st.number_input("Please input Spouse value from HKD 0 - HKD 60,000:", min_value=0.0, max_value=60000.0)
    st.markdown("5.Qualifying Annuity Premiums")
    d19 = st.number_input("Note: Total deductible MPF Voluntary Contributions and Annuity Premiums cannot exceed HKD 60,000. Please input Spouse value:", min_value=0.0, max_value=60000.0-d4)
    st.markdown("6. Domestic Rental Expenses")
    d20 = st.number_input("Note: If you are married for the full year, the total Domestic Rental Expenses claimed by you and your spouse cannot exceed $100,000. Please input Spouse value from HKD 0 - HKD 100,000:", min_value=0.0, max_value=100000.0)
    st.markdown("7. Home Loan Interest")
    d21 = st.number_input("Please input Spouse value from HKD 0 - HKD 100,000:", min_value=0.0, max_value=100000.0, key="d21")
    st.markdown("8. Qualifying Health Insurance Premiums")
    d22 = st.number_input("Note: Maximum for self is HKD 8,000. Amount paid for self. Please input Spouse value:", min_value=0.0, max_value=8000.0)
    d23 = st.selectbox("No. of specified relative(s). Please input Spouse value:", list(range(5)))
    d24 = st.number_input("Note: Maximum for each relative is HKD 8,000. Amount paid for specified relative(s). Please input Spouse value:", min_value=0.0, max_value=d9*8000.0)
    st.markdown("9. Elderly Residential Care Expenses")
    d25 = st.selectbox("No. of dependant(s) resided in residential care home. Please input Spouse value:", list(range(5)))
    d26 = st.selectbox("No. of dependant(s) eligible for Disabled Dependant Allowance. Please input Spouse value:", list(range(d11+1)))
    d27 = st.number_input("Note: Maximum is HKD 100,000. Amount paid to residential care home. Please input Spouse value:", min_value=0.0, max_value=100000.0)
    st.markdown("Allowances")
    d28 = st.selectbox("Eligible to claim Personal Disability Allowance. Please input Spouse value:", ['No', 'Yes'])

    st.divider()
    st.subheader("Part 3 - Allowances")
    st.markdown("Other Allowances Claimed")
    st.markdown("1. No. of dependent children Born in the year")
    a1 = st.selectbox("Please select input:", list(range(10)))
    a2 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a1+1)))
    st.markdown("2. No. of dependent children NOT Born in the year")
    a3 = st.selectbox("Please select input:", list(range(10)), key="a3")
    a4 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a3+1)), key="a4")
    st.markdown("3. No. of dependent brothers / sisters")
    a6 = st.selectbox("Please select input:", list(range(10)), key="a6")
    a7 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a6+1)), key="a7")
    st.markdown("4. Dependent parents/grandparents aged 60 or over, or aged under 60 but eligible to claim Government's Disability Allowance")
    a8 = st.selectbox("Case 1 - No. of dependent parents/grandparents Resided with you", list(range(5)), key="a8")
    a9 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a8+1)), key="a9")
    a10 = st.selectbox("Case 2 - No. of dependent parents/grandparents NOT Resided with you", list(range(5)), key="a10")
    a11 = st.selectbox("Of the dependant(s) claimed above, No. of dependant(s) eligible for Disabled Dependant Allowance:", list(range(a10+1)), key="a11")
    st.markdown("5. Dependent parents/grandparents aged 55 or over but under 60")
    a12 = st.selectbox("Case 1 - No. of dependent parents/grandparents Resided with you", list(range(5)), key="a12")
    a13 = st.selectbox("Case 2 - No. of dependent parents/grandparents NOT Resided with you", list(range(a12+1)), key="a13")
    st.markdown("6. Your Spouse is eligible for Disabled Dependant Allowance:")
    a14 = st.selectbox("Please select input:", ['No', 'Yes'])

    #################### calculation
    total_income = i1+i2+i3+i4
    self_deductions = d1+d2+d3+d4+d5+d6+d7+d8+d10+d13
    spouse_deductions = d15+d16+d17+d18+d19+d20+d21+d22+d24+d27
    deductions = self_deductions+spouse_deductions
    married = 264000
    no_of_disabled_dependants = d12+a2+a4+a7+a9+a11+d26
    other_allowances = a1*260000 + a3*130000 + a6*37500 + a8*100000 + a10*50000 + a12*50000 + a13*25000

    personal_disability_allowance = 0
    if d14 == 'Yes': personal_disability_allowance += 75000
    if d28 == 'Yes': personal_disability_allowance += 75000

    disabled_dependants_allowances = 75000*no_of_disabled_dependants
    if a14 == 'Yes': disabled_dependants_allowances += 75000

    total_allowances = married + other_allowances + disabled_dependants_allowances + personal_disability_allowance
    net_chargeable_income = total_income - deductions - total_allowances

    if net_chargeable_income < 0: net_chargeable_income = 0

    tax = tax_payable_function(2, net_chargeable_income)

    #################### display result
    st.divider()
    st.markdown("Computation of Estimated Salaries Tax Liabilities")
    value = [int(total_income), int(deductions), int(total_allowances), int(net_chargeable_income), int(tax)]
    index = ["Total Income", "Deductions", "Total Allowances", "Net Chargeable Income", "Tax Payable"]
    df = pd.DataFrame(value, index=index, columns=["HKD"])
    st.table(df)




