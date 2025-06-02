import random

def guess_number_game(max_number: int):
    print("🎮 Welcome to the 'Guess the Number' Game!")
    print(f"🤔 Think of a number between 1 and {max_number}. I will try to guess it.")
    print("🗣️ Respond with:")
    print("    H → if my guess is too High")
    print("    L → if my guess is too Low")
    print("    C → if my guess is Correct")

    low = 1
    high = max_number
    feedback = ''

    while feedback != 'c':
        if low > high:
            print("🚫 Seems like there was inconsistent feedback. Let's restart!")
            return

        guess = random.randint(low, high)
        feedback = input(f"\nIs {guess} too high (H), too low (L), or correct (C)? ").strip().lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"\n🎉 Yay! I guessed your number {guess} correctly!")
        else:
            print("⚠️ Invalid input. Please enter only H, L, or C.")

# Run the game with a range of 1 to 10
guess_number_game(10)
