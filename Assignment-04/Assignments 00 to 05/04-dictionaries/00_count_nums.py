
def dict_ionary(result):


    return result


def get_user_input():
     user_input = input("Enter number or press enter to stop: ")

     if user_input == "":
        return None
          
     return int(user_input)

     
def main():
    frequency = {}
    while True:
      user_input = get_user_input()
      if user_input is None:
        break
      
      if user_input in frequency:
         frequency[user_input] += 1
      else:
           frequency[user_input] =1

    result = dict_ionary(frequency)

    print(result)


if __name__ == '__main__':
    main()


    