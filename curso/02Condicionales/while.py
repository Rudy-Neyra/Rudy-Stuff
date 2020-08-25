opcion = 0

while opcion < 10:
    print(opcion)
    opcion += 1

    if opcion == 5:
        # break                             #break rompe la ejecucion del while, nisiquiera entra en else, solo se acaba el ciclo"""
        continue

else:
    print("Termino el ciclo while")
