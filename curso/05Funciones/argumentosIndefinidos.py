def ejemplo(*args):  # Si queremos recibir argumentos indefinidos por posicion
    for dato in args:
        print(dato)


ejemplo("Rudy", 34, 12.5)


# Podemos hacer lo mismo por nombre en lugar de por posicion
def porNombre(**kwargs):
    print(kwargs)


porNombre(a="Rudy", n=10)  # Podemos recordar la forma de los diccionarios


def nombre_posicion(*args, **kwargs):  # Tambien podemos hacerlo de forma mixta
    print(args, kwargs)


nombre_posicion(2, 3, n=4)
