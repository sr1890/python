
student_list = []

def create_student():
    name = input("Enter the name of the student: ")
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data


def add_marks(student, marks):
    student['marks'].append(marks)

def calculate_average_marks(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number

def print_student_details(student)
    print ("{}, average marks {}.".format(student['name'],
                                          calculate_average_marks(student)))

def print_student_list(students):
    for student in students:
        print_student_details (student)
