
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator."
    
    cls.greet = greet

    return cls

@add_greeting
class Person:
    def __init__(self):
        pass

p = Person()

print(p.greet())

