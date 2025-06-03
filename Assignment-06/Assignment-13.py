
import gc

class Engine:
    def start(self):
        return "Engine Started"
    
class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
      return  self.engine.start()
    

car = Car()

del car

gc.collect()

try:
   print(car.start())

except Exception as e:
    print("Error:", e)

