

def modulus(a,b):
    c = a%b

    return (f"\nModulus of {a}/{b} is = {c}")


if __name__ == '__main__':
   
 try:
    a = input("Enter first number: ").strip()
    b = input("Enter second number: ").strip()

    if not b or not b:
     raise ValueError ("One or more required fields are missing.Please enter all necessary input.")

    if not a.isdigit() or b.isdigit():
      raise ValueError("Only numeric data allowed.Please don't enter characters")
    
    a = int(a)
    b = int(b)
    if a ==0 or b ==0:
     raise ValueError(f"Division by zero is not allowed.")




    print(modulus(a,b))
 
 except ValueError as e:
    print("\nError: " + str(e))