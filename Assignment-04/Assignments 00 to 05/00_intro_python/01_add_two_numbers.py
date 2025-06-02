try:
    num1:str = input("Enter the first number: ")
    num2:str = input("Enter the second number: ")

    if not num1 or not num2:
       raise ValueError("\nInput can not be empty.")
    
    if not num1.isdigit() or not num2.isdigit():
        raise ValueError("\nValue must be numeric.")

    total = num1 + num2

    print(f"Before convert to int, the total is: {total}")

    def add_number(x,y) ->int:
            add = int(x) + int(y)
            return(f"After convert to int, the total is: {add}")


    print(add_number(num1,num2))

except Exception as e:
      print(e)