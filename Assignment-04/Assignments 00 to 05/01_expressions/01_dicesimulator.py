import random

def roll_dice():
    die1:int = random.randint(1,6)
    die2:int = random.randint(1,6)
    return die1, die2

print("Wellcome to the Diece Roller!")
print("Press enter to Dice the Roller\n")

input("Roller-1: press enter to roll ")
d1,d2= roll_dice()
print(f"Rolled Die 1 = {d1}, D2 = {d2}\n")

input("Roll-2: Press enter to roll ")
d1,d2 = roll_dice()
print(f"Rolled Die 1 = {d1}, D2 ={d2}")

input("Roll-3: Press enter to roll ")
d1,d2 = roll_dice()
print(f"Rolled Die 1 = {d1}, D2 ={d2}")