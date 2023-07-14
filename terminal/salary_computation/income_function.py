def income_function(params):    
    total_income = 0
    
    # 1. Income
    print("Income for the year of assessment 2023/24")
    print("                                 ")
    while True:
        income = input(f"Please input {params} value: ")
        try:
            income = float(income)
            if income >= 0:                
                total_income += income                
                break                
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")    
    print("---------------------------------")
    
    # 2. Value of residence
    print("Value of all places of residence provided by employer or associated corporation")
    print(" ")
    print("Note: The value of all places of residence provided cannot exceed 10% of your income.")
    print(" ")
    while True:
        residence = input(f"Please input {params} value: ")
        try:
            residence = float(residence)
            if residence>=0 and residence<=income*0.1:
                total_income += residence
                break
            elif residence>income*0.1:
                total_income += income*0.1
                break
            else:
                print("Input Error, Please enter it again!!!")
        except:
            print("Input Error, Please enter it again!!!")
    print("---------------------------------")
    
    return total_income