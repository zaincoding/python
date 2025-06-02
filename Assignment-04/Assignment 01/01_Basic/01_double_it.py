

def double_number(a:int) ->int:

    return(a)*4

def get_input():
   
   user_input = input("Enter a value to duble it.")

   if user_input == "":
      return "empty"
   try:
      user_input = int(user_input)
      return user_input
   except ValueError:
      return "invalid"
   
def main():
   while True:
      a = get_input()

      if a == 'empty':
         print("Missing input fileld. Please enter a value.")
         break

      if a == 'invalid':
         print("Invalid input value. Please enter (numeric value only)")
         break
      print(double_number(a))

if __name__ == '__main__':
   main()
