
# Function to calculate the final grade and equivalent grade
def get_student_info():
    # Input student's name
    student_name = input("Enter the student's name: ")

    # Input ratings for quizzes, research/assignment, project, and final exam
    final_quizzes = float(input("Enter the final quizzes rating (out of 100): "))
    final_research_assignment = float(input("Enter the final research/assignment rating (out of 100): "))
    final_project = float(input("Enter the final project rating (out of 100): "))
    final_exam = float(input("Enter the final exam rating (out of 100): "))

    # Calculate the final grade using the formula
    final_grade = (0.30 * final_quizzes) + (0.10 * final_research_assignment) + (0.40 * final_exam) + (
                0.20 * final_project)

    # Determine the equivalent grade based on the final grade
    if 98 <= final_grade <= 100:
        equivalent_grade = 4.00
    elif 95 <= final_grade <= 97:
        equivalent_grade = 3.75
    elif 92 <= final_grade <= 94:
        equivalent_grade = 3.50
    elif 89 <= final_grade <= 91:
        equivalent_grade = 3.25
    elif 86 <= final_grade <= 88:
        equivalent_grade = 3.00
    elif 83 <= final_grade <= 85:
        equivalent_grade = 2.75
    elif 80 <= final_grade <= 82:
        equivalent_grade = 2.50
    elif 77 <= final_grade <= 79:
        equivalent_grade = 2.25
    elif 74 <= final_grade <= 76:
        equivalent_grade = 2.00
    elif 71 <= final_grade <= 73:
        equivalent_grade = 1.75
    elif 68 <= final_grade <= 70:
        equivalent_grade = 1.50
    elif 64 <= final_grade <= 67:
        equivalent_grade = 1.25
    elif 60 <= final_grade <= 63:
        equivalent_grade = 1.00
    else:
        equivalent_grade = "Below the provided grading scale"

    # Display student's information and grades
    print("\nStudent Name:", student_name)
    print("Final Quizzes Rating:", final_quizzes)
    print("Final Research/Assignment Rating:", final_research_assignment)
    print("Final Project Rating:", final_project)
    print("Final Exam Rating:", final_exam)

    # Display the final grade and equivalent grade
    print("Final Grade:", round(final_grade, 2))
    print("Equivalent Grade:", equivalent_grade)


# Run the program
get_student_info()