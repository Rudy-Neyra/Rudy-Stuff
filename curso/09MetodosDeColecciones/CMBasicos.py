# Añade un item a un conjunto, si ya existe, no lo añade
c = set()
c.add(1)
c.add(2)
c.add(3)
c.add(4)
print(c)

# Borra un item de un conjunto
c.discard(1)
print(c)

# Devuelve una copia del conjunto
c1 = {1, 2, 3, 4}
c2 = c1.copy()
print(c1, c2)

# Borra todos los items de un conjunto
c2.clear()
print(c2)
