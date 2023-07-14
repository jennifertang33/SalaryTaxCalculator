from tkinter import *
from tkinter import ttk
from tokenize import Floatnumber

###

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

def myfunction():

    if marital_status.get() == "Single / Separated / Divorced / Widowed":
        
        total_income = float(i1.get())+float(i2.get())
        deductions = float(d1.get())+float(d2.get())+float(d3.get())+float(d4.get())+float(d5.get())+float(d6.get())+float(d7.get())+float(d8.get())+float(d10.get())+float(d13.get())
        basic = 132000
        no_of_disabled_dependants = float(d12.get())+float(a2.get())+float(a4.get())+float(a7.get())+float(a9.get())+float(a11.get())
        other_allowances = float(a1.get())*260000 + float(a3.get())*130000 + float(a6.get())*37500 + float(a8.get())*100000 + float(a10.get())*50000 + float(a12.get())*50000 + float(a13.get())*25000

        personal_disability_allowance = 0
        if d14.get() == 'Yes': personal_disability_allowance += 75000

        disabled_dependants_allowances = 75000*no_of_disabled_dependants
        
        single_parent_allowance = 0
        if a5.get() == 'Yes': single_parent_allowance += 132000
        
        total_allowances = basic + other_allowances + disabled_dependants_allowances + personal_disability_allowance + single_parent_allowance
        net_chargeable_income = total_income - deductions - total_allowances

        if net_chargeable_income < 0: net_chargeable_income = 0

        tax = tax_payable_function(1, net_chargeable_income)    

    else:

        total_income = float(i1.get())+float(i2.get())+float(i3.get())+float(i4.get())
        self_deductions = float(d1.get())+float(d2.get())+float(d3.get())+float(d4.get())+float(d5.get())+float(d6.get())+float(d7.get())+float(d8.get())+float(d10.get())+float(d13.get())
        spouse_deductions = float(d15.get())+float(d16.get())+float(d17.get())+float(d18.get())+float(d19.get())+float(d20.get())+float(d21.get())+float(d22.get())+float(d24.get())+float(d27.get())
        deductions = self_deductions+spouse_deductions
        married = 264000
        no_of_disabled_dependants = float(d12.get())+float(a2.get())+float(a4.get())+float(a7.get())+float(a9.get())+float(a11.get())+float(d26.get())
        other_allowances = float(a1.get())*260000 + float(a3.get())*130000 + float(a6.get())*37500 + float(a8.get())*100000 + float(a10.get())*50000 + float(a12.get())*50000 + float(a13.get())*25000

        personal_disability_allowance = 0
        if d14.get() == 'Yes': personal_disability_allowance += 75000
        if d28.get() == 'Yes': personal_disability_allowance += 75000

        disabled_dependants_allowances = 75000*no_of_disabled_dependants
        if a14.get() == 'Yes': disabled_dependants_allowances += 75000

        total_allowances = married + other_allowances + disabled_dependants_allowances + personal_disability_allowance
        net_chargeable_income = total_income - deductions - total_allowances

        if net_chargeable_income < 0: net_chargeable_income = 0

        tax = tax_payable_function(2, net_chargeable_income)

    result1.config(text="Total Income: " + str(int(total_income)))
    result2.config(text="Deductions: " + str(int(deductions)))
    result3.config(text="Total Allowances: " + str(int(total_allowances)))
    result4.config(text="Net Chargeable Income: " + str(int(net_chargeable_income)))
    result5.config(text="Tax Payable: " + str(int(tax)))
###

window = Tk()
window.title("Salary Tax Calculator for 2023/24")

canvas = Canvas(window)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(window, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Link the scrollbar to the Canvas widget
canvas.configure(yscrollcommand=scrollbar.set)

# Create a Frame to hold the content of the window
content = Frame(canvas)
canvas.create_window((0, 0), window=content, anchor='nw')

##
frame = Frame(content)
frame.pack()

### 1st Frame - Marital Status
frame1 = LabelFrame(frame, text="Marital Status")
frame1.grid(row=0, column=0, sticky="news", padx=20, pady=10)

marital_status = ttk.Combobox(frame1, values=["Single / Separated / Divorced / Widowed", "Married"])
marital_status.current(0)
marital_status.grid(row=0, column=0)

### 2nd Frame - Income
frame2 = LabelFrame(frame, text="Income")
frame2.grid(row=1, column=0, sticky="news", padx=20, pady=10)

self_label = Label(frame2, text="Self")
self_label.grid(row=0, column=1)
spouse_label = Label(frame2, text="Spouse")
spouse_label.grid(row=0, column=2)

income_label = Label(frame2, text="Income of the year")
income_label.grid(row=1, column=0, sticky="W")
i1 = Entry(frame2, textvariable=IntVar())
i1.grid(row=1, column=1)
i3 = Entry(frame2, textvariable=IntVar())
i3.grid(row=1, column=2)

residence_label = Label(frame2, text="Value of residence provided by employer or associated corporation", anchor="w", justify="left")
residence_label.grid(row=2, column=0)
i2 = Entry(frame2, textvariable=IntVar())
i2.grid(row=2, column=1)
i4 = Entry(frame2, textvariable=IntVar())
i4.grid(row=2, column=2)

### 3rd Frame - Deductions
frame3 = LabelFrame(frame, text="Deductions")
frame3.grid(row=2, column=0, sticky="news", padx=20, pady=10)

self_label = Label(frame3, text="Self")
self_label.grid(row=0, column=1)
spouse_label = Label(frame3, text="Spouse")
spouse_label.grid(row=0, column=2)

d1_label = Label(frame3, text="1. Self Education Expenses\n(HKD 0 - HKD 100,000)", justify=LEFT)
d1_label.grid(row=1, column=0, sticky="W")
d1 = Entry(frame3, textvariable=IntVar())
d1.grid(row=1, column=1)
d15 = Entry(frame3, textvariable=IntVar())
d15.grid(row=1, column=2)

d2_label = Label(frame3, text="2. Approved Charitable Donations\n(Note: The deductible Approved Charitable Donations cannot\nexceed 35% of your income.)", justify=LEFT)
d2_label.grid(row=2, column=0, sticky="W")
d2 = Entry(frame3, textvariable=IntVar())
d2.grid(row=2, column=1)
d16 = Entry(frame3, textvariable=IntVar())
d16.grid(row=2, column=2)

d3_label = Label(frame3, text="3. Mandatory Contributions to Recognized Retirement Schemes\n(HKD 0 - HKD 18,000)", justify=LEFT)
d3_label.grid(row=3, column=0, sticky="W")
d3 = Entry(frame3, textvariable=IntVar())
d3.grid(row=3, column=1)
d17 = Entry(frame3, textvariable=IntVar())
d17.grid(row=3, column=2)

d4_label = Label(frame3, text="4. Tax Deductible MPF Voluntary Contributions\n(HKD 0 - HKD 60,000)", justify=LEFT)
d4_label.grid(row=4, column=0, sticky="W")
d4 = Entry(frame3, textvariable=IntVar())
d4.grid(row=4, column=1)
d18 = Entry(frame3, textvariable=IntVar())
d18.grid(row=4, column=2)

d5_label = Label(frame3, text="5. Qualifying Annuity Premiums\n(Note: Total deductible MPF Voluntary Contributions and\nAnnuity Premiums cannot exceed HKD 60,000.)", justify=LEFT)
d5_label.grid(row=5, column=0, sticky="W")
d5 = Entry(frame3, textvariable=IntVar())
d5.grid(row=5, column=1)
d19 = Entry(frame3, textvariable=IntVar())
d19.grid(row=5, column=2)

d6_label = Label(frame3, text="6. Domestic Rental Expenses\n(Note: If you are married for the full year, the total\nDomestic Rental Expenses claimed by you and your spouse\ncannot exceed $100,000.)", justify=LEFT)
d6_label.grid(row=6, column=0, sticky="W")
d6 = Entry(frame3, textvariable=IntVar())
d6.grid(row=6, column=1)
d20 = Entry(frame3, textvariable=IntVar())
d20.grid(row=6, column=2)

d7_label = Label(frame3, text="7. Home Loan Interest\n(HKD 0 - HKD 100,000)", justify=LEFT)
d7_label.grid(row=7, column=0, sticky="W")
d7 = Entry(frame3, textvariable=IntVar())
d7.grid(row=7, column=1)
d21 = Entry(frame3, textvariable=IntVar())
d21.grid(row=7, column=2)

d8_label = Label(frame3, text="8. Qualifying Health Insurance Premiums")
d8_label.grid(row=8, column=0, sticky="W")
d8_1_label = Label(frame3, text="- Amount paid for self\n(Note: Maximum for self is HKD 8,000.)", justify=LEFT)
d8_1_label.grid(row=9, column=0, sticky="W")
d8 = Entry(frame3, textvariable=IntVar())
d8.grid(row=9, column=1)
d22 = Entry(frame3, textvariable=IntVar())
d22.grid(row=9, column=2)

d9_label = Label(frame3, text="- No. of specified relative(s)")
d9_label.grid(row=10, column=0, sticky="W")
d9 = ttk.Combobox(frame3, values=list(range(5)))
d9.current(0)
d9.grid(row=10, column=1)
d23 = ttk.Combobox(frame3, values=list(range(5)))
d23.current(0)
d23.grid(row=10, column=2)

d10_label = Label(frame3, text="- Amount paid for specified relative(s)\n(Note: Maximum for each relative is HKD 8,000.)", justify=LEFT)
d10_label.grid(row=11, column=0, sticky="W")
d10 = Entry(frame3, textvariable=IntVar())
d10.grid(row=11, column=1)
d24 = Entry(frame3, textvariable=IntVar())
d24.grid(row=11, column=2)

d11_label = Label(frame3, text="9. Elderly Residential Care Expenses")
d11_label.grid(row=12, column=0, sticky="W")
d11_1_label = Label(frame3, text="- No. of dependant(s) resided in residential care home")
d11_1_label.grid(row=13, column=0, sticky="W")
d11 = ttk.Combobox(frame3, values=list(range(5)))
d11.current(0)
d11.grid(row=13, column=1)
d25 = ttk.Combobox(frame3, values=list(range(5)))
d25.current(0)
d25.grid(row=13, column=2)

d12_label = Label(frame3, text="- No. of dependant(s) eligible for Disabled Dependant Allowance")
d12_label.grid(row=14, column=0, sticky="W")
d12 = ttk.Combobox(frame3, values=list(range(5)))
d12.current(0)
d12.grid(row=14, column=1)
d26 = ttk.Combobox(frame3, values=list(range(5)))
d26.current(0)
d26.grid(row=14, column=2)

d13_label = Label(frame3, text="- Amount paid to residential care home\n(Note: Maximum is HKD 100,000.)", justify=LEFT)
d13_label.grid(row=15, column=0, sticky="W")
d13 = Entry(frame3, textvariable=IntVar())
d13.grid(row=15, column=1)
d27 = Entry(frame3, textvariable=IntVar())
d27.grid(row=15, column=2)

d14_label = Label(frame3, text="Allowances")
d14_label.grid(row=17, column=0, sticky="W")
d14_1_label = Label(frame3, text="Eligible to claim Personal Disability Allowance")
d14_1_label.grid(row=18, column=0, sticky="W")
d14 = ttk.Combobox(frame3, values=["Yes", "No"])
d14.current(1)
d14.grid(row=18, column=1)
d28 = ttk.Combobox(frame3, values=["Yes", "No"])
d28.current(1)
d28.grid(row=18, column=2)

### 4th Frame - Other Allowances Claimed
frame4 = LabelFrame(frame, text="Other Allowances Claimed")
frame4.grid(row=3, column=0, sticky="news", padx=20, pady=10)

label1 = Label(frame4, text="No. of dependant(s) claimed")
label1.grid(row=0, column=1)
label2 = Label(frame4, text="Of the dependant(s) claimed,\nNo. of dependant(s) eligible for\nDisabled Dependant Allowance")
label2.grid(row=0, column=2)

a1_label = Label(frame4, text="1. No. of dependent children")
a1_label.grid(row=1, column=0, sticky="W")
a1_1_label = Label(frame4, text="- Born in the year")
a1_1_label.grid(row=2, column=0, sticky="W")
a1 = ttk.Combobox(frame4, values=list(range(10)))
a1.current(0)
a1.grid(row=2, column=1)
a2 = ttk.Combobox(frame4, values=list(range(10)))
a2.current(0)
a2.grid(row=2, column=2)

a3_label = Label(frame4, text="- Born in other year(s)")
a3_label.grid(row=3, column=0, sticky="W")
a3 = ttk.Combobox(frame4, values=list(range(10)))
a3.current(0)
a3.grid(row=3, column=1)
a4 = ttk.Combobox(frame4, values=list(range(10)))
a4.current(0)
a4.grid(row=3, column=2)

a6_label = Label(frame4, text="2. No. of dependent brothers / sisters")
a6_label.grid(row=4, column=0, sticky="W")
a6 = ttk.Combobox(frame4, values=list(range(10)))
a6.current(0)
a6.grid(row=4, column=1)
a7 = ttk.Combobox(frame4, values=list(range(10)))
a7.current(0)
a7.grid(row=4, column=2)

a8_label = Label(frame4, text="3. No. of dependent parents/grandparents\naged 60 or over, or aged under 60 but eligible to\nclaim Government's Disability Allowance", justify=LEFT)
a8_label.grid(row=5, column=0, sticky="W")
a8_1_label = Label(frame4, text="- Resided with you throughout the year")
a8_1_label.grid(row=6, column=0, sticky="W")
a8 = ttk.Combobox(frame4, values=list(range(5)))
a8.current(0)
a8.grid(row=6, column=1)
a9 = ttk.Combobox(frame4, values=list(range(5)))
a9.current(0)
a9.grid(row=6, column=2)

a10_label = Label(frame4, text="- NOT Resided with you throughout the year")
a10_label.grid(row=7, column=0, sticky="W")
a10 = ttk.Combobox(frame4, values=list(range(5)))
a10.current(0)
a10.grid(row=7, column=1)
a11 = ttk.Combobox(frame4, values=list(range(5)))
a11.current(0)
a11.grid(row=7, column=2)

a12_label = Label(frame4, text="4. No. of dependent parents/grandparents\naged 55 or over but under 60", justify=LEFT)
a12_label.grid(row=8, column=0, sticky="W")
a12_1_label = Label(frame4, text="- Resided with you throughout the year")
a12_1_label.grid(row=9, column=0, sticky="W")
a12 = ttk.Combobox(frame4, values=list(range(5)))
a12.current(0)
a12.grid(row=9, column=1)

a13_label = Label(frame4, text="- NOT Resided with you throughout the year")
a13_label.grid(row=10, column=0, sticky="W")
a13 = ttk.Combobox(frame4, values=list(range(5)))
a13.current(0)
a13.grid(row=10, column=1)

### 5th Frame - Other Allowances Claimed continued
frame5 = LabelFrame(frame, text="Other Allowances Claimed continued")
frame5.grid(row=4, column=0, sticky="news", padx=20, pady=10)

a5_label = Label(frame5, text="Eligible for Single Parent Allowance", justify=LEFT)
a5_label.grid(row=0, column=0, sticky="W")
a5 = ttk.Combobox(frame5, values=["Yes", "No"])
a5.current(1)
a5.grid(row=0, column=1)

a14_label = Label(frame5, text="Your spouse is eligible for Disabled Dependant Allowance")
a14_label.grid(row=1, column=0, sticky="W")
a14 = ttk.Combobox(frame5, values=["Yes", "No"])
a14.current(1)
a14.grid(row=1, column=1)

button = Button(frame5, command=myfunction, text="Submit")
button.grid(row=2, column=1, sticky=W)

### 6th Frame - Result
frame6 = LabelFrame(frame, text="Computation of Estimated Salaries Tax Liabilities")
frame6.grid(row=5, column=0, sticky="news", padx=20, pady=10)

result1 = Label(frame6)
result1.grid(row=0, column=1, sticky=W, pady=10)
result2 = Label(frame6)
result2.grid(row=1, column=1, sticky=W, pady=10)
result3 = Label(frame6)
result3.grid(row=2, column=1, sticky=W, pady=10)
result4 = Label(frame6)
result4.grid(row=3, column=1, sticky=W, pady=10)
result5 = Label(frame6)
result5.grid(row=4, column=1, sticky=W, pady=10)

content.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

window.mainloop()