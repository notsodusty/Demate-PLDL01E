class CustomerInfo: # Class for Customer Information
    def __init__(self): # initialize the customer info
        self.customer_name = input("Enter customer name: ")
        self.house_number = input("Enter house number: ")
        self.street = input("Enter street:")
        self.barangay = input("Enter barangay: ")
        self.municipality = input("Enter municipality: ")
        self.city = input("Enter city: ")
        self.customer_account_number = input("Enter customer account number: ")

class ElectricBill: # Class for Electric Bill
    def __init__(self):# initialize Electric Bill
        self.balance = int(input("Enter balance from previous billing: "))
        self.current_amount_due = input("Enter amount due: ")
        self.current_due_date = input("Enter due date: ")
        self.total_amount_due = 0

#solving for total amount due
    def get_total_amount_due(self):
        self.total_amount_due = self.balance + self.current_amount_due
        return self.total_amount_due


class ServiceInfo: # Class for Service Info
    def __init__(self, customer):# initialize the service info
        self.customer = customer
        self.service_id_number = customer.customer_account_number
        self.rate = input("Enter Residential or Business: ")
        self.contact = customer.customer_name
        self.contact_house_number = customer.house_number
        self.contact_street = customer.street
        self.contact_barangay = customer.barangay
        self.contact_municipality = customer.municipality
        self.contact_city = customer.city


class BillingInfo: # Class for Billing Info

    def __init__(self, bill): # initialize the billing info
        self.bill = bill
        self.bill_date = input("Enter bill date: ")
        self.meter_reading_date = input("Enter meter reading date: ")
        self.bill_period = input("Enter bill period: ")
        self.due_date = bill.current_due_date
        self.total_kwh = int(input("Enter total KWH: "))
        self.rate_per_kwh = int(input("Enter rate per KWH:"))
        self.total_current_amount = bill.total_amount_due
        self.next_meter_reading = input("Enter next meter reading: ")
        self.amount_due = 0

# solving for amount due
    def get_amount_due(self):
        self.amount_due = self.rate_per_kwh * self.total_kwh
        return self.amount_due


class BillComputationSummary: #Class for Bill Computation Summary
    def __init__(self, bill): # initialize the bill computation summary
        self.billing = bill
        self.remaining_balance = bill.balance
        self.generation = input("Enter Generation fee: ")
        self.transmission = input("Enter Transmission fee: ")
        self.system_loss = input("Enter System loss: ")
        self.distribution = input("Enter Distribution fee:")
        self.subsidies = input("Enter subsidies fee: ")
        self.government_taxes = input("Enter Government Taxes: ")
        self.universal_charges = input("Enter Universal charges")
        self.fit_all = input("Enter FiT-All (Renewable) fee: ")
        self.applied_credits = input("Enter applied credits: ")
        self.other_charges = input("Enter other charges: ")
        self.installment_due = input("Enter installment due: ")

