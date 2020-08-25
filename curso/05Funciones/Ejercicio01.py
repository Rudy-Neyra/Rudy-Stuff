def area_rectangulo(base, altura):
    return base * altura


a = float(input("Ingresa el valor de base: "))
b = float(input("Ingresa el valor de altura: "))

print("Area del rectangulo = ", area_rectangulo(a, b))


def test(num):
    return num, num * 2, num * 4


print(test(5))
