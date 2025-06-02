
def fruits_name():

    fruits = {"Apple": '1', "Mango": 2}

    count = 0
    for fruit in fruits:
     price = fruits[fruit]

     while True:
        user_input = input(f"How many \"{fruit}\" do you want to buy? ")
        if user_input == "":
            return None
        

        try:
            user_input = int(user_input)
            price = int(price)


            total_price = user_input * price

            count +=total_price
            break
        except ValueError:
            print("Please enter only a numeric value.")
            
        
    return (f"Total price: ${count}")
    
             

print(fruits_name())        

    


    


