option = int(input("Seleccione 1. Registro 2. Login 3. Cerrar  "))
match option:
    case 1:
        print("Resgistro")
    case 2:
        print("Login")
    case 3:
        print("Cerrar")
    case _:
        print("Opció no válida...")