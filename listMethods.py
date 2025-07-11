headers = ["Identificación", "Nombre", "Apellido", "Salario", "Está activo", "Telefono", "Correo"]
customer = []

id = int(input("Ingrese su id: "))
name = input("Ingrese el nombre del empleado: ")
lastName = input("Ingrese el apellido del empleado: ")
salary = float(input("Ingrese el salario del empleado: "))
isActive = bool(input("¿Está activo?: "))
phone = input("Ingrese su teléfono: ")
mail = input("Ingrese correo electrónico: ")

customer.append(id)
customer.append(name)
customer.append(lastName)
customer.append(salary)
customer.append(isActive)
customer.append(phone)
customer.append(mail)

for i 
