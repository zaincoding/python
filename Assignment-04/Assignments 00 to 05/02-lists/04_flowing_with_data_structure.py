def add_three_copies(my_list, data):
    
    for i in range(3):
        my_list.append(data)



def main():
    user_input = input("Enter a message to copy: ")

    messages = []
    print("\nList before:", messages)

    add_three_copies(messages,user_input)

    print("List after:", messages)

if __name__ == '__main__':
    main()
