# SalaryTaxCalculator

Hong Kong Salary Tax Calculator for 2023/24

Three versions are designed:

1. No UI version, run it on terminal by typing “python terminal/app.py”

2. With UI version by Streamlit, an open source app framework in Python, run it on terminal by typing “streamlit run streamlit_ui.py”

3. With UI version by Tkinter, the standard Python GUI toolkit, run it on terminal by typing “python tkinter_ui.py”

Note: In order to reduce computational complexity, two assumptions are made.

1. For Single / Separated / Divorced / Widowed, tax payable is calculated by the lowest of progressive tax and standard tax.

2. For Married, tax payable is ONLY calculated under Joint Assessment Scheme in which progressive tax is adopted.

All the details of allowances, deductions and tax rate table are available in the “pam61e.pdf” file.
