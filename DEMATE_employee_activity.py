#Initialization of Values
net_income = 0
gross_income = 0
total_deduction = 0
name_of_employee = " "
department = " "
pag_ibig_contribution = 100

# Input employee's name and department
employee_name = str(input("Enter the employee's name: "))
department = str(input("Enter the employee's department: "))

# Input rate per hour, working hours per day, days per week, and weeks per month
rate_per_hour = float(input("Enter the rate per hour: "))
working_hours_per_day = float(input("Enter the number of working hours per day: "))
days_per_week = int(input("Enter the number of days per week: "))
weeks_per_month = int(input("Enter the number of weeks per month: "))

# Compute gross income
gross_income = rate_per_hour * working_hours_per_day * days_per_week * weeks_per_month

# Pag-IBIG Contribution
pagibig_contribution = 100.00

# Determine SSS and PhilHealth Contribution based on gross income
if gross_income <= 20000:
        sss_contribution = 125.75
        philhealth_contribution = 100.00
elif 20001 <= gross_income <= 50000:
        sss_contribution = 2200.50
        philhealth_contribution = 1200.00
elif 50001 <= gross_income <= 75000:
        sss_contribution = 4800.00
        philhealth_contribution = 6800.00
else:
        sss_contribution = 5800.00
        philhealth_contribution = 8800.00

# Compute total deductions
total_deduction = pagibig_contribution + sss_contribution + philhealth_contribution

# Compute net income
net_income = gross_income - total_deduction

# Display employee's information and computed values
print("\nEmployee Name:", employee_name)
print("Department:", department)
print("Gross Income: ", round(gross_income, 2))
print("Pag-IBIG Contribution: ", round(pagibig_contribution, 2))
print("SSS Contribution: ", round(sss_contribution, 2))
print("PhilHealth Contribution: ", round(philhealth_contribution, 2))
print("Total Deduction: ", round(total_deduction, 2))
print("Net Income: ", round(net_income, 2))

