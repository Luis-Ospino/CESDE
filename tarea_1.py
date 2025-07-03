cliente = {
    'nombre cliente': [],
    'cedula cliente': [],
    'edad cliente': []
}
producto = {
    'nombre producto': [],
    'id producto': [],
    'precio producto': [],
    'stock': []
}
nombre_cliente= input("Digite nombre del cliente: ")
cedula_cliente = input("Digite su cédula: ")
edad_cliente = int(input("Digite su edad: "))

nombre_producto= input("\nDigite nombre del producto: ")
id_producto = input("Digite el id del producto: ")
precio_producto = int(input("Digite el precio del producto: "))
stock = int(input("Digite la cantidad en existencia: "))

cliente['nombre cliente'].append(nombre_cliente)
cliente["cedula cliente"].append(cedula_cliente)
cliente['edad cliente'].append(edad_cliente)

producto['id producto'].append(id_producto)
producto['nombre producto'].append(nombre_producto)
producto['precio producto'].append(precio_producto)
producto['stock'].append(stock)

for clave in cliente:
    print(f"{clave}: ")
    for i, valor in enumerate(cliente[clave]):
        print(f"{valor} | Tipo: {type(valor)}")

for clave2 in producto:
    print(f"{clave2}: ")
    for j, valor2 in enumerate(producto[clave2]):
        print(f"{valor2} | Tipo: {type(valor2)}")