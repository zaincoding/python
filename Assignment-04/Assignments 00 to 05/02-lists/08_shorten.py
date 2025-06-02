

def shorten_list(lst):
 
    max_value = 3
    while len(lst) > max_value:
       lst.pop()
    print(lst)



def get_lst():
   my_lst = []
   user_input = input("Enter some value or press enter to stop: ")
   while user_input != "":
     my_lst.append(user_input)
     user_input = input("Enter some value or press enter to stop: ")

   return my_lst

def main():
   lst = get_lst()
   shorten_list(lst)

if __name__ == '__main__':
   main()