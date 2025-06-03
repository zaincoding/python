

class Multiplyer:
    def __init__(self,factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
    

multi = Multiplyer(3)

print(multi(5))