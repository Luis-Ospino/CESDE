A = 4500
B = 18900
C = 50000

paciente = input("Ingrese su nombre: ")
categoria = input("Indique la categoria: ")

if categoria == "A":
    print(F"Señor {paciente} su pago es de: {A}")
elif categoria == "B":
    print(F"Señor {paciente} su pago es de: {B}")
elif categoria == "C":
    print(F"Señor {paciente} su pago es de: {C}")
else:
    print("pailas")