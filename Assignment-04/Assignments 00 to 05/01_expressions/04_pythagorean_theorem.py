
# hypotenuse^2 = base^2 + Perpendicular^2
#fomula  h**2 = b**2 + p**2

import math

def hyp_length(b,p):

    h = math.sqrt(b**2 + p**2)

    print(f"Base = {b}")
    print(f"Height = {p}")

    return(f"Hypotenuse = {h:.2f}")

    
if __name__ == '__main__':

  try:
    b = input("Enter base value: ").strip()
    p = input("Enter height value: ").strip()

    if not b or not p:
     raise ValueError ("One or more required fields are missing.Please enter all necessary input.")

    b = int(b)
    p = int(p)
    if b == 0 or p == 0:
        raise ValueError("Division by zero is not allowed.")

    print(hyp_length(b,p))

  except ValueError as e:
   print("\nError: " +str(e))

