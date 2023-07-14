def deductions_function(income, params):
    total = 0
    
    #####
    # 1. Self Education Expenses
    print("1. Self Education Expenses")
    print("                                 ")
    while True:
        a = input(f"Please input {params} value from HKD 0 - HKD 100,000: ")
        try:
            a = float(a)
            if a>=0 and a<=100000:
                total += a
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    #####
    # 2. Approved Charitable Donations
    print("2. Approved Charitable Donations")
    print("                                 ")
    print("Note: The deductible Approved Charitable Donations cannot exceed 35% of your income.")
    print("                                 ")
    while True:
        b = input(f"Please input {params} value: ")
        try:
            b = float(b)
            if b>=0 and b<=income*0.35:
                total += b
                break
            elif b>income*0.35:
                total += income*0.35
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    #####
    # 3. Mandatory Contributions to Recognized Retirement Schemes
    print("3. Mandatory Contributions to Recognized Retirement Schemes")
    print("                                 ")
    while True:
        c = input(f"Please input {params} value from HKD 0 - HKD 18,000: ")
        try:
            c = float(c)
            if c>=0 and c<=18000:
                total += c
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    #####
    # 4. Tax Deductible MPF Voluntary Contributions
    print("4. Tax Deductible MPF Voluntary Contributions")
    print("                                 ")
    while True:
        d = input(f"Please input {params} value from HKD 0 - HKD 60,000: ")
        try:
            d = float(d)
            if d>=0 and d<=60000:
                total += d
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    #####
    # 5. Qualifying Annuity Premiums
    print("5. Qualifying Annuity Premiums")
    print("                                 ")
    print("Note: Total deductible MPF Voluntary Contributions and Annuity Premiums cannot exceed HKD 60,000.")
    print("                                 ")
    while True:
        e = input(f"Please input {params} value: ")
        try:
            e = float(e)
            if e>=0 and e<=60000-d:
                total += e
                break
            elif e>60000-d:
                total += 60000-d
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    #####
    # 6. Domestic Rental Expenses
    print("6. Domestic Rental Expenses")
    print("                                 ")
    print("Note: If you are married for the full year, the total Domestic Rental Expenses claimed by you and your spouse cannot exceed $100,000.")
    print("                                 ")
    while True:
        f = input(f"Please input {params} value from HKD 0 - HKD 100,000: ")
        try:
            f = float(f)
            if f>=0 and f<=100000:
                total += f
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    #####
    # 7. Home Loan Interest
    print("7. Home Loan Interest")
    print("                                 ")
    while True:
        g = input(f"Please input {params} value from HKD 0 - HKD 100,000: ")
        try:
            g = float(g)
            if g>=0 and g<=100000:
                total += g
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    #####
    # 8. Qualifying Health Insurance Premiums
    print("8. Qualifying Health Insurance Premiums")
    print("                                 ")
    while True:
        h = input(f"Amount paid for self (Please input {params} value from HKD 0 - HKD 8,000): ")
        try:
            h = float(h)
            if h>=0 and h<=8000:
                total += h
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("                                 ")
    
    while True:
        i = input(f"No. of specified relative(s) (Please input {params} value '0 - 4'): ")
        try:
            i = int(i)
            if i in range(5):
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("                                 ")
    
    while True:
        j = input(f"Amount paid for specified relative(s) (Please input {params} value) \nNote: Maximum Limit is HKD 8,000 for each relative: ")
        if i != 0:
            try:
                j = float(j)           
                if j/i>=0 and j/i<=8000:
                    total += j
                    break
                elif j/i>8000:
                    total += 8000*i
                    break
                else:
                    print("Input Error, Please enter it again!!!")
                
            except:
                print("Input Error, Please enter it again!!!")
        else:
            break
    print("---------------------------------")
    
    #####
    # 9. Elderly Residential Care Expenses
    print("9. Elderly Residential Care Expenses")
    print("                                 ")    
    while True:
        k = input(f"No. of dependant(s) resided in residential care home (Please input {params} value '0 - 4'): ")
        try:
            k = int(k)
            if k in range(5):
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("                                 ")
    
    while True:
        l = input(f"No. of dependant(s) eligible for Disabled Dependant Allowance (Please input {params} value '0 - 4'): ")
        try:
            l = int(l)
            if l in range(5):
                disabled_dependant_deductions = 75000*l
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("                                 ")
        
    while True:
        m = input(f"Amount paid to residential care home (Please input {params} value from HKD 0 - HKD 100,000): ")
        try:
            m = float(m)
            if m>=0 and m<=100000:
                total += m
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    #####
    # Allowances - Personal Disability Allowance
    print("Allowances - Personal Disability Allowance")
    print("                                 ")    
    while True:
        n = input(f"Eligible to claim Personal Disability Allowance (Please input {params} value 'y' or 'n'): ")
        try:
            if n == 'y':
                personal_disability_allowance = 75000
                break
            elif n == 'n':
                personal_disability_allowance = 0
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
        
    return (total, disabled_dependant_deductions, personal_disability_allowance)