# A set is a collection which is unordered, unchangeable*, and unindexed.

'''
Method	Shortcut	Description
add()	 	                                Adds an element to the set
clear()	 	                                Removes all the elements from the set
copy()	 	                                Returns a copy of the set
difference()        	            -	    Returns a set containing the difference between two or more sets
difference_update()	                -=  	Removes the items in this set that are also included in another, specified set
discard()	 	                            Remove the specified item
intersection()	                    &	    Returns a set, that is the intersection of two other sets
intersection_update()	            &=	    Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                        Returns whether two sets have a intersection or not
issubset()	                        <=	    Returns whether another set contains this set or not
 	                                <	    Returns whether all items in this set is present in other, specified set(s)
issuperset()	                    >=	    Returns whether this set contains another set or not
 	                                >	    Returns whether all items in other, specified set(s) is present in this set
pop()	 	                                Removes an element from the set
remove()	 	                            Removes the specified element
symmetric_difference()	            ^	    Returns a set with the symmetric differences of two sets
symmetric_difference_update()	    ^=	    Inserts the symmetric differences from this set and another
union()	                            |	    Return a set containing the union of sets
update()	                        |=	    Update the set with the union of this set and others
'''


# Acces Set Items
# https://www.w3schools.com/python/python_sets_access.asp
print("Acces Set Items")


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)


# Add Set Items
# https://www.w3schools.com/python/python_sets_add.asp
print("Add Set Items")


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)

print(thisset)


# Remove Set Items
# https://www.w3schools.com/python/python_sets_remove.asp
print("Remove Set Items")


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()

print(thisset)


thisset = {"apple", "banana", "cherry"}
# del thisset # usuwa set

print(thisset)


# Loop Sets
# https://www.w3schools.com/python/python_sets_loop.asp
print("Loop Sets")


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Join Sets
# https://www.w3schools.com/python/python_sets_join.asp
print("Join Sets")


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

del set1
del set2
del set3


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2      # You can use the | operator instead of the union() method, and you will get the same result.
print(set3)

del set1
del set2
del set3

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

del set1
del set2
del set3
del set4


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

del set1
del set2
del set3
del set4


x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

del x
del y
del z


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

del set1
del set2


