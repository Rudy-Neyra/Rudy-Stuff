v = "otro texto"
n = 10

c = "Un texto '{}' y un numero '{}'".format(v, n)
print(c)

print("{:>30}".format("palabra"))  # a la derecha
print("{:30}".format("palabra"))  # a la izquierda
print("{:^30}".format("palabra"))  # al centro

print("{:.3}".format("palabra"))  # Solo escribe 3 caracteres
print("{:>30.3}".format("palabra"))  # 30 espacios a la derecha y solo 3 caracteres

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))

nombre = "Rudy"
texto = f"Hola {nombre}"  # igual que escribir texto = "Hola {}".format(nombre)
print(texto)
