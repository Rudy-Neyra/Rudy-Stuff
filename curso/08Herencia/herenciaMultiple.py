class A:  # Super clase A
    def __init__(self):
        print("Soy clase A")

    def a(self):
        print("Metodo de la clase A")


class B:  # Super clase B
    def __init__(self):
        print("Soy clase B")

    def b(self):
        print("Metodo de la clase B")


class C(A, B):  # Clase C, hereda las clases A y B
    def c(self):
        print("soy la clase C")


c = C()  # Al momento de ejecutar esto, imprimira lo de la clase A
# Se pueden tener multiples herencias, pero si se tienen metodos iguales, solo heredara el de la izquierda (A, B) <- la A en este caso
c.a()
c.b()  # si ejecutamos esto, se podra ver la herencia de los metodos
c.c()
