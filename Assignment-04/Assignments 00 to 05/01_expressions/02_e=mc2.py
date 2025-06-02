
# # # #E = m*c**2

def main(m):

    c = 299792458 

    E = m*c**2
    
    print("e = m*c^2")
    print(f"m = {m} kg")
    print(f"c = {c}")
    return (f"E = {E}  joules of energy!")

m = input("Enter value in kilo: ")

a = float(m)

if __name__ =='__main__':
 print(main(a))