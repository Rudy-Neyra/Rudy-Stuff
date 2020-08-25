# Los metodos son como las funciones de las clases
class Galletas:
    chocolate = False  # Los atributos tambien se pueden declarar dentro de la clase
    sabor = None
    color = None
    forma = "Cuadrada"

    def __init__(self, sabor=None, color=None):  # Este metodo se efectua cuando un objeto se crea
        # sabor y color no tienen que ver con sabor y color de la clase, estos existen dentro de el metodo
        self.sabor = sabor
        self.color = color  # Por esa razon, los declaramos
        print("Se creo una galleta {} de sabor {}".format(color, sabor))

    def chocolatear(
            self):  # Metodo para cambiar el valor de chocolate, en los metodos de las clases siempre debe llevar la palabra self
        self.chocolate = True  # para referirnos a uno de los atributos de la clase debemos usar la palabra self tambien

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta con chocolate")
        else:
            print("Soy una galleta sin chocolate")


g = Galletas("Salado", "Naranja")  # Le damos los argumentos de sabor y color

g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()

print(g.chocolate)
