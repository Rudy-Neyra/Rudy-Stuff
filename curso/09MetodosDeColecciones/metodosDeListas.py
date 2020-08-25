lista = [1, 2, 3, 4, 5]
lista.append(6)  # Añade un item al final de la lista
print(lista)

lista.clear()  # Vacia todos los items de la lista
print(lista)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)  # La l2 se la añadira a la l1
print(l1)

nombre = ["Hola", "mundo", "mundo"]
print(nombre.count("Hola"))  # Cuenta las veces que aparece Hola en la lista

print(nombre.index("mundo"))  # la posicion dentro de la palabra indicada

l = [1, 2, 2, 2, 3, 4]
l.insert(0, 10)  # agrega un item a la lista en una posicion especifica (posicion, item)
print(l)

l.pop()  # Elimina el ultimo item de la lista
print(l)

l.remove(1)  # Elimina el 1 de la lista, en este caso
print(l)

l.reverse()  # Ordena al revez la lista
print(l)

n = [10, 3, 4, 18, 1]
n.sort()  # Ordena la lista de menor a mayor
print(n)

n.sort(reverse=True)  # Ordena la lista de mayor a menor
print(n)
