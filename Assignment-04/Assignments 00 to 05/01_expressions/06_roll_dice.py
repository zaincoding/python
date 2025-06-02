
import random
def roll_dice():

    input(f"Press enter to roll the die...")
    a = random.randint(1,6)
    print(f"Roller-1 rolled: {a}\n")

    input(f"Press enter to roll the die...")
    b = random.randint(1,6)
    print(f"Roller-2 rolled: {b}\n")

    print(f"Total: {a + b}")    
   
if __name__ == '__main__':
  (roll_dice())  


    