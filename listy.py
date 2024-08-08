'''
Method	Description
append()  	Adds an element at the end of the list
clear()   	Removes all the elements from the list
copy()	    Returns a copy of the list
count()   	Returns the number of elements with the specified value
extend()	  Add the elements of a list (or any iterable), to the end of the current list
index() 	  Returns the index of the first element with the specified value
insert()	  Adds an element at the specified position
pop()	      Removes the element at the specified position
remove()	  Removes the item with the specified value
reverse()	  Reverses the order of the list
sort()    	Sorts the list
'''


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

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# Sort Lists
# https://www.w3schools.com/python/python_lists_sort.asp
print("Sort Lists")

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# Copy Lists
# https://www.w3schools.com/python/python_lists_copy.asp
print("Copy Lists")


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# Join Lists
# https://www.w3schools.com/python/python_lists_join.asp
print(" Join Lists")


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


