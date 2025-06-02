

def  game_interaction(select_option):

    lst = ['Apple','Mango','Pineapple','Grapes','Banana']

    if select_option == 'access':
        return lst
    
    if select_option == 'modify':

        while True:
            index = input("Enter index value: ")

            if index == "":
                print("Missiong one input field. Please enter some value.")
                continue

            try:
                index = int(index)
                if index<0 or index >= len(lst):
                    print(f"Index out of range. Please enter value b/w 0 and {len(lst)-1}")
                break
            except ValueError:
                print("Invalid Value: Please enter numberic value only.")

        while True:

                new_value = input("Enter a new value to modify the list: ")

                if new_value == "":
                    print("Missing one input field value. Please enter some value.")
                    continue

                if new_value.isnumeric():
                    print("Invalid Value: Please enter value in character only.")
                    continue
                break
        
        lst[index] = new_value

        return lst

     





    
    if select_option == 'slice':
        while True:
            
            index = input("Enter first index: ")
            if index == "":
                print("Missing input value. Please enter some value.")

            try:
                index = int(index)
                if index<0 or index >= len(lst):
                    print(f"Index value out of range. Please enter value b/w 0 and {len(lst)-1}")
                break
            except ValueError:
                print("Invalid value. Please enter numberic value only.")

        while True:
            
            last_index = input("Enter first last index: ")
            if last_index == "":
                print("Missing input value. Please enter some value.")

            try:
                last_index = int(last_index)
                if last_index<0 or last_index >= len(lst):
                    print(f"last index value out of range. Please enter value b/w 0 and {len(lst)-1}")
                break
            except ValueError:
                print("Invalid value. Please enter numberic value only.")
                
        if index > last_index:
            print("Starting index should be less or equal to the ending index.")
            return []
        
        return lst[index:last_index]

def get_select_value():

    while True:
         
         opetions = ['Access','Modify', 'Slice']
         for index, i in enumerate(opetions):
             
             print(f"{index+1}. {i}")

         select_option = input("Enter an option to perform operation").lower().strip()

         if select_option == 'access':
             return select_option
         
         if select_option == 'modify':
             return select_option
         
         if select_option == 'slice':
             return select_option


def main():

    select_option = get_select_value()

    result = game_interaction(select_option)

    if result:
        if select_option == 'access':
          print(f"List Displayed: {result}")

    if result:
        if select_option == 'slice':
          print(f"List Sliced: {result}")

    if result:
        if select_option == 'modify':
          print(f"List Updated: {result}")



if __name__ == '__main__':
    main()
             

         



