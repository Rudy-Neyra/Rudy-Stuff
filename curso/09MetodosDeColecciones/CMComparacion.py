c1 = {1, 2, 3}
c2 = {3, 4, 5}
c3 = {1, 2, 3, 4, 5}
c4 = {1, 2, 3, 4, 5, 6, 7}

# Comprueba si el conjunto es disjunto de otro conjunto
print(c1.isdisjoint(c2))  # En este caso retornara un False, porque no son totalmente diferentes

# Comprueba si el conjunto es subconjunto de otro conjunto
print(c3.issubset(c4))  # En este caso retornara un True, porque el conjunto 3 esta dentro del conjunto 4

# Comprueba si el conjunto es contenedor de otro subconjunto
print(c4.issuperset(c3))  # En este caso retornara un True, porque el conjunto 4 si tiene dentro al conjunto 3
