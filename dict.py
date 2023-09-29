# dictionary

# Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) 

# lenght
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict)) 
print(type(thisdict)) 
x = thisdict["model"]
print(x)

# Get the value of the "model" key:
x = thisdict.get("model")
print(x)

# Get a list of the keys:
x = thisdict.keys() 
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change 

# Get a list of the values:
x = thisdict.values() 
print(x)
# change
x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change 

# add new item
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["color"] = "red"

print(x) #after the change 

#get items
x = thisdict.items() 
print(x)



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change 



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change 

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 

# Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
