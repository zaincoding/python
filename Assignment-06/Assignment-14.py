

class Employee:

    def __init__(self,name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def __str__(self):
        return(f"Employee Name: {self.name}\n Employee ID: {self.emp_id}")


class Department:

    def __init__(self,dep_name,employee):
        self.dep_name = dep_name
        self.employee = employee

    def show_detail(self):
        print(f"Department: {self.dep_name}")
        print(f"Employee: {self.employee}")

emp = Employee('zain', 'id_123')

dep = Department('IT', emp)


del emp  

dep.show_detail() 


    

    

