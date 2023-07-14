def marital_function():
    while True:
        marital_status = input("Marital status \n(Please input '1' for Single / Separated / Divorced / Widowed OR '2' for Married): ")
        if marital_status=='1':
            people = ['Self']
            break
        elif marital_status=='2':
            people = ['Self', 'Spouse']
            break
        else:
            print("Input Error, Please enter it again!!!")
    return people    