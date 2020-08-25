def saludar():
    c = 0
    while c < 5:
        print("Hola esto es una funcion")
        c += 1


saludar()

# no podemos utilizar una variable que se definio dentro de una funcion, fuera de esa funcion
# solamente si la definimos como global, antes del nombre de dicha variable
# si podemos utilizar variables globales dentro de las funciones
