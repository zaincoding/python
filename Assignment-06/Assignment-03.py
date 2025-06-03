

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"My car brand is {self.brand}.")


car = Car('Corolla')

print(f"Brand: {car.brand}")

car.start()


