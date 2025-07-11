# listas en python son mutabñles, aceptan diferentes tipos de datos
# tienen métodos que permiten manipularlas
# son iterables

customer = [123456789, "pepito", "perez", "1600000,14", True]
print(type(customer))
print(customer[4])

# Agregar un nuevo elemento a la lista
# indicar la posición a la que voy a agregar
customer.insert(5, 3235369329)
# agregar al final de la lista
customer.append("pepito@mail.com")
print(customer)

# medir la longitud de una lista
print(len(customer))

# recorrer una lista con un while
contar  = 0
while contar < len(customer):
    print(customer[contar])
    contar+=1

