# a program to calculate the area and perimeter of square and rectangle #

def square():
    l=float(input("enter the value of lenght :"))
    lenght = l
    print(f"area of square is :{lenght ** 2}")

    print(f"perimeter of square is :{lenght + lenght + lenght + lenght}")

def rectangle():
    l=float(input("enter the value of lenght:"))
    lenght = l
    b=float(input("enter the value of breathe:"))
    breathe = b
    print(f"area of rectangle is :{lenght * breathe}")

    print(f"perimeter of rectangle is :{2 * (l + b)}")
    lenght = l
    breathe = b

print("select your choice\
\n1: square\
\n2: rectangle")

choice = int(input("enter your choice : "))
if choice == 1:
    square()
elif choice == 2:
    rectangle()
else:
    print("ERROR")

 

