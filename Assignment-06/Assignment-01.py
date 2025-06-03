

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}\n Marks: {self.marks}")


student_result = Student('Zain', '94%')

student_result.display()