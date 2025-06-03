

def slice_list(lst,index,last_index):
    
    return lst[index:last_index]



def get_slice():
    
    lst = ['Apple','Mango','Banana','Pineapple','Watermelon','Grapes']

    while True:
      index = input('Enter first index value: ')

      if index == "":
         print("Missing input value. Please enter an input value.")

      try:
          index = int(index)
          if index < 0 or index >= len(lst):
              print(f"Index value out of range. Pleas enter value b/w 0 and {len(lst)-1}")
              continue
          break
      except ValueError:
          print("ValueError: Please enter numberic value only.")

    while True:
      last_index = input('Enter last index value: ')

      if last_index == "":
         print("Missiong input value. Please enter an input value.")

      try:
          last_index = int(last_index)
          if last_index < 0 or last_index >= len(lst):
              print(f"last index value out of range. Pleas enter value b/w 0 and {len(lst)-1}")
              continue
          break
      except ValueError:
          print("ValueError: Please enter numberic value only.")

    return(lst,index,last_index)

def main():
    
    lst,index,last_index = get_slice()

    sliced_list = slice_list(lst,index, last_index)

    if sliced_list:
     print(sliced_list)

if __name__ == '__main__':
    main()

      
    