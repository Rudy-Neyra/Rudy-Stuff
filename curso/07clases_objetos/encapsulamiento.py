# Existen metodos y atributos privados, los cuales se crean dentro de una clase y
# no se pueden acceder a ellos desde fuera
class Ejemplo:
    __atributo_privado = "Soy una tributo inalcanzable desde fuera"

    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde fuera")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()


e = Ejemplo()
# print(e.__atributo_privado)
# e.__metodo_privado()

# Se pueden acceder a estos con un "truco" metiendolos en metodos publicos
print(e.atributo_publico())
e.metodo_publico()
