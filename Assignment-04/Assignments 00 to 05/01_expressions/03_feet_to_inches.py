# 1 foot = 12inches



def feet_to_inches(ft):
      
      
      result = ft*12

      return(f"{ft}feet = {result}inches")


ft = input("enter number number of feet: ")
   
ft = float(ft)

if  __name__ == '__main__':
     print(feet_to_inches(ft))