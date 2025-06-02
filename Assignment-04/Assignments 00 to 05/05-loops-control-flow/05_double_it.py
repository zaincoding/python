
def double_number(curr_value):

    curr_value = curr_value*2

    print(curr_value)

def get_curr_value():

    user_input = input("Enter Value to double it.(or press enteter to stop): ")

    if user_input == "":
        return None
    
    try:
        user_input = int(user_input)
        return user_input

    except ValueError:
        print("ValueError: Please enter (numeric value only).")

def main():
    while True:
       curr_value = get_curr_value()
       if curr_value is None:
           break
       
       if curr_value<1 or curr_value > 100:
           print("Value should be b/w 1 and 100.")
       
       if curr_value <= 100:
           double_number(curr_value)

if __name__ == '__main__':
    main()
           
