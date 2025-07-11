# recorrer una lista con for in
ages = [23, 45, 32, 32, 21, 38, 45]
for age in ages:
    print(age)
print("--------------------------------------")
# recorrer una lista con for in range len
for age in range(len(ages)):
    print(ages[age])
print("--------------------------------------")
# creando lista con comprensión de lista
ages2 = [age for age in ages]
print(ages2)
ages2 = [age for age in ages if age > 30]
print(ages2)


