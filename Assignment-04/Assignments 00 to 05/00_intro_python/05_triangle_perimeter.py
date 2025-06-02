
def square(a):
    return "{:.2f}".format(a*a)

while True:
    try:
        input_a = input("Enter a number to square: ")
        if not input_a.strip():
            raise ValueError("An empty input.")
        
        try:

          user_input = float(input_a)
        except ValueError:
            raise ValueError("Invalid input.Please provide numeric value only.")
        
        print(square(user_input))
        break

    except ValueError as e:
        print("Error:", e)