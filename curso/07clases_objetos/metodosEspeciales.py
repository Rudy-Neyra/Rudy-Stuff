class Pelicula:
    # Constructor de la clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

        print("Se creo la pelicula ", self.titulo)

    def __del__(self):  # Sin ejecutar del, veremos que se ejecuta automaticamente, esto porque siempre que se ejecuta
        print("Se esta borrando la pelicula ", self.titulo)  # una clase, al finalizar, se elimina

    # Redefiniendo el metodo string
    def __str___(self):
        return self.titulo

    def __len__(self):
        return self.duracion


p = Pelicula("El padrino", 175, 1973)

print(len(p))
