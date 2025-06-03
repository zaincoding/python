

class Employee:

    def __init__(self,name,salary,ss):
        self.name = name
        self._salary = salary
        self.__ss = ss



employee = Employee('zain','$500','abc')

print(employee.name)
print(employee._salary)
print(employee.__ss)

