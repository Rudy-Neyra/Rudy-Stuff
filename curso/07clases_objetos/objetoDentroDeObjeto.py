class Pelicula:
    # Constructor de la clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

        print("Se creo la pelicula", self.titulo)

    def __str__(self):
        return "{} lanzado en {} con duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)


class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def mostrar(self):
        for p in self.peliculas:
            print(p)

    def agregar_p(self, p):
        self.peliculas.append(p)


p = Pelicula("El padrino", 175, 1972)
c = Catalogo([p])
c.mostrar()

c.agregar_p(Pelicula("El padrino parte 2", 202, 1974))
c.mostrar()
