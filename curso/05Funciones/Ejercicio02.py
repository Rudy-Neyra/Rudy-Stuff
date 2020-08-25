def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))

print(relacion(a, b))
