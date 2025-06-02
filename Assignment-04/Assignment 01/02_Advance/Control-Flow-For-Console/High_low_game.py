import random 


def guess_number():
    
    score = 0
    total_rounds = 5



    for i in range(1,total_rounds  +1):
        user_number = random.randint(1,100)
        computer_number = random.randint(1,100)

        print(f"Your Number is, {user_number}")
        user_input = input("Guess your number is higher or lower than the computer: ")
        if user_number >= computer_number:
                if user_input == "higher":
                    score +=1
                    print(f"round: {i}")
                    print(f"Thats correct the computer number was {computer_number} ")
                    print(f"Your score: {score}")
                else:
                    print(f"round: {i}")
                    print(f"Aww, that's incorrect. The computer's number was {computer_number} ")
                    print(f"Your score: {score}")

        elif user_number <= computer_number:
                if user_input == "lower":
                    score +=1
                    print(f"round: {i}")
                    print(f"That's correct. The computer's number was {computer_number} ")
                    print(f"Your score: {score}")

                else:
                    print(f"round: {i}")
                    print(f"Aww, that's incorrect. The computer's number was {computer_number} ")
                    print(f"Your score: {score}")

    print(f"\nTotal score: {score}")
guess_number()

