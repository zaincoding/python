

class InvalidAgeError(Exception):

    pass
def check_age(age):

    if age < 18 :
        raise InvalidAgeError("You are not eligible for vote.")
    
    else:
            print("You are eligible.")
        
try:
    user_age = int(input("Enter your age."))
    check_age(user_age)
except InvalidAgeError as e:
        print("Access denied", e)

except ValueError:
        print("Please enter a valid value.")



