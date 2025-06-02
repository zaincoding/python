

def fav_animal() ->str:
    try:
        user_input:str = str(input("Enter your favourite animal name: "))

        if not user_input:
          raise ValueError("Enter some Value.")
        
        if user_input.isdigit():
           raise ValueError("Animal cannot be a number.")

        return (f"My favourite animal is also, {user_input}!")

    except Exception as e:
      return(f"\nError: {e}")

if __name__ == "__main__":
    print(fav_animal())

