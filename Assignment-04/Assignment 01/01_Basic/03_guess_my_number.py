
import random

def random_number(user_value, random_num) ->bool:

    if user_value == random_num:
        print(f"Congrats! The number was: {random_num}")
        return True
        

    elif user_value > random_num:
        print(f"Your guessed number is too high.")
        return False
    
    elif user_value < random_num:
        print(f"Your guessed number is too low")
        return False

def get_number():

    user_input = input("Enter a number: ")

    if user_input == "":
        return  "empty"
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        print("ValueError: Please enter numeric value only.")
        return "invalid"
    
def main():
    random_num = random.randint(1,99)
    while True:
        user_value = get_number()

        if user_value == 'empty':
            print("Missing input field. Please enter a value.")
            break
        if user_value == 'invalid':
            print("Invalid input value. Please enter number only. ")
            break
        if user_value< 1  or user_value>99:
            print("Provided value should be between 1 and 99")
            continue

        if random_number(user_value, random_num):
            break

if __name__ == '__main__':
   main()

