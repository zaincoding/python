

def weight_calculation(earth_weight):
    """In these program we calculate weight difference on earth and other planets"""


    mars_weight = earth_weight*(37.8/100)
    mars_weight = round(mars_weight, 2)
    mars_weight = (f"\nYour weight on Mars = {mars_weight}")



    mercury = earth_weight*(37.6/100)
    mercury = round(mercury, 2)
    mercury = (f"\nYour weight on Mercury = {mercury}")



    venus = earth_weight*(88.9/100)
    venus = round(venus, 2)
    venus = (f"\nYour weight on Venus = {venus}")



    jupiter = earth_weight*(37.6/100)
    jupiter = round(jupiter, 2)
    jupiter = (f"\nYour weight on Jupiter = {jupiter}")



    saturn = earth_weight*(37.6/100)
    saturn = round(saturn, 2)
    saturn = (f"\nYour weight on Saturn = {saturn}")


    uranus = earth_weight*(37.6/100)
    uranus = round(uranus, 2)
    uranus = (f"\nYour weight on Uranus = {uranus}")


    neptune = earth_weight*(37.6/100)
    neptune = round(neptune, 2)
    neptune = (f"\nYour weight on Neptune = {neptune}")

    weight_in_planates = mars_weight,mercury,venus,jupiter,saturn,uranus,neptune

    for i in weight_in_planates:

        print(i)



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
        
        weight_calculation(earth_weight)
        break
       


if __name__ == '__main__':
    main()
