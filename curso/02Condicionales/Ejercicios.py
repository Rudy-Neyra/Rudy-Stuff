eje = input("¿Que ejercicio quieres evaluar?")

if eje == "1":
    print("Dado 2 numeros diferentes, devolver el numero mayor.")

    num1 = input("Primer numero a comparar: ")
    num2 = input("Segundo numero a comparar: ")
    num1 = int(num1)
    num2 = int(num2)

    print("El numero mayor es: ")
    if num1 < num2:
        print(num2)
    elif num2 < num1:
        print(num1)
    else:
        print("Los numeros son iguales")

elif eje == "2":
    print("Determinar si un numero es positivo, negativo o neutro")

    num = input("Ingresa el numero a evaluar: ")
    num = float(num)

    print("El numero es: ")
    if num < 0:
        print("Negativo")
    elif num > 0:
        print("Positivo")
    else:
        print("Neutro")

elif eje == "3":
    print("Dado un caracter, determine si es una vocal o no")

    car = input('Ingresa el caracter a evaluar: ')
    print(type(car))
    print("El caracter es de tipo: ")

    if car == "a" or car == "e" or car == "i" or car == "o" or car == "u":
        print("El caracter es una vocal")
    else:
        print("El caracter es una consonante")

elif eje == "4":
    print("Determine si el numero es multiplo de 3 y 5")

    n = input("Ingresa el numero a evaluar: ")
    n = int(n)
    m3 = n % 3
    m5 = n % 5

    if m3 == 0:
        print("El numero es multiplo de 3")
    else:
        print("El numero no es multiplo de 3")

    if m5 == 0:
        print("El numero es multiplo de 5")
    else:
        print("El numero no es multiplo de 5")

elif eje == "5":
    print("Determine si un numero entero es par o inpar")

    n = input("Ingrese el numero a evaluar: ")
    n = int(n)
    n = n % 2

    if n == 0:
        print("El numero es par")
    else:
        print("El numero es inpar")

elif eje == "6":
    print("Dado 3 numeros enteros, regresar el numero mayor")
    num1 = input("Primer numero: ")
    num2 = input("Segundo numero: ")
    num3 = input("Tercer numero: ")
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    if num1 > num2 and num1 > num3:
        print("El primer numero es mayor")
    elif num2 > num1 and num2 > num3:
        print("El segundo numero es mayor")
    elif num3 > num1 and num3 > num2:
        print("El tercer numero es mayor")

elif eje == "7":
    print("Dado un numero entero, devolver el doble si el numero es par, caso contrario el triple")
    n = input("Igresa el numero a evaluar: ")
    n = int(n)
    if n % 2 == 0:
        print("El numero es par")
        print(n * 2)
    else:
        print("El numero es inpar")
        print(n * 3)

elif eje == "8":
    print("Dado 3 numeros, devolver el numero en orden asendente")
    n1 = input("Numero 1: ")
    n2 = input("Numero 2: ")
    n3 = input("Numero 3: ")
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    if n1 > n2 and n1 > n3:
        if n2 > n3:
            print("%d, %d, %d"), (n1, n2, n3)
        else:
            print("%d, %d, %d" % (n1, n3, n2))
    elif n2 > n1 and n2 > n3:
        if n1 > n3:
            print("%d, %d, %d" % (n2, n1, n3))
        else:
            print("%d, %d, %d" % (n2, n3, n1))
    elif n3 > n1 and n3 > n2:
        if n1 > n2:
            print("%d, %d, %d" % (n3, n1, n2))
        else:
            print("%d, %d, %d" % (n3, n2, n1))

elif eje == "9":
    print(
        "Un restaurante ofrece un descuento del 10% para consumos de hasta $100.00 \ny un descuento de 20% para consumos mayores, para ambos \ncasos se aplica un impuesto de 19%. \nDeterminar el monto del descuento, el impuesto y \nel importe a pagar")
    desc1 = 0.1
    desc2 = 0.2
    meta = 100.0
    iva = 0.19
    consumo = input("Igresa el consumo: ")
    consumo = float(consumo)
    ivaap = consumo * iva
    if consumo < meta:
        promo = consumo * desc1
        promo1 = consumo - promo
        promo2 = promo1 + ivaap
        print("El monto del descuento es %d" % (promo))
        print("El impuesto sera de %d" % (ivaap))
        print("El total es %d" % (promo2))
    elif consumo >= meta:
        promo = consumo * desc2
        promo1 = consumo - promo
        promo2 = promo1 + ivaap
        print("El monto del descuento es %d" % (promo))
        print("El impuesto sera de %d" % (ivaap))
        print("El monto a pagar es %d" % (promo2))

elif eje == "10":
    desc1 = 0.1
    desc2 = 0.2
    desc3 = 0.3
    meta = 100.0
    meta2 = 200.0
    iva = 0.19
    consumo = input("Igresa el consumo: ")
    consumo = float(consumo)
    ivaap = consumo * iva
    if consumo < meta:
        promo = consumo * desc1
        promo1 = consumo - promo
        promo2 = promo1 + ivaap
        print("El monto del descuento es %d" % (promo))
        print("El impuesto sera de %d" % (ivaap))
        print("El total es %d" % (promo2))
    elif consumo >= meta and consumo < meta2:
        promo = consumo * desc2
        promo1 = consumo - promo
        promo2 = promo1 + ivaap
        print("El monto del descuento es %d" % (promo))
        print("El impuesto sera de %d" % (ivaap))
        print("El monto a pagar es %d" % (promo2))
    elif consumo >= meta2:
        promo = consumo * desc3
        promo1 = consumo - promo
        promo2 = promo1 + ivaap
        print("El monto del descuento es %d" % (promo))
        print("El impuesto sera de %d" % (ivaap))
        print("El monto a pagar es %d" % (promo2))

elif eje == "11":
    op = ["Verano", "Otono", "Invierno", "Primavera"]
    while True:
        n = input("Ingresa el numero: ")
        if n == "salir":
            break
        else:
            n = int(n)
            n -= 1
            print(op[n])

elif eje == "12":
    n1 = input("Ingresa el numero menor: ")
    n2 = input("Ingresa el numero mayor: ")
    n1 = int(n1)
    n2 = int(n2)
    while n2 >= n1:
        print(n2)
        n2 -= 1

elif eje == "13":
    n1 = input("Ingresa el numero menor: ")
    n2 = input("Ingresa el numero mayor: ")
    n1 = int(n1)
    n2 = int(n2)
    pares = 0
    while n2 >= n1:
        if n2 % 2 == 0:
            pares += 1
        n2 -= 1
    print("Cantidad de numeros pares: %d" % (pares))

elif eje == "14":
    while True:
        x = 1
        op = input("Elige una opcion: ")
        if op == "multiplicacion":
            n = input("Ingresa un numero: ")
            n = int(n)
            while x <= 10:
                mul = n * x
                print("%d * %d = %d" % (n, x, mul))
                x += 1
        elif op == "salir":
            break

elif eje == "15":
    while True:
        print("Ingreso al cine")
        print("====================")
        print("1 - Terror")
        print("2 - Accion")
        print("3 - Aventura")
        op = int(input("Elige la opcion: "))
        if op == 1:
            edad = int(input("Ingresa tu edad: "))
            if edad > 18 and edad < 55:
                print("================")
                print("Ingreso permitido")
                print("================")
            else:
                print("================")
                print("Ingreso denegado")
                print("================")
        elif op == 2:
            edad = int(input("Ingresa tu edad: "))
            if edad > 10:
                print("================")
                print("Ingreso permitido")
                print("================")
            else:
                print("================")
                print("Ingreso denegado")
                print("================")
        elif op == 3:
            edad = int(input("Ingresa tu edad: "))
            if edad > 4:
                print("================")
                print("Ingreso permitido")
                print("================")
            else:
                print("================")
                print("Ingreso denegado")
                print("================")
