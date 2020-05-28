
student_list = []

class Student:
    def __init__(self, name):
        self.name = "john"
        self.marks = []

    def average_mark(self):
        number = len(self.marks)
        if number == 0:
            return 0

        total = sum(self.marks)
        return total / number


def create_student():
    name = input("Enter the name of the student: ")
    student_data = Student(name)

    return student_data

def add_marks(student, marks):
    student.marks.append(marks)


def print_student_details(student):
    print ("{}, average marks {}.".format(student.name,
                                          student.average_mark()))

def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details (student)

def menu():
    selection = input ("Enter 'p' to print the student list, "
                       "'s' to add a new student,"
                       "'a' to add a new marks to student,"
                       " or 'q'  to quit.")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input ("Enter the student id to add marks to :"))
            student = student_list[student_id]
            new_marks = int(input("Enter the new marks to be added :"))
            add_marks(student, new_marks)

        selection = input("Enter 'p' to print the student list, "
                          "'s' to add a new student,"
                          "'a' to add a new marks to student,"
                          " or 'q'  to quit.")
menu()