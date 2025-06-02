import random

def random_num():

    for i in range(10):
            random_num = random.randint(1, 100)
            print(random_num, end=' ')


random_num()