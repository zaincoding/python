def double_each_number():

    "Double each element in a list of numbers."
     
    number_list = [1,2,3,4]

    for i in range(len(number_list)):
          number_list[i] *= 2

    return number_list

if __name__ == '__main__':
    print(double_each_number())


