while True:
    try:
        n = float(input("Introduce un numer: "))
        print(5 / n)
    except TypeError:
        print("No se puede dividir un numero entre una cadena")
    except ValueError:
        print("Debes introducir un numero")
    except ZeroDivisionError:
        print("No se puede utilizar 0, prueba otro numero")
    except Exception as e:  # Con esto guardamos el error en la variable e
        print("Ha ocurrido un error -> ", type(e).__name__)
    else:
        print("Todo funciono correctamente")
        break
