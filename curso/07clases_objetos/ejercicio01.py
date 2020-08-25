class rectangulo:
    # Constructor de la clase
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return "=====\nBase: " + str(self.base) + " Altura: " + str(self.altura) + "\nArea: " + str(
            self.base * self.altura) + " Perimetro: " + str(2 * self.base + 2 * self.altura) + "\n====="


class PruebaRectangulo:
    rectangulos = []

    def __init__(self, rectangulos=[]):
        self.rectangulos = rectangulos

    def agregar_r(self, r):
        self.rectangulos.append(r)

    def mostrar(self):
        for r in self.rectangulos:
            print(r)


r = rectangulo(2, 4)
pr = PruebaRectangulo([r])
pr.agregar_r(rectangulo(3, 5))
pr.agregar_r(rectangulo(1, 2))
pr.agregar_r(rectangulo(3, 10))
pr.mostrar()
