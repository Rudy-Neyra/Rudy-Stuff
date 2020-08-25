print("Hola Mundo".upper())  # Imprime con todos los caracteres en mayuscuclas
print("Hola Mundo".lower())  # Imprime con todos los caracteres en minusculas
print("Hola Mundo".capitalize())  # Solo el primer caracter en mayuscula
print("hola mundo".title())  # Los primeros caracteres de cada palabra en mayusculas
print("Hola mundo mundo mundo".count(
    "mundo"))  # Cuenta las veces que aparece la palabra mundo, en este caso, regresa un numero entero
print("hola mundo mundo".find(
    'mundo'))  # La posicion del primer caracter de la palabra indicada, contando desde la izquierda
print("hola mundo mundo".rfind(
    'mundo'))  # La posicion del primer caracter de la palabra indicada, contando desde la derecha
print("123".isdigit())  # Devuelve true si la cadena de caracteres es solo numeros
print("ASD3431DSAfds".isalnum())  # Devuelve true cuando la cadena contiene solo alfanumericos
print("ASDCsa".isalpha())  # True si toda la cadena es alfabetica
print("dsafa".islower())  # True si toda la cadena es de minusculas
print("HAJSDSA".isupper())  # True si toda la cadena es de mayusculas
print("Hola Mundo".istitle())  # True si cada palabra inicia con mayuscula
print("      ".isspace())  # True si toda la cadena es de espacios
print("Hola mundo".startswith("Hola"))  # True si la cadena empieza con la subcadena indicada
print("Hola mundo".endswith("mundo"))  # True si la cadena acaba con la subcadena indicada
print("Hola gente del mundo".split(
    " "))  # Devuelve un array, cada subcadena delimitada en este caso por un espacio sera un elemento de ese array
print("-".join("Hola mundo"))  # Cada caracter los une a travez de un guion, en este caso
print("      Hola mundo         ".strip())  # Elimina los espacios innecesarios
print("Hola mundo".replace('o', '0'))  # Reemplaza el primer caracter por el segundo, las veces que se encuentre
