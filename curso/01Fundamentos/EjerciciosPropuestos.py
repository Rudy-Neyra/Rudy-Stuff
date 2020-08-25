a = input("¿Cual es el ejercicio que quieres evaluar?")

if (a == "1"):
    # Ejercicio 1
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")

    num1 = int(num1)
    num2 = int(num2)

    print("La suma de los numeros: ", num1 + num2)
    print("La resta de los numeros: ", num1 - num2)
    print("La division de los numeros: ", float(num1) / float(num2))
    print("La multiplicacion de los numeros: ", num1 * num2)

# Ejercicio 2
elif (a == "2"):
    num3 = input("Ingresa el tercer numero: ")
    num4 = input("Ingresa el cuarto numero: ")

    num3 = int(num3)
    num4 = int(num4)

    print("Cociente de la division: ", num3 // num4)
    print("Residuo de la division: ", num3 % num4)

# Ejercicio 3
elif (a == "3"):
    precio = input("Ingresa el valor del producto: ")

    precio = float(precio)
    IGV = 0.18

    print("El IGV del producto es: ", precio * IGV)

# Ejercicio 4
elif (a == "4"):
    num5 = input("Ingresa el numero: ")
    num6 = input("Ingresa el valor de la potencia: ")

    num5 = int(num5)
    num6 = int(num6)

    print("El resultado es: ", num5 ** num6)

# Ejercicio 5
elif (a == "5"):
    num7 = input("Ingrese el valor de a: ")
    num8 = input("Ingrese el valor de n: ")

    num7 = float(num7)
    num8 = float(num8)

    print("El resultado de la operacion es: ", num7 ** 1 / num8)
