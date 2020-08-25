# Podemos tambien escribir nuestro propio mensaje de error con raise
n = None
if n is None:
    raise ValueError("Error, no se permite un valor nulo")
