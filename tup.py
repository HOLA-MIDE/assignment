#tuple

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) 

print(len(thistuple)) 

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 

mytuple = ("abc", 34, True, 40, "male") 
print(type(mytuple)) 

thistuple = tuple(["apple", "banana", "cherry"]) # note the double round-brackets
print(thistuple) 

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[1]) 
print(thistuple[-1]) 

print(thistuple[2:5]) 
print(thistuple[-4:-1]) 

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 

#change
x = ("apple", "banana", "cherry")
y = list(x)
print(type(y))
y[1] = "kiwi"
x = tuple(y)

print(x) 
print(type(x))

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
y = list(thistuple)
print(type(y))
y.append("orange")
thistuple = tuple(y)
print(thistuple)

y = ("orange",)
thistuple += y

print(thistuple)

#Remove
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) 

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) 

#count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
