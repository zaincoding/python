def leap_year(year: int) -> bool:

        if (year % 4 == 0  and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year")
            return True
        
        else:
            print(f"{year} is not a leap year")

            return False


def get_year():
    while True:
        user_input = input("Enter a year or(press enter to stop): ")
        if user_input =="":
            return None
        
        try:
            year = int(user_input)
            return year

        except ValueError:
            print("ValueError: Please enter a valid year")

def main():
    while True:
     year = get_year()
     if year is None:
         print("Exiting: program")
         break

     if leap_year(year):
       print(f"\nBreaking because it's a leap year")
       break


if __name__ == '__main__':
    main()
