

class Person:
    def __init__(self,name):

        self.name = name

class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


obj1 = Teacher('Mr.Zain', 'Python')


print("Name:" + " " + obj1.name +"\n "  +"Subject:" + " "+ obj1.subject)
