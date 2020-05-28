
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
    total = sum(student['marks'])
    number = len(student['marks'])
    if number == 0:
        return 0
    return total / number

