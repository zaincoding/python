

def triangle(a,b,c):
  
   return a+b+c

  
while True:   
   try:
        input_a = input("Enter side 'A' value: ")
        input_b = input("Enter side 'B' value: ")
        input_c = input("Enter side 'C' value: ")
        if not input_a.strip() or not input_b.strip() or not input_c.strip():
            raise ValueError("One or more inputs are empty.")
    
    
        try:
            side_a = float(input_a)
            side_b = float(input_b)
            side_c = float(input_c)
        except ValueError:
            raise ValueError("Invalid input: Please enter numeric value only.")


        if(side_a + side_b > side_c and side_a + side_c> side_b and side_c + side_b > side_a):
              print(f"Total Length: {triangle(side_a,side_b,side_c)}")
              break
        else:
                print("The sum of the two side should be greater than the third one.")
                break

   except Exception as e:
           print("Input Error:",e)




