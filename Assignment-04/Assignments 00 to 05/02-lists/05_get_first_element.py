
def get_first_element(lst):

   try:
     print(lst[0])
   except IndexError:
       print("IndexError: The list is empty.")

def get_list():
    
    lst = []
    user_input = input("Enter an element or press enter to stop: ")
     
    while user_input != "":
     
        lst.append(user_input)
        user_input = input("Enter an element or press enter to stop: ")

    return lst

def main():
    lst = get_list()
    get_first_element(lst)


        

if __name__ == '__main__':
    main()