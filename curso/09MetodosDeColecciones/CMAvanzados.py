# Une un conjunto a otro y devuelve el resultado en un nuevo conjunto
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c3 = c1.union(c2)
print(c3)  # Al unirlos, elimina los datos repetidos

# Une un conjunto a otro en el propio conjunto
c1.update(c2)
print(c1)

# Encuentra en el conjunto los elementos no comunes entre dos conjuntos
c1 = {1, 2, 3}
c2 = {3, 4, 5}
print(c2.difference(c1))
print(c1.difference(c2))

# Guarda en el conjunto los elementos no comunes entre dos conjuntos
c1.difference_update(c2)
print(c1)

# Devuelve un conjunto con los elementos comunes en dos conjuntos
c1 = {1, 2, 3}
c2 = {3, 4, 5}
print(c1.intersection(c2))

# Guarda en el conjunto los elementos comunes entre dos conjuntos
c1.intersection_update(c2)
print(c1)

# Devuelve los elementos simetricamente diferentes entre dos conjuntos
c1 = {1, 2, 3}
c2 = {3, 4, 5}
print(c1.symmetric_difference(c2))
