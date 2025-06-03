

class Product:
    def __init__(self,price):
        self.price = price

    @property
    def price(self):
        print("Printing price.")
        return self._price

    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Value should not be negative.")
        print("setting value.")
        self._price =value

    @price.deleter
    def price(self):
        print("Value is deleting")
        del self._price

p = Product(5)

print(p.price)

del p.price