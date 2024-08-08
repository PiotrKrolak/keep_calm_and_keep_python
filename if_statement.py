'''
Equals:                     a == b
Not Equals:                 a != b
Less than:                  a < b
Less than or equal to:      a <= b
Greater than:               a > b
Greater than or equal to:   a >= b
'''

godzina = 18
ladna_pogoda = False

if godzina >= 20 and not ladna_pogoda:
    print("Wracamy do domu")
elif godzina >= 20 or ladna_pogoda:
    print("Zostajemt")
else:
    print("rob co chcesz")