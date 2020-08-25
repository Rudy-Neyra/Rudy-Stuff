import time

usuarios = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'}
administradores = {'Juan', 'Marta'}

administradores.discard('Juan')
administradores.add('Marcos')

while True:
    for nombre in usuarios:
        time.sleep(1)
        if nombre in administradores:
            print("%s es administrador" % (nombre))
        else:
            print(nombre)
