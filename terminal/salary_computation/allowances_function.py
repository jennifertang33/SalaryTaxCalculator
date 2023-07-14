def allowances_function(people):
    others=0
    disabled_dependant_allowances=0
    
    #####
    # 1. Child Allowance - Born in the year
    print("1. Child Allowance - Born in the year")
    print("                                 ") 
    while True:
        a = input("No. of dependent children Born in the year \n(Please input '0 - 9'): ")
        try: 
            a = int(a)
            if a in range(10):
                others += 260000*a
                break
            else:
                print("Input Error, Please enter it again!!!")
        except: 
            print("Input Error, Please enter it again!!!")            
    print("                                 ")
    
    print("Of the dependant(s) claimed above, ")
    while True:
        b = input("No. of dependant(s) eligible for Disabled Dependant Allowance: ")
        try: 
            b = int(b)
            if b in range(a+1):
                disabled_dependant_allowances += 75000*b
                break
            else:
                print("Input Error, Please enter it again!!!")
        except: 
            print("Input Error, Please enter it again!!!")            
    print("---------------------------------")
    
    #####
    # 2. Child Allowance - Born in other years
    print("2. Child Allowance - Born in other years")
    print("                                 ") 
    while True:
        c = input("No. of dependent children Born in other years \n(Please input '0 - 9'): ")
        try: 
            c = int(c)
            if c in range(10):
                others += 130000*c
                break
            else:
                print("Input Error, Please enter it again!!!")
        except: 
            print("Input Error, Please enter it again!!!")            
    print("                                 ")
    
    print("Of the dependant(s) claimed above, ")
    while True:
        d = input("No. of dependant(s) eligible for Disabled Dependant Allowance: ")
        try: 
            d = int(d)
            if d in range(c+1):
                disabled_dependant_allowances += 75000*d
                break
            else:
                print("Input Error, Please enter it again!!!")
        except: 
            print("Input Error, Please enter it again!!!")            
    print("---------------------------------")
    
    #####
    # 3. Dependent Brother or Sister Allowance
    print("3. Dependent Brother or Sister Allowance")
    print("                                 ") 
    while True:
        e = input("No. of dependent brothers / sisters \n(Please input '0 - 9'): ")
        try: 
            e = int(e)
            if e in range(10):
                others += 37500*e
                break
            else:
                print("Input Error, Please enter it again!!!")
        except: 
            print("Input Error, Please enter it again!!!")
    print("                                 ")
    
    print("Of the dependant(s) claimed above, ")
    while True:
        f = input("No. of dependant(s) eligible for Disabled Dependant Allowance: ")
        try: 
            f = int(f)
            if f in range(e+1):
                disabled_dependant_allowances += 75000*f
                break
            else:
                print("Input Error, Please enter it again!!!")
        except: 
            print("Input Error, Please enter it again!!!")                             
    print("---------------------------------")
    
    #####
    # 4. Dependent parents/grandparents aged 60 or over, or aged under 60 but eligible to claim Government's Disability Allowance
    print("4. Dependent parents/grandparents aged 60 or over, \nor aged under 60 but eligible to claim Government's Disability Allowance")
    print("                                 ")
    while True:
        g = input("Case 1 - No. of dependent parents/grandparents Resided with you \n(Please input '0 - 4'): ")
        try:
            g = int(g)
            if g in range(5):
                others += 100000*g
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("                                 ")    
       
    print("Of the dependant(s) claimed above, ")
    while True:
        h = input("No. of dependant(s) eligible for Disabled Dependant Allowance: ")
        try: 
            h = int(h)
            if h in range(g+1):
                disabled_dependant_allowances += 75000*h
                break
            else:
                print("Input Error, Please enter it again!!!")
        except: 
            print("Input Error, Please enter it again!!!")
    print("                                 ")
    
    while True:
        i = input("Case 2 - No. of dependent parents/grandparents NOT Resided with you \n(Please input '0 - 4'): ")
        try:
            i = int(i)
            if i in range(5):
                others += 50000*i
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("                                 ")    
       
    print("Of the dependant(s) claimed above, ")
    while True:
        j = input("No. of dependant(s) eligible for Disabled Dependant Allowance: ")
        try: 
            j = int(j)
            if j in range(i+1):
                disabled_dependant_allowances += 75000*j
                break
            else:
                print("Input Error, Please enter it again!!!")
        except: 
            print("Input Error, Please enter it again!!!")         
    print("---------------------------------")
    
    #####
    # 5. Dependent parents/grandparents aged 55 or over but under 60
    print("5. Dependent parents/grandparents aged 55 or over but under 60")
    print("                                 ")
    while True:
        k = input("Case 1 - No. of dependent parents/grandparents Resided with you \n(Please input '0 - 4'): ")
        try:
            k = int(k)
            if k in range(5):
                others += 50000*k
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("                                 ")
    
    while True:
        l = input("Case 2 - No. of dependent parents/grandparents NOT Resided with you \n(Please input '0 - 4'): ")
        try:
            l = int(l)
            if l in range(5):
                others += 25000*l
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    #####
    if people == ['Self']:
        while True:
            m = input("Are you eligible for Single Parent Allowance? (Please input 'y' OR 'n'): ")
            try:
                if m == 'y':
                    others += 132000
                    break
                elif m == 'n':
                    break
                else:
                    print("Input Error, Please enter it again!!!")
            except:
                print("Input Error, Please enter it again!!!")
        print("---------------------------------")
                                
    else:
        while True:
            n = input("Are your spouse eligible for Disabled Dependant Allowrance? (Please input 'y' OR 'n'): ")
            try:
                if n == 'y':
                    disabled_dependant_allowances += 75000
                    break
                elif n == 'n':
                    break
                else:
                    print("Input Error, Please enter it again!!!")
            except:
                print("Input Error, Please enter it again!!!")
        print("---------------------------------")        
    
    return (others, disabled_dependant_allowances)