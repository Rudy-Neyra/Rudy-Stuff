# Almacenador de datos desordenado
conjunto = {1, 2, 3}
print(conjunto)
conjunto.add(4)
print(conjunto)
conjunto.add(0)
print(conjunto)
conjunto.add("A")
conjunto.add("H")
conjunto.add("Z")
print(conjunto)

nombres = {"Alex", "Alex", "Alex"}
print(nombres)
print("Rudy" in nombres)
print("Alex" in nombres)
print("Alex" not in nombres)

# Podemos convertir una lista a conjunto para eliminar los datos repetidos
# y regresarla a lista, volvera sin los datos repetidos
lista = [1, 2, 2, 2, 3, 3, 2, 1]
print(lista)
conjunto = set(lista)
print(conjunto)
lista = list(conjunto)
print(lista)
