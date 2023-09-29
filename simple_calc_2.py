
x = float(input("first number: "))

operation = input("""addition +
subtraction -
multiplication *
division /: """)

y = float(input("second number: "))

if operation == "+":
    print( x + y )
elif operation == "-":
    print( x - y )
elif operation == "*":
    print( x * y )
elif operation == "/":
    print( x / y )
else: 
    print( "Operation must be either +, -, * or / " )
