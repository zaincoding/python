

def weight_calculation(earth_weight):
    """In these program we calculate weight difference on mars and earth"""

   ## mars_weight = earth-weight * 0.378

    mars_weight = earth_weight*0.378
    mars_weight = round(mars_weight, 2)
    mars_weight = (f"\nYour weight on Mars = {mars_weight}")
    
    return mars_weight



def get_weight():

    earth_weight = input("Enter your weight on earth or(press enter to exit): ")

    if earth_weight == "":
        return None
    
    try:
        earth_weight = float(earth_weight)
        return earth_weight
    except ValueError:
        print("ValueError. Invalid value.")
        return "invalid"
    
def main():
    while True:
        earth_weight = get_weight()
        if earth_weight is None:
            break

        if earth_weight == "invalid":
            print("Invalid value. Please enter numbers only")
            continue
        
        if weight_calculation(earth_weight):
            print(weight_calculation(earth_weight))
            break
       


if __name__ == '__main__':
    main()
