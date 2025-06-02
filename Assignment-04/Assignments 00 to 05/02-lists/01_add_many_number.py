
def get_numbers(numbers):
   
   """Takes a list of numbers and returns the sum of those numbers."""
 
   total = 0

   for number in numbers:

     total += number

   return total
   

def num():
    number_list:list = [1,2,3,4]
    sum_of_number = get_numbers(number_list)
    print(sum_of_number)
      

     
if __name__ == '__main__':
    num()