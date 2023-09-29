# list

mylist = ["apple", "berry", "orange", "banana", "34", "True", "apple"]
print(mylist)
print(len(mylist))
print(type(mylist))
print(mylist[-1])

thislist = list(("12", "15", "False", "chocolate"))
print(thislist)
print(mylist[3:])
print(mylist[:3])

mylist[1:3] = ["blackcurrent", "watermelon", "kiwi"]
print(mylist)

thislist.append("avacado")
print(thislist)

thislist.insert(2, ("dradon fruit"))
print(thislist)

tropical = ["pineapple", "blackberry"]
thislist.extend(tropical)
print(thislist)

thislist.remove("False")
print(thislist)
thislist.pop(2)
print(thislist)
del thislist[:]
print(thislist)

thislist.clear()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) 

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) 

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) 

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) 

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) 

#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

#append list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) 

# extend() 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 

#count
mylist = ["apple", "berry", "orange", "banana", "34", "True", "apple"]
x = mylist.count("apple")
print(x)





