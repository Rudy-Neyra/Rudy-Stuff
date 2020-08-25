from io import open

texto = "Una linea con texto \nOtra linea con texto"
fichero = open('fichero.txt', 'w')  # se crea el archivo txt en la ruta especificada, para escribir debemos incluir la w

fichero.write(texto)  # Se escribe dentro del txt
fichero.close()  # Siempre debemos cerrar
