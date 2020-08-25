from collections import deque

cola = deque(['Alex', 'Roel', 'Franco'])  # Asi se define una cola
print(cola)

cola.append('Maria')  # Se agrega Maria al final
cola.popleft()  # Se retira el primer dato de la cola, en este caso Alex, puede ser agregado en una variable
print(cola)
