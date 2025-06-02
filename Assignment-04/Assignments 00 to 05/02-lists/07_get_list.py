

def get_number_list(lst):

    print(lst)


def get_lst():
    my_lst = []

    user_input = input("Enter a value: ")


    while user_input != "":
        my_lst.append(user_input)
        user_input = input("Enter a value: ")
    return my_lst

def main():
    lst = get_lst()
    get_number_list(lst)

if __name__ == '__main__':
    main()