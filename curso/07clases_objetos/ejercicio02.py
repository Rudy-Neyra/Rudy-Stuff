class coche:
    def __init__(self, color, marca, modelo, hp, puertas, matricula):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.hp = hp
        self.puertas = puertas
        self.matricula = matricula

    def __str__(self):
        return "El coche -> " + self.marca + " " + self.color + " del año " + self.modelo + " con " + self.hp + " caballos de fuerza, " + self.puertas + " puertas y matricula " + self.matricula


class pruebaCoches:
    coches = []

    def __init__(self, coches=[]):
        self.coches = coches

    def mostrar(self):
        for c in self.coches:
            print(c)


c = coche("negro", "aveo", "2018", "4", "4", "FMK-21-56")
pc = pruebaCoches([c])
pc.mostrar()
