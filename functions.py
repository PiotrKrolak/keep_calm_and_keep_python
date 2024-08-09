#https://www.w3schools.com/python/python_functions.asp


def my_function(*kids):         # If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
  print("The youngest child is " + kids[2])


def function():
  print("Hello from a function")

def function3(**kid):           # If the number of keyword arguments is unknown, add a double ** before the parameter name.
  print("His last name is " + kid["lname"])

def function4(country = "Norway"):
  print("I am from " + country)

def function5(food):
  for x in food:
    print(x)

def function6():
  pass

def function7(*, x):
  print(x)


###################################################################


my_function("Emil", "Tobias", "Linus")  

function()

function3(fname = "Tobias", lname = "Refsnes")

#function4()
function4("Sweden")
function4("India")
function4()
function4("Brazil")

# function5()
fruits = ["apple", "banana", "cherry"]

function5(fruits)

# function6()
function6()

# function7()
x = 5
# function7(x)