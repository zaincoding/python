
def check_affirmation(message):

    affirm = "I am capable of doing anything I put my mind to."
        
    if message == affirm:
        print("\nThat's right.")
        return True
           
    else:
      print(f"\nHmmm That was not the affirmation.")
      return False
def get_message():
    print("\nPlease type the following affirmation: I am capable of doing anything I put my mind to.")
    affirm_message = input("Enter the affirmation message: ")

    if affirm_message == "":
        return None
    
    return affirm_message
   
    
def main():
    
   while True:
       message = get_message()
       if message is None:
           break
       
       if check_affirmation(message):
           break
    
if __name__ == '__main__':
    main()
