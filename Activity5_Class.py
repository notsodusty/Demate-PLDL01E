class Student:
    def __init__(self, name, course, student_number, academic_year):
        self.name = name
        self.course = course
        self.student_number = student_number
        self.academic_year = academic_year

class Assessment:
    def __init__(self, sections):
        self.sections = sections
        self.tuition_fee_per_unit = 1551.00
        self.assessment_fees = {}

    def add_subject(self, section, subject, units):
        if section not in self.sections:
            self.sections[section] = []
        self.sections[section].append({'subject': subject, 'units': units})

    def compute_tuition_fee(self):
        total_units = sum(subject['units'] for section in self.sections.values() for subject in section)
        return total_units * self.tuition_fee_per_unit

    def compute_assessment_amount(self):
        tuition_fee = self.compute_tuition_fee()
        other_fees = sum(self.assessment_fees.values())
        return tuition_fee + other_fees

    def compute_total_due(self, downpayment):
        assessment_amount = self.compute_assessment_amount()
        return assessment_amount + downpayment

    def compute_payment_terms(self, total_due):
        return total_due / 3

def main():
    # Input student details
    name = input("Enter student name: ")
    course = input("Enter course: ")
    student_number = input("Enter student number: ")
    academic_year = input("Enter academic year: ")

    student = Student(name, course, student_number, academic_year)

    # Input current date
    current_date = input("Enter current date: ")
    print(f"Date Printed: {current_date}")

    # Input sections, subjects, and units
    sections = {}
    num_sections = int(input("Enter number of sections: "))
    for _ in range(num_sections):
        section = input("Enter section: ")
        num_subjects = int(input(f"Enter number of subjects for section {section}: "))
        for _ in range(num_subjects):
            subject = input("Enter subject: ")
            units = int(input(f"Enter units for subject {subject}: "))
            if section not in sections:
                sections[section] = []
            sections[section].append({'subject': subject, 'units': units})

    assessment = Assessment(sections)

    # Input assessment fees (excluding Tuition Fee Lecture)
    num_fees = int(input("Enter number of other assessment fees: "))
    for _ in range(num_fees):
        fee_name = input("Enter fee name: ")
        fee_amount = float(input(f"Enter amount for {fee_name}: "))
        assessment.assessment_fees[fee_name] = fee_amount

   # Compute Tuition Fee Lecture
    tuition_fee = assessment.compute_tuition_fee()
    print(f"Tuition Fee Lecture: P {tuition_fee:.2f}")

    # Compute Assessment Amount
    assessment_amount = assessment.compute_assessment_amount()
    print(f"Assessment Amount: P {assessment_amount:.2f}")

    # Input downpayment
    downpayment = float(input("Enter downpayment: "))

    # Compute Total Due
    total_due = assessment.compute_total_due(downpayment)
    print(f"Total Due: P {total_due:.2f}")

    # Compute payment terms
    payment_term = assessment.compute_payment_terms(total_due)
    print(f"Prelims: P {payment_term:.2f}")
    print(f"Midterms: P {payment_term:.2f}")
    print(f"Finals: P {payment_term:.2f}")

if __name__ == "__main__":
  main()