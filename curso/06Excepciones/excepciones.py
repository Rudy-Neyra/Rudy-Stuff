while True:
    try:  # Actividad principal que intenta hacer
        n = float(input("Introduce un numero: "))
        print(n + 5)
    except:  # Si no logra hacer la actividad principal
        print("Ocurrio un error, introduce bien el numero")
    else:  # Si se logra ejecutar el Try
        print("Todo funciona correctamente")
        break
    finally:  # Lo hace despues de Try o Except, sin importar
        print("Acabo.")
