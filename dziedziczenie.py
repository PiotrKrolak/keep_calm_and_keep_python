# Python Inheritance

'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

[PL]
Dziedziczenie pozwala nam zdefiniować klasę, która dziedziczy wszystkie metody i właściwości z innej klasy.
Klasa nadrzędna to klasa, z której dziedziczymy, nazywana również klasą bazową.
Klasa potomna to klasa, która dziedziczy z innej klasy, nazywana również klasą pochodną.
'''


# utworzenie klasy person z parametrami i predefiniowana metoda
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# utworzenie klasy student ktora dziedziczy z klasy person
class Student(Person):
  pass


#  dowod ze student odziedziczyl parametry i metody z klasy person
x = Student("Mike", "Olsen")
x.printname()


# uzycie funkcji __init__() sprawai ze dziecko nie dziedziczy od rodzica tej funkcji (lub nadpisuje ja w obrebie dziecka)
class Student(Person):
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

y = Student("Pioter", "King")
y.printname()


# można też użyć funkcji __init__() w taki sposob jak ponizej - odniesc sie odrazu do parametrow z klasy Person
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

z = Student("Janusz", "Bak")
z.printname()


# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


    