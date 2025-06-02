
import random
def guess_number(a):

    random_number = random.randint(1,a)

    guess =0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and {}: ".format(a)))

        if guess > random_number:
            print("\nSorry the number is too high. Guess again.")
        elif guess < random_number:
            print("\nSorry the number is too low. Guess again.")
    
    print("\nCongrats you guessed the number {} correctly.".format(random_number))
        

guess_number(10)