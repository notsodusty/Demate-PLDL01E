class ServiceInfo: # Class for Service Info
    def __init__(self): # initialize the Service info
        #Input Service Information
        self.contract_account_no = input("Enter Contract Account No. :")
        self.account_name = input("Enter account name: ")
        self.house_number = input("Enter house number: ")
        self.street = input("Enter street:")
        self.barangay = input("Enter barangay: ")
        self.municipality = input("Enter municipality: ")
        self.city = input("Enter city: ")
        self.tin = input("Enter TIN ID No. :")
        self.rate_class = input("Residential or Business: ")
        self.business_area = input("Enter Business Area: ")

class MeteringInfo: #Class for Metering Information
    def __init__(self): #Initialization for Metering Info
    #Input for Meter Info
       self.meter_number =  input("Enter Meter No. :")
       self.mru_number = input("Enter MRU No. : ")
       self.seq_number = input("Enter Seq No. : ")
       self.reading_date = input("Enter Reading Date: ")
       self.present_reading = input("Enter Present Reading: ")
       self.previous_reading = input("Enter Previous Reading: ")
       self.consumption = float(input("Enter Consumption (cu.m) : "))

class BillPaymentHistory:#Class for Bill Payment History
    def __init__(self): #Initialization for BillPayment History

       self.description ="WB-Waterbill, GD-Guarantee Deposit, MISC-Reopening Fee, Connection Fee, Metering Charge"

class BillingSummary: #Class for Billing Summary
    def __init__(self, bill): #Initialization for Billing Summary
        self.basic_charge = 0
        self.environmental_charge = 0
        self.total_charges_before_tax = 0
        self.government_taxes = 0
        self.total_amount_due = 0
        self.current_charges = 0
        self.bill_consumption = bill.consumption
        self.billing_period = input("Enter Billing Period: ")
        self.end_billing_period = bill.reading_date
        self.rate_cu_m = 23.52
        self.msc = float(input("Enter Maintenance Service Charge: "))
        self.payment_due_date = input("Enter Payment Due Date: ")


    def get_basic_charge(self): #define on getting basic charge
        #Solve for basic charge
        self.basic_charge = self.bill_consumption * self.rate_cu_m
        return self.basic_charge

    def get_environmental_charge(self): #define on getting environmental charge
        #Solve for Environmental Charge
        self.environmental_charge = 0.20 * self.basic_charge
        return self.environmental_charge

    def get_total_charges_before_tax(self): #define on getting total charges before tax
        #Solve for Total Charges Before Tax
        self.total_charges_before_tax = self.basic_charge + self.environmental_charge + self.msc
        return self.total_charges_before_tax

    def get_government_taxes(self): #define on getting government taxes
        #Solve for Government Tax
        self.government_taxes = self.total_charges_before_tax * 0.025
        return self.government_taxes

    def get_total_amount_due(self): #define on getting total amount due
        #Solve for total amount due
        self.total_amount_due = self.total_charges_before_tax + self.government_taxes
        return self.total_amount_due

    def get_current_charges(self):
        #Equalization of current charges to total amount due
        self.current_charges = self.total_amount_due
        return self.current_charges



