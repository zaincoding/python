
def fahrenheit_to_celsius():

        try:
            fahrenheit:str = input("Enter fahrenheit: ")
            
            if not fahrenheit.strip():
                raise ValueError("Error: Input cannot be empty.")
            fahrenheit = float(fahrenheit)            

        except Exception as e:
            print(e)

        else:
            celsius = (fahrenheit -32)*5/9
            print(f"Celsius: {celsius:.2f}")
            print(f"Conversion successful.\n")
        finally:
             print("Conversion process completed.")

fahrenheit_to_celsius()