
def min_height(height: int) ->bool:

    if height >= 10:
        print("Your are tall enough to ride.")
        return True
    
    if height <= 10:
        print("You are not tall enought to ride")
        return False
    
def get_height():
    while True:
        user_input = input("Enter your height or (press enter to stop): ")
        if user_input == "":
            return None
        
        try:
            height = int(user_input)
            return height

        except ValueError:
            print("ValueError: Please enter a valid height.")
        
def main():
    while True:
        height = get_height()
        if height is None:
            break

        if min_height(height):
            print("\nBreaking because you are tall enoguh.")
            break

if __name__ == '__main__':
    main()
