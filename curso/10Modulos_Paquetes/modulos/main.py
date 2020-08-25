"""
import saludos    #Asi importamos el script saludos, Si importamos de esta forma, solo podemos usar las funciones o clases poniedo antes de su invocacion un saludos.saludr()

saludos.saludar()       #Para invocar la funcion saludar
saludos.Saludo()        #Para invocar la clase saludo
"""
from saludos import saludar, Saludo  # Si importamos asi no debemos poner el saludos.saludar()

saludar()
Saludo()

# Tambien podemos importar con
# from saludos import *   <-- Con el asterisco le decimos que queremos importar todas las funciones y clases que contenga saludos.py
