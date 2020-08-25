# Se refiere a que una clase hereda sus atributos y metodos a otra clase y hace nuestro programa mas optimo
# La clase heredada puede incluir sus propios atributos y metodos
class Producto:
    def __init__(self, codigo, nombre, precio, descripcion):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return f"CODIGO\t\t{self.codigo}\n" \
               f"NOMBRE\t\t{self.nombre}\n" \
               f"PRECIO\t\t{self.precio}\n" \
               f"DESCRIPCION.\t{self.descripcion}\n" \
 \
 \
class Adorno(Producto):  # Asi la clase Adorno hereda los atributos de la clase Producto
    pass  # Siempre debe incluir algo asi que poreso ponemos el pass


class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return f"CODIGO\t\t{self.codigo}\n" \
               f"NOMBRE\t\t{self.nombre}\n" \
               f"PRECIO\t\t{self.precio}\n" \
               f"DESCRIPCION.\t{self.descripcion}\n" \
               f"PRODUCTOR.\t{self.productor}\n" \
               f"DISTRIBUIDOR.\t{self.distribuidor}\n" \
 \
 \
class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return f"CODIGO\t\t{self.codigo}\n" \
               f"NOMBRE\t\t{self.nombre}\n" \
               f"PRECIO\t\t{self.precio}\n" \
               f"DESCRIPCION.\t{self.descripcion}\n" \
               f"ISBN.\t\t{self.isbn}\n" \
               f"AUTOR.\t\t{self.autor}\n" \
 \
 \
adorno = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana")
# print(adorno)

alimento = Alimento(2035, "Botella de aceite", 5, "250mL")
alimento.productor = "La aceitera"
alimento.distribuidor = "Distribuido SA"
# print(alimento)

libro = Libro(2036, "Cocina mediterranea", 9, "Recetas sanas y buenas")
libro.isbn = "0-1234567"
libro.autor = "Rudy"
print(libro)
