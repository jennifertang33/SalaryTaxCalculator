from salary_computation.allowances_function import allowances_function
from salary_computation.deductions_function import deductions_function
from salary_computation.income_function import income_function
from salary_computation.marital_function import marital_function
from salary_computation.tax_payable_function import tax_payable_function


def main():
    """
    For Single / Separated / Divorced / Widowed, tax payable is calculated by the lowerest of progressive tax and standard tax.
    For Married, tax payable is ONLY calculated under Joint Assessment Scheme in which progressive tax is adopted.
    """
     
    total_income = []
    deductions = []
    disabled_dependant_deductions = []
    personal_disability_allowance = []
    others_allowance = []
    disabled_dependant_allowances = []
    
    people = marital_function()
    
    for i in range(len(people)):
        total_income.append(income_function(people[i]))
        a, b, c = deductions_function(total_income[i], people[i])
        deductions.append(a)
        disabled_dependant_deductions.append(b)
        personal_disability_allowance.append(c)
        
    d, e = allowances_function(people)
    others_allowance.append(d)
    disabled_dependant_allowances.append(e)
    
    if people == ['Self']:
        basic = 132000
    else:
        basic = 264000
        
    total_allowances = basic + sum(others_allowance) + sum(personal_disability_allowance) + sum(disabled_dependant_allowances) + sum(disabled_dependant_deductions)
    net_chargeable_income = sum(total_income) - sum(deductions) - total_allowances
        
    if net_chargeable_income <= 0:
        net_chargeable_income = 0
        tax_payable = 0
    else:
        tax_payable = tax_payable_function(people, net_chargeable_income)
    
    ###
    print(f"Total Income: {int(sum(total_income))}")
    print(f"Deductions: {int(sum(deductions))}")
    print(f"Total Allowances: {int(total_allowances)}")
    print(f"Net Chargeable Income: {int(net_chargeable_income)}")
    
    if people == ['Self']:
        return f"Tax Payable by You: {int(tax_payable)}"
    else:
        return f"Tax Payable by You and Your Spouse: {int(tax_payable)}"


print(main())