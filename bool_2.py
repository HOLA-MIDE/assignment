# a program that will interact with someone 

a = input("what is your name: ")
print(f" {a}")

b = input("what is your surname: ")
print(f"Hello, {b} {a}")

c =input("please insert age: ")

d = "18"

if c >= d:
    print(f"citizen is eligible to vote")
else:
    print(f"citizen is not eligible to vote")