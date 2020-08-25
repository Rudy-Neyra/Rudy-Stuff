tareas = [
    [6, 'Distribucion'],
    [2, 'Diseño'],
    [1, 'Concepcion'],
    [7, 'Mantenimiento'],
    [4, 'Produccion'],
    [3, 'Planificacion'],
    [5, 'Pruebas'],
]
'''
print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])
'''
print("== Tareas ordenadas ==")
tareas.sort()
for tarea in tareas:
    print(tarea[0], tarea[1])
