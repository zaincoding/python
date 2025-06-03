def my_function(lst, index):

   """Accessing element through index input"""
 
   if index < 0   or index >= len(lst):
         return("Index out of bount")
   else:
         return lst[index]
  

def get_index():

    lst:list = ['apple','mango','Pineapple','Orange','banana']
    print(lst)

    index = input("Enter an index.")

    if index == "":
       return None, lst
    
    try:
       index = int(index)
       return index,lst
    except ValueError:
       print("ValueError: Invalid value")
       return 'Invalid',lst
    
def main():
   while True:
      index,lst = get_index()
      if index is None:
         break
      
      if index == 'Invalid':
         continue
      
      if  my_function(lst,index):
          print(my_function(lst,index))
          break

if __name__ == '__main__':
   main()

