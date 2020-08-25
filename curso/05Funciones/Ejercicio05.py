numeros = [-12, 84, 13, 20, -33, 101, 9]


def separar(lista):
    lista.sort()
    pares = []
    inpares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            inpares.append(n)

    return pares, inpares


pares, inpares = separar(numeros)
print("Pares: ", pares)
print("Inpares: ", inpares)
