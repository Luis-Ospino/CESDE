numero_secreto = 7
intento = None

print("¡Adivina el número secreto entre 1 y 10!")

while intento != numero_secreto:
    intento = int(input("Ingresa tu número: "))
    
    if intento < numero_secreto:
        print("🔻 Muy bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("🔺 Muy alto. Intenta de nuevo.")
    else:
        print("🎉 ¡Correcto! Adivinaste el número.")
