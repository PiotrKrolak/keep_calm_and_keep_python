# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


'''
Method	Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''


# Access Dictionary Items
# https://www.w3schools.com/python/python_dictionaries_access.asp
print("Access Dictionary Items")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
y = thisdict.get("brand")

z = thisdict.keys()

print(x)
print(y)
print(z)

print(thisdict)

thisdict["color"] = "white"

print(thisdict)


val = thisdict.values()

print(val)


thisdict["color"] = "red"


print(thisdict["color"])




# Change Dictionary Items
# https://www.w3schools.com/python/python_dictionaries_change.asp
print("Change Dictionary Items")


thisdict.update({"year": 2020})
print(thisdict)


# Remove Dictionary Items
# https://www.w3schools.com/python/python_dictionaries_remove.asp
print("Remove Dictionary Items")


thisdict.pop("model")
print(thisdict)


thisdict.popitem()
print(thisdict)


#thisdict.clear()
print(thisdict)


# Loop Dictionaries
# https://www.w3schools.com/python/python_dictionaries_loop.asp
print("Loop Dictionaries")


for x in thisdict:
  print(x)


for x in thisdict:
  print(thisdict[x])


for x in thisdict.values():
  print(x)


for x in thisdict.keys():
  print(x)


# to je dobreeeee !!!!!
for x, y in thisdict.items():
  print(x, y)


# Copy Dictionaries
# https://www.w3schools.com/python/python_dictionaries_copy.asp
print("Copy Dictionaries")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()
print(mydict)


car = dict(thisdict)
print(car)


# Nested Dictionaries
# https://www.w3schools.com/python/python_dictionaries_nested.asp
print("Nested Dictionaries")


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# or

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}



print(myfamily["child2"]["name"])



for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


