lista = ["apple", "banana", "orange", "cherry", "peach", "watermelon", "melon"]

for i in range(3):
    print(lista[i])


for j in range(2,5,2):             #sprawdź w range od 3 elementu(bo liczysz od 0) do 6 elementu iterujac co 2
    print(lista[j], end=" ")       #argument end sprawia ze nie ma przejscia do nastepnej lini tylko spacja miedzy wypisanymi rzeczami 
