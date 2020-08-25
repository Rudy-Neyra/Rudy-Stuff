def resta(a, b):  # En este caso, a y b son los parametros
    r = a - b
    return r


r = resta(10, 2)  # El 10 y 2 son los argumentos, que le daran valor a los parametros a y b
print(r)
# En el caso anterior le mandamos los argumentos por posicion pero tambien se pueden enviar por nombre

r2 = resta(b=3, a=5)  # Asi se envian argumentos por nombre
print(r2)
