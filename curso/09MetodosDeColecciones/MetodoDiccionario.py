# Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
print(colores.get('negro',
                  'No se encuentra'))  # colores.get(lo que busca en el diccionario, si no lo encuentra retorna esto)

# Genera una lista en clave de los registros del diccionario
print(colores.keys())

# Genera una lista en valor de los registros del diccionario
print(colores.values())

# Genera una lista en clave-valor de los registros del diccionario
print(colores.items())
for clave, valor in colores.items():
    print(clave, valor)

# Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto
print(colores.pop("amarillo", "no se encuentra"))  # Si no encuentra la clave amarillo, retornara el segundo mensaje
print(colores)  # amarillo fue eliminado

# Borra todos los registros de un diccionario
colores.clear()
print(colores)
