caballero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}
guerrero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}
arquero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}

caballero['vida'] = 2 * guerrero['vida']
caballero['defensa'] = 2 * guerrero['defensa']

guerrero['ataque'] = 2 * caballero['ataque']
guerrero['alcance'] = 2 * caballero['alcance']

arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa'] // 2
arquero['alcance'] = 2 * guerrero['alcance']

print("Caballero", caballero)
print("Guerrero", guerrero)
print("Arquero", arquero)
