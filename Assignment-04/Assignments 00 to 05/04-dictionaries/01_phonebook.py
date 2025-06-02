

def phone_Book(result):
    
    return result

def get_data():

    user_nmae    = input("Enter name or (press enter to stop): ")
    if user_nmae == "":
        return None
    
    if user_nmae.isnumeric():
       print("Please enter a valid name (not numbers only.)")
       return None

    phone_number = input("Enter phone number or(press enter to stop): ")
    if phone_number == "":
        return None
    
    try:
     phone_number = int(phone_number)
    except ValueError:
       print("Please enter a valid phone number.")
       return None

    return {'name': user_nmae, 'phone': phone_number}

def main():
    phone_data ={}
    while True:
      user_data = get_data()

      if user_data is None:
          break
      
      name = user_data['name']
      phone  = user_data['phone']

      phone_data[name] = phone

      result =phone_Book(phone_data)

      print(result)


if __name__ == '__main__':
    main()
        
    

