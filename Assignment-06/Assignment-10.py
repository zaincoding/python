

class Dog:

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Dog Name {self.name} & it's breed {self.breed}")


dog = Dog('Tomy','German Shepherd')

dog.bark()
