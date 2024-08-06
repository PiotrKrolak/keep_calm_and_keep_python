# acces to list
print("acces to list")

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# change list items
print("change list items")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# add list items
print("add list items")

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# remove list items
print("remove list items")

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# remowe second item (index 1)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# remove last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#delate first item with index 0
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#delite entire list
thislist = ["apple", "banana", "cherry"]
del thislist


# loop list
# https://www.w3schools.com/python/python_lists_loop.asp
print("loop list")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# to je dobre!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# List Comprehension
# https://www.w3schools.com/python/python_lists_comprehension.asp
print("List Comprehension")

