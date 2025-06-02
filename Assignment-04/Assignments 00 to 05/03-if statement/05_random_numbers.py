
import random

def random_number():

    numbers = [str(random.randint(1,100)) for _ in range(10)]

    number = ",".join(numbers)

    print(number)

random_number()