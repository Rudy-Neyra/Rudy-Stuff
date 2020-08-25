#################################
## Cadenas ##

a = "Rudy"
b = 45
c = 12

print("Hola %s tengo %d años" % (a, b))

# El % indica que tomara el literal de una variable
# %c para char
# %s para string
# %d para int
# %f para floats

##########################
# Entradas por teclado #

nombre = input("Ingresa tu nombre: ")

print(nombre)

# Todo lo que ingresemos en input sera tomado automaticamente como string
# Incluso los numeros, si queremos hacer funciones u operaciones con estos numeros debemos ingresarlos a la variable
# a travez de input y despues convertirlos por programacion

###########################
# Operadores logicos

print(not True)
print(True and True)
print(True or False)
