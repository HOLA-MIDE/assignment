# a program that search if a number is greater than the other

x = float(input("first number: "))

y = float(input("second number: "))

if x > y:
    print(f"{x} > {y}" )
elif x == y:
    print(f"{x} == {y}" )
else:
    print(f"{x} < {y}" )