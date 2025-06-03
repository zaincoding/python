
class Counter:
    count = 0

    @classmethod
    def create_object(cls):
        cls.count +=1
        return cls
    
    @classmethod
    def display_object(cls):
        print(f"Total object created {cls.count}")


obj1 = Counter.create_object()
obj2 = Counter.create_object()
obj3 = Counter.create_object()

Counter.display_object()