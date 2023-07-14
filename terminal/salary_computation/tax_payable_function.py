def tax_payable_function(people, net_chargeable_income):    
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

    ######
    #print(f"tax: {tax}")
    #print(f"standard_tax: {standard_tax}")
    ######
        
    if people == ['Self']:        
        if tax < standard_tax:
            return tax
        else:
            return standard_tax
    else:
        return tax 