# Set Theory

x =set(input("input: " ).split(","))
print(f"{x}")
print(type(x))

y = set(input("input: ").split(","))
print(f"{y}")
print(type(y))
operation = input(""" difference .difference  
difference_update .difference_update:
""")

if operation == "difference":
    print ( x.difference(y) )