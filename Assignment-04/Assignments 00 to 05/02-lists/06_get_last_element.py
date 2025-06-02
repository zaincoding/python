
def get_last_element(lst):
             
  try:
     print(lst[-1])
  except IndexError:
     print("IndexError: The list is enmpty.")

def get_lst():

    my_list = []
    user_input = input("Enter several element or press enter to stop: ")

    while user_input != "":
        my_list.append(user_input)
        user_input = input("Enter several element or press enter to stop: ")


    return my_list

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()



    