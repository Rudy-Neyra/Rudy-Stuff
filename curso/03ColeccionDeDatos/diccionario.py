# Cada elemento de un diccionario debe tener una clave y un significado
datos = {'azul': 'blue', 1: 'uno',
         2: 'dos'}  # un diccionario vacio se define como datos {}, un conjunto vacio se define como set()
print(datos)
print(datos['azul'])

# para agregar datos
datos['verde'] = 'green'
print(datos)

# del(datos['azul'])                 #Elimina el dato 'azul'

for d in datos:
    print(d)  # De esta forma con el for solo mostrara las claves, sin significado

for d in datos:
    print(datos[d])  # De esta forma se mostraran unicamente los valores

for clave, valor in datos.items():
    print(clave, " - ", valor)  # De esta forma se mostrara clave y valor por orden
