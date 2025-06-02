
def update(lst,index,new_value):

    lst[index] = new_value

    return lst


def get_lst():
    lst = ['Apple','Mango','Pineapple','Banana','Grapes']

    while True:
        index = input('Enter index value.')

        if index == "":
            print("Input fields is missing.Please enter some value.")
            continue

        try:
            index = int(index)
            if index< 0 or index >= len(lst):
                print(f"Index out of range. Please enter value between 0 and {len(lst)-1}")
            break #if value valid break the loop.
        except ValueError:
            print("ValueError: Please enter numeric value only.")

    while True:

        new_value = input("Enter new value to update the list.")

        if new_value == "":
            print("Input fields is missing. Please enter some value.")
            continue

        if new_value.isnumeric():
            print("Invlaid input. Please enter value in characters only.")
            continue
        break # if value valid break the loop.

    return(lst,index,new_value)


def main():

    lst,index,new_value = get_lst()

    print(f"List: {lst}, Index: {index}, New Value: {new_value}")

    updated_list =update(lst, index, new_value)

    if updated_list:
        print(updated_list)

if __name__ == '__main__':
    main()