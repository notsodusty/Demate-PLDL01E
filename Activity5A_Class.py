import Activity5_Class  # import the Activity5_Class module

def main():
    # call the classes and a method from the Activity5_Class module
    student = Activity5_Class.StudentInfo()
    student.get_subjects()
    assessment = Activity5_Class.Assessment(student)

    # call the display function
    display_student_info(student)
    display_subjects(student)
    display_assessment_fees(assessment, student)

def display_student_info(student):
    # display the student information
    print(f'''
    Student Name: {student.student_name}
    Course: {student.student_course}
    Student Number: {student.student_number}
    Academic Year: {student.academic_year}
    Date Printed: {student.date_printed}

    **************************
    ''')

def display_subjects(student):
    for section, subject, units in student.get_subjects_info():
        print(f'\tSection: {section}, Subject: {subject}, Units: {units}')
    print(f'\tTotal Units: {student.total_units()}')

def display_assessment_fees(assessment, student):
    # display the assessment fees
    print(f'''
    ***************************\n
        ASSESSMENT OF FEES
    Tuition Fee: P {assessment.get_tuition_fee():.2f}
    ADU Chronicle: P {assessment.adu_chronicle:.2f}
    Athletic: P {assessment.athletic:.2f}
    Audio Visual Library: P {assessment.audio_visual:.2f}
    AUSG: P {assessment.ausg:.2f}
    Cultural Fee: P {assessment.cultural_fee:.2f}
    Energy Cost, AirCon Classroom: P {assessment.energy_cost_aircon_classroom:.2f}
    Guidance: P {assessment.guidance:.2f}
    Insurance Fee: P {assessment.insurance:.2f}
    Learning Management System: P {assessment.learning_management_system:.2f}
    Library Fee: P {assessment.library_fee:.2f}
    Medical and Dental: P {assessment.medical_and_dental:.2f}
    Registration: P {assessment.registration:.2f}
    RSO: P {assessment.rso:.2f}
    Student Activities Fee: P {assessment.student_activities_fee:.2f}
    Student Nurturance Fee: P {assessment.student_nurturance_fee:.2f}
    Technology Fee: P {assessment.technology_fee:.2f}
    Test Papers: P {assessment.test_papers:.2f}
    
    **************************

    Assessment Amount: P {assessment.get_total_assessment_amount():.2f}
    Downpayment: P {assessment.downpayment:.2f}

    **************************

    Total Due: P {assessment.get_total_due():.2f}

    **************************

    Prelims: P {assessment.get_total_due() / 3:.2f}
    Midterms: P {assessment.get_total_due() / 3:.2f}
    Finals: P {assessment.get_total_due() / 3:.2f}
    
    Date Printed: {student.date_printed}
    ''')

if __name__ == '__main__':
    main()
