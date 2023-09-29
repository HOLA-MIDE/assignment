#set

thisset = {"apple", "banana", "cherry"}
print(thisset) 

# diplicate will be ignored
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) 

# lenght
thisset = {"apple", "banana", "cherry"}

print(len(thisset)) 

# What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset)) 

# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) 

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 

# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 

# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) 

# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) 
# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) 
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset) 
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) 

# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 

thisset = {"apple", "banana", "cherry"}
myset = {"apple", "banana", "cherry", "kiwi"}

set = thisset.difference(myset)
print(set)
set = myset.difference(thisset)
print(set)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 
print(z)
z = y.difference(x)
print(z)

x.difference_update(y)
print(x)

# intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)

x.intersection_update(y)
print(x)
y.intersection_update(x)
print(y)

# isdisjoint
# Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)
print(z)

z = y.isdisjoint(x)
print(z)

# subset
# Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
print(z)

z = y.issuperset(x)
print(z)

# superset
# Return True if all items set y are present in set x:

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)
print(z)

z = y.issubset(x)
print(z)

# Return a set that contains all items from both sets, except items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# Remove the items that are present in both sets, AND insert the items that is not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# Return a set that contains all items from both sets, duplicates are excluded:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

# Insert the items from set y into set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)