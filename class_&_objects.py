

# To create a class, use the keyword class:
class MyClass:
  x = 5


# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)


'''
__init__
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


'''
__str__
The __str__() function controls what should be returned when the class object is represented as a string.
If the __str__() function is not set, the string representation of the object is returned:
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


'''
METHODS
Objects can also contain methods. Methods in objects are functions that belong to the object.
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


'''
self
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
'''

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


'''
pass
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
'''

class Person:
  pass