
class A:

    def show(self):
        print("Hello World")

class B(A):

    def show(self):
        print("Welcome to our program.")

class C(A):

    def show(self):
        print("Welcome to the class.")

class D(B , C):
    pass

d = D()


d.show()
print(D.__mro__)