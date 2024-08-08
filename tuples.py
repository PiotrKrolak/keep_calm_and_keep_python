'''
Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# Access Tuple Items
# https://www.w3schools.com/python/python_tuples_access.asp
print("Access Tuple Items")

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



# Update Tuples
# https://www.w3schools.com/python/python_tuples_update.asp
print("Update Tuples")


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# Unpack Tuples
# https://www.w3schools.com/python/python_tuples_unpack.asp
print("Unpack Tuples")


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Loop Tuples
# https://www.w3schools.com/python/python_tuples_loop.asp
print("Loop Tuples")


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


# Join Tuples
# https://www.w3schools.com/python/python_tuples_join.asp
print("Join Tuples")


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)