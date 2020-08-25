def ejemplo():
    return "Cadena retornada"  # No solo puede retornar cadenas de caracteres, tambien listas o numeros


print(ejemplo())


def ejemplo2():
    return [3, 1, 32, 14]


print(ejemplo2()[1])  # En caso de que el retorno sea una lista, podemos especificar el elemento que queremos mostrar


def ejemplo3():
    return "Cadena", 10, [3, 6, 13]  # Se puede retornar mas de un valor


print(ejemplo3())
