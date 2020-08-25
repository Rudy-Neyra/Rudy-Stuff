while True:
    num1 = float(input("Introduce un numero: "))
    num2 = float(input("Introduce un numero: "))
    try:
        resultado = num1 / num2
        print(resultado)
    except:
        print("Prueba con otros numeros")
        print("El segundo numero no puede ser 0")
    else:
        print("Numeros validos")
        break
