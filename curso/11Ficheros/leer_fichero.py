from io import open

fichero = open('fichero.txt', 'r')  # Para leer debemos incluir la letra r
texto = fichero.read()
fichero.close()
print(texto)
