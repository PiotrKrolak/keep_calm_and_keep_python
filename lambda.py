# A lambda function can take any number of arguments, but can only have one expression.

z = lambda x, y : x**y
print(z(2, 7))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


# Or, use the same function definition to make a function that always triples the number you send in:
mytripler = myfunc(3)

print(mytripler(11))


