import MidtermQ1

def main():
    # Call the Classes
    customer = MidtermQ1.CustomerInfo()
    electric_bill = MidtermQ1.ElectricBill()
    service_info = MidtermQ1.ServiceInfo(customer)
    billing_info = MidtermQ1.BillingInfo(electric_bill)
    bill_summary = MidtermQ1.BillComputationSummary(electric_bill)
  # Call the Display function
    display_customer_info(customer)
    display_electric_bill(electric_bill)
    display_service_info(service_info)
    display_billing_info(billing_info)
    display_bill_summary(bill_summary)


def display_customer_info(customer):
    # display customer info
    print(f'''
    {customer.customer_name}
    {customer.house_number}
    {customer.street}
    {customer.barangay}
    {customer.municipality}
    {customer.city}
    {customer.customer_account_number}

     **************************
    ''')

def display_electric_bill(electric_bill):

    # Display electric bill info
    if electric_bill.balance == 0:
        print("Thank You")
    else:
        print("Please pay remaining balance.")

    print(f'''
    {electric_bill.current_amount_due}
    {electric_bill.current_due_date}
    {electric_bill.total_amount_due}


    **************************
    ''')
def display_service_info(service_info):
    # Display service info
    print(f'''
    Service ID Number: {service_info.service_id_number}
    Rate: {service_info.rate}
    Contact in the name of : {service_info.contact}
    Service Address: {service_info.contact_house_number}
    {service_info.contact_street} {service_info.contact_barangay}
    {service_info.contact_city} {service_info.contact_municipality}
    **************************
    ''')

def display_billing_info(billing_info):
    # Display Billing Info
    print(f'''
    Bill Date: {billing_info.bill_date}
    Meter Reading Date: {billing_info.meter_reading_date}
    Bill Period: {billing_info.bill_period}
    Due Date: {billing_info.due_date}
    Total KWH: {billing_info.total_kwh}
    Total Current Amount: {billing_info.total_current_amount}
    Next Meter Reading: {billing_info.next_meter_reading}
    Amount Due: {billing_info.amount_due}
    **************************
    ''')

def display_bill_summary(bill_summary):
    # Display Bill Summary
    print(f'''
    Generation: {bill_summary.generation}
    Transmission: {bill_summary.transmission}
    System Loss: {bill_summary.system_loss}
    Distribution (Meralco): {bill_summary.distribution}
    Subsidies: {bill_summary.subsidies}
    Government Taxes: {bill_summary.government_taxes}
    Universal Charges: {bill_summary.universal_charges}1
    FiT-All (Renewable): {bill_summary.fit_all}
    Applied Credits: {bill_summary.applied_credits}
    Other Charges: {bill_summary.other_charges}
    Installment Dues: {bill_summary.installment_due}
     **************************
    ''')

main()