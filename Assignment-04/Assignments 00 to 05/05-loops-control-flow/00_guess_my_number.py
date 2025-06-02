
import random

def random_number(number):
    
    
         random_num = random.randint(1,99)

         if random_num == number:
                print(f"\nCongrate! You guess is right! The number was {random_num}.")
         elif  number < random_num :
                print(f"\nYour guess {number} is too low. The number was {random_num}")
         else:
              print(f"\nYour guess {number} is too high. The number was {random_num}")



def get_number():

    user_input = input("Enter guess number or(press enter to stop): ")

    if user_input == "":
        return None
    
    
    
    try:
        user_input = int(user_input)
        return user_input
    
    except ValueError:
        print("Invalid input: Please enter number only.")


def main():

    while True:
        number = get_number()

        if number is None:
            print("It's stopped.")
            break
        elif number< 1 or number >99:
            print("Please enter a number between 1 and 99.")
            continue
        
        random_number(number)

if __name__ == '__main__':
    main()





    