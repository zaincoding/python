
def voting_age(age):
   if age >=16:
      print("\nYou can vote in \"Peturksbouipo\"")
   else:
      print(f"\nyou can not vote in \"Peturksbouipo\" voting age is {age}")
        
   if age >=25:
       print("\nYou can vote in \"Stanlau\"")
   else:
      print(f"\nYou can't vote in \"Stanlau\" your age is {age}")

   if age >=48:
      print("\nYou can vote in \"Mayengua\"")

   else:
      print(f"\nYou can't vote in \"Mayengua\" your age is {age}")
    

def user_data():
   
   age= int(input("Please enter your age: "))

   return age

def main():
   age = user_data()
   voting_age(age)


if __name__ == '__main__':
   main()
