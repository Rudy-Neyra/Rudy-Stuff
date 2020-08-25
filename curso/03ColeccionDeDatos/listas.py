numeros = [3, 4, 1, 7, 8]
print(numeros)
print(numeros[0:2])  # Imprime 0 y 1
print(numeros[:-2])  # Imprime 0, 1 y 2

pares = [0, 2, 4, 5, 8, 10]
pares[3] = 6
print(pares)

# Funciones o metodos de listas
c = len(pares)  # Tamanio de la lista
pares.append(12)  # Al final de la lista agregara el dato entre parentesis
print(c)
print("Lista de pares acutualizada: ", pares)
