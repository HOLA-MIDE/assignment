# a program that will take in a string and perform all modifiers

greet = " Hello "
names = "TEMI, OLAMIDE, FORTRESS, GAIUS, WONU, ELLAMS, TOMISIN, SOPHIAT, OLAMIDE"
nums = "10, 20, 15, 30, 12, 48, 31"
nos = "102"
# to index a code
print(greet[0])
print(greet[1])
print(greet[2])
print(greet[3])
print(greet[4])

first_letter = greet[-5]
second_letter = greet[-4]
third_letter = greet[-3]
fourth_letter = greet[-2]
fifth_letter = greet[-1]

print(first_letter, second_letter, third_letter, fourth_letter, fifth_letter)

# to slice a code
print(greet[2:])
print(names[5:])
print(greet[:3])
print(greet[:])
print(greet[1:])
print(greet[-5:])
print(greet[-5:-1])
print(greet[:-1])

# upper case
print(greet.upper())

# lower case
print(greet.lower())
print(names.lower())

# remove whitespace
print(greet.strip())
print(names.strip())
print(nums.strip())

# replace
print(greet.replace("H","J"))

# split
print(names.split(","))
print(nums.split(","))

print(names.capitalize())

print(nums.center(50)) 

print(names.casefold())

print(names.count("OLAMIDE"))

print(greet.encode())
print(names.encode())
print(nums.encode())

print(names.endswith("OLAMIDE"))
print(nums.endswith("16"))
print(greet.endswith("o "))

print(greet.expandtabs(100))

print(greet.find("H"))
print(greet.find("l"))
print(greet.find("o"))
print(greet.find("a"))

print(greet.format())
print(greet.format_map("H"))

print(names.translate("OLAMIDE"))
print(greet.translate("Hello"))

print(names.title())

print(greet.swapcase())
print(names.swapcase())

print(nums.zfill(100))

print(nums.startswith(" 10"))

print(names.splitlines())
print(greet.splitlines())

print(greet.split())
print(names.split())

print(names.rsplit())
print(greet.rsplit())
print(names.rstrip())
print(greet.rstrip())

print(names.index("O"))

print(names.isalnum())
print(greet.isalnum())
print(nums.isalnum())

print(names.isalpha())
print(nos.isdigit())
print(greet.isalpha())
print(names.isascii())
print(nums.isascii())

print(names.isidentifier())
print(greet.islower())
print(nos.isnumeric())

print(names.isspace())
print(names.isprintable())
print(names.istitle())

print(names.isupper())

print(names.join("-"))

print(names.partition("OLA"))
print(names.rpartition("OLA"))
