def get_employee_info():

    #Initialization
    hdmf_contribution = 100

    # Input employee's name and department
    company_name = input("Enter company's name:")
    department = input("Enter the employee's department: ")
    employee_code = input ("Enter employee's code: ")
    employee_name = input("Enter the employee's name: ")
    salary_date_cutoff = input("Enter salary date cut-off: ")

   # Input rate per hour, working hours per day, days per week, and weeks per month
    rate_per_hour = float(input("Enter the rate per hour: "))
    hours_per_payday = float(input("Enter the number of hours per payday: "))
    hours_overtime = float(input("Enter the number of hours overtime: "))
    honorarium = float(input("Enter the amount of honorarium: "))

    # Input number of hours absent and tardy
    hours_absent = float(input("Enter the number of hours absent: "))
    hours_tardy = float(input("Enter the number of hours tardy: "))

    # Compute Basic Pay, Overtime pay and honorarium Pay
    basic_pay = rate_per_hour*hours_per_payday
    overtime_pay = rate_per_hour*hours_overtime

    #Compute for absence and tardiness
    absence = rate_per_hour*hours_absent
    tardy = rate_per_hour*hours_tardy
    # Compute Gross Earnings
    gross_earnings = basic_pay+overtime_pay+honorarium

    # Determine SSS Contribution
    if gross_earnings <= 4249.99:
        sss_contribution = 180.00
    elif 4250 <= gross_earnings <=4749.99:
        sss_contribution = 202.50
    elif 4750 <= gross_earnings <= 5249.99:
        sss_contribution = 225.00
    elif 5250 <= gross_earnings <= 5749.99:
        sss_contribution = 247.50
    elif 5750 <= gross_earnings <= 6249.99:
        sss_contribution = 270.00
    elif 6250 <= gross_earnings <= 6749.99:
        sss_contribution = 292.50
    elif 6750 <= gross_earnings <= 7249.99:
        sss_contribution = 315.00
    elif 7250 <= gross_earnings <= 7749.99:
        sss_contribution = 337.50
    elif 7750 <= gross_earnings <= 8249.99:
        sss_contribution = 360.00
    elif 8250 <= gross_earnings <= 8749.99:
        sss_contribution = 382.50
    elif 8750 <= gross_earnings <= 9249.99:
        sss_contribution = 405.00
    elif 9250 <= gross_earnings <= 9749.99:
        sss_contribution = 427.50
    elif 9750 <= gross_earnings <= 10249.99:
        sss_contribution = 450.00
    elif 10250 <= gross_earnings <= 10749.99:
        sss_contribution = 472.50
    elif 10750 <= gross_earnings <= 11249.99:
        sss_contribution = 495.00
    elif 11250 <= gross_earnings <= 11749.99:
        sss_contribution = 517.50
    elif 11750 <= gross_earnings <= 12249.99:
        sss_contribution = 540.00
    elif 12250 <= gross_earnings <= 12749.99:
        sss_contribution = 562.50
    elif 12750 <= gross_earnings <= 13249.99:
        sss_contribution = 585.00
    elif 13250 <= gross_earnings <= 13749.99:
        sss_contribution = 607.50
    elif 13750 <= gross_earnings <= 14249.99:
        sss_contribution = 630.00
    elif 14250 <= gross_earnings <= 14749.99:
        sss_contribution = 652.50
    elif 14750 <= gross_earnings <= 15249.99:
        sss_contribution = 675.00
    elif 15250 <= gross_earnings <= 15749.99:
        sss_contribution = 697.50
    elif 15750 <= gross_earnings <= 16249.99:
        sss_contribution = 720.00
    elif 16250 <= gross_earnings <= 16749.99:
        sss_contribution = 742.50
    elif 16750 <= gross_earnings <= 17249.99:
        sss_contribution = 765.00
    elif 17250 <= gross_earnings <= 17749.99:
        sss_contribution = 787.50
    elif 17750 <= gross_earnings <= 18249.99:
        sss_contribution = 810.00
    elif 18250 <= gross_earnings <= 18749.99:
        sss_contribution = 832.50
    elif 18750 <= gross_earnings <= 19249.99:
        sss_contribution = 855.00
    elif 19250 <= gross_earnings <= 19749.99:
        sss_contribution = 877.50
    elif 19750 <= gross_earnings <= 20249.99:
        sss_contribution = 900.00
    elif 20250 <= gross_earnings <= 20749.99:
        sss_contribution = 900.00
    elif 20750 <= gross_earnings <= 21249.99:
        sss_contribution = 900.00
    elif 21250 <= gross_earnings <= 21749.99:
        sss_contribution = 900.00
    elif 21750 <= gross_earnings <= 22249.99:
        sss_contribution = 900.00
    elif 22250 <= gross_earnings <= 22749.99:
        sss_contribution = 900.00
    elif 22750 <= gross_earnings <= 23249.99:
        sss_contribution = 900.00
    elif 23250 <= gross_earnings <= 23749.99:
        sss_contribution = 900.00
    elif 23750 <= gross_earnings <= 24249.99:
        sss_contribution = 900.00
    elif 24250 <= gross_earnings <= 24749.99:
        sss_contribution = 900.00
    elif 24750 <= gross_earnings <= 25249.99:
        sss_contribution = 900.00
    elif 25250 <= gross_earnings <= 25749.99:
        sss_contribution = 900.00
    elif 25750 <= gross_earnings <= 26249.99:
        sss_contribution = 900.00
    elif 26250 <= gross_earnings <= 26749.99:
        sss_contribution = 900.00
    elif 26750 <= gross_earnings <= 27249.99:
        sss_contribution = 900.00
    elif 27250 <= gross_earnings <= 27749.99:
        sss_contribution = 900.00
    elif 27750 <= gross_earnings <= 28249.99:
        sss_contribution = 900.00
    elif 28250 <= gross_earnings <= 28749.99:
        sss_contribution = 900.00
    elif 28750 <= gross_earnings <= 29249.99:
        sss_contribution = 900.00
    elif 29250 <= gross_earnings <= 29749.99:
        sss_contribution = 900.00
    elif 29750 <= gross_earnings <= 5249.99:
        sss_contribution = 900.00
    else:
        sss_contribution = 900.00


    # Determine Philhealth Contribution
    if gross_earnings <=9999.99:
        philhealth_contribution= 0
    elif gross_earnings == 10000.00 :
        philhealth_contribution = 500
    elif 10000.01<= gross_earnings <= 99999.99:
        philhealth_contribution = gross_earnings*0.05
    else:
        philhealth_contribution = 5000

    # Determine Withholding tax
    if gross_earnings <= 20832.99:
        withholding_tax = 0.00
    elif 20833.00 <= gross_earnings <= 33332.99:
        withholding_tax = 0.00 + (0.15*(gross_earnings-20833))
    elif 33333.00 <= gross_earnings <= 66666.99:
        withholding_tax = 1875.00+(0.20*(gross_earnings-33333))
    elif 66667.00 <= gross_earnings <= 166666.99:
        withholding_tax = 8541.80+(0.25*(gross_earnings-66667))
    elif 166667 <= gross_earnings <= 666666.99:
        withholding_tax = 33541.80 + (0.30*(gross_earnings-166667))
    else:
        withholding_tax = 183541.80 + (0.35*(gross_earnings-666667))

    # Compute total deductions
    total_deduction = hdmf_contribution + withholding_tax + sss_contribution + philhealth_contribution + absence + tardy

    # Compute net income
    net_pay = gross_earnings - total_deduction

    # Display employee's information and computed values
    print("\nCompany Name:", company_name)
    print("Employee Code:", employee_code)
    print("Employee Name:", employee_name)
    print("Department:", department)
    print("Cut-Off:", salary_date_cutoff)
    print("Pay Period: ", salary_date_cutoff)
    print("Basic Pay: ",basic_pay)
    print("Overtime: ", overtime_pay)
    print("Absences:", absence)
    print("Honorarium:", honorarium)
    print("Tardiness:", tardy)
    print("Withholding Tax: ", round(withholding_tax, 2))
    print("SSS Contribution: ", round(sss_contribution, 2))
    print("HDMF Contribution: ", round(hdmf_contribution, 2))
    print("PhilHealth Contribution: ", round(philhealth_contribution, 2))
    print("Total Deduction: ", round(total_deduction, 2))
    print("Gross Earnings: ", round(gross_earnings, 2))
    print("Net Pay: ", round(net_pay, 2))

get_employee_info()
