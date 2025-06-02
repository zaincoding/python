

def  Joke(user_input):

    if "joke" in user_input:
       return ("Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk."
        " The programmer asks why and Sophia replies: 'because they had eggs'")
    elif user_input == "":
        return("Missing input field. Please enter a value.")
    else:
        return("Sorry I only tell jokes")
    
user_input = input("What do you want to listen?: ")

print(Joke(user_input))