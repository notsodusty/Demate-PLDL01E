import MidtermExam #import Previous file

def main():
    #Call for Classes
    service_info = MidtermExam.ServiceInfo()
    metering_info = MidtermExam.MeteringInfo()
    bill_payment_history = MidtermExam.BillPaymentHistory()
    billing_summary = MidtermExam.BillingSummary(metering_info)
    billing_summary.get_basic_charge()
    billing_summary.get_environmental_charge()
    billing_summary.get_total_charges_before_tax()
    billing_summary.get_government_taxes()
    billing_summary.get_total_amount_due()
    billing_summary.get_current_charges()

   #Call for Display Functions
    display_service_info(service_info)
    display_metering_info(metering_info)
    display_bill_payment_history(bill_payment_history)
    display_billing_summary(billing_summary)


def display_service_info(service_info):
    #DISPLAY FOR SERVICE INFORMATION IN OUR FIRST CLASS
    print(f'''
                                                            Maynilad Water Services, Inc.
                                                            8390 DR A SANTOS AVE BF HOMES
                                                            PARANAQUE CITY
                                                            VAT Reg TIN 005-393-442-0000
                                                            SPM No.:
                                                            Machine SN:
    
                           SERVICE INFORMATION
       Contract Account No.: {service_info.contract_account_no}
       Account Name: {service_info.account_name}
       Service Address : {service_info.house_number} {service_info.street}  {service_info.barangay}  {service_info.municipality} {service_info.city}
       TIN: {service_info.tin}
       Rate Class: {service_info.rate_class}
       Business Area : {service_info.business_area}
       -----------------------------------------------------------------------
       ''')

def display_metering_info(metering_info):
    # DISPLAY FOR METERING INFORMATION IN OUR SECOND CLASS
    print(f'''
                           METERING INFORMATION
        Meter No.                           MRU No.                           Seq No.
        {metering_info.meter_number}                   {metering_info.mru_number}                   {metering_info.seq_number}
        Reading Date: {metering_info.reading_date}
        Present Reading: {metering_info.present_reading}
        Previous Reading: {metering_info.previous_reading}
        Consumption: {metering_info.consumption}
           
        Previous 3 Months Consumption
        ---------------------------------------------------------------------
        ''')
def display_bill_payment_history(bill_payment_history):
    # DISPLAY FOR BILL PAYMENT HISTORY IN OUR THIRD CLASS
    print(f'''
                           BILL & PAYMENT HISTORY
        Desc          Total Amount              OR#            Date
        
        Description:   {bill_payment_history.description}
        ------------------------------------------------------------------
          ''')
def display_billing_summary(billing_summary):
    # DISPLAY FOR BILLING SUMMARY IN OUR FOURTH CLASS
    print(f'''
                            BILLING SUMMARY
         BILLING PERIOD: {billing_summary.billing_period} TO {billing_summary.end_billing_period}
         Current Charges: {billing_summary.current_charges:.2f}
                  
                  Basic Charge                                    {billing_summary.basic_charge:.2f}
                  Environmental Charges (20% of Basic Charge)     {billing_summary.environmental_charge:.2f}
                  Maintenance Service Charge (MSC)                {billing_summary.msc:.2f}
                  Total Current Charges Before Taxes              {billing_summary.total_charges_before_tax:.2f}
                  Government Taxes                                {billing_summary.government_taxes:.2f}
             ------------------------------------------------------------------------------------------
             TOTAL AMOUNT DUE:                                    PHP{billing_summary.total_amount_due:.2f}
             PAYMENT DUE DATE:                                    {billing_summary.payment_due_date}     
                
         ''')
main()