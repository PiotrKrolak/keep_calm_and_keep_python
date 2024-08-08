lista = ["apple", "banana", "orange", "cherry", "peach", "watermelon", "melon"]

for i in range(3):
    print(lista[i])


for j in range(2,5,2):             #sprawdź w range od 3 elementu(bo liczysz od 0) do 6 elementu iterujac co 2
    print(lista[j], end=" ")       #argument end sprawia ze nie ma przejscia do nastepnej lini tylko spacja miedzy wypisanymi rzeczami 





adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)




# while

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1