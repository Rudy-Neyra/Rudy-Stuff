# Las tuplas son parecidas a las listas pero no se pueden modificar
tupla = (100, "Hola", [1, 2, 3], -50)

print(tupla[0])

for dato in tupla:
    print(dato)

# tupla[0] = 10          Esto saltara un error

# print(len(tupla))              #Imprime el tamaño de la tupla
# print(len(tupla[2]))           #Imprime el tamaño de la lista dentro de la tupla, solo funciona si hay una lista en esa posicion
# print(tupla.index(100))        #Imprime la posicion del dato 100
# print(tupla.count(100))        #Imprime cuantos 100 hay en la tupla
