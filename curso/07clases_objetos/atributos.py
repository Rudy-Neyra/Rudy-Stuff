# Los atributos son como variables pero de una clase
class Galletas:
    chocolate = False  # Los atributos tambien se pueden declarar dentro de la clase
    sabor = None
    color = None
    forma = "Cuadrada"


galleta = Galletas()
# galleta.sabor = "Salado"        #Estos 3 son atributos de nuestro objeto galleta, el cual pertenece a la clase Galletas
# galleta.color = "Naranja"       #Asi es como se declaran los atributos de un objeto
# galleta.forma = "Cuadrado"

print(galleta.sabor)
