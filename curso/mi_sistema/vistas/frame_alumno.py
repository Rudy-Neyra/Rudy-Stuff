##### Pestaña de alumnos
from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *

class vistaAlumnos(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Muestra de la tabla
        def listar_datos():
            #Eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)

            #Ejecutar la consulta y carga de datos
            query = '''SELECT codigo_a, nombre_a, edad_a, telefono_a, nombre_c FROM alumno 
                    INNER JOIN carreras ON alumno.codigo_c1 = carreras.codigo_c'''
            conn = Conectar_db()
            datos = conn.run_db(query)

            for alumno in datos:
                self.tabla.insert('', 0, text = alumno[0], value = (alumno[1], alumno[2], alumno[3], alumno[4]))

        def nuevo():
            self.entry_alumno.config(state = 'normal')
            self.entry_edad.config(state = 'normal')
            self.entry_telefono.config(state = 'normal')

        def agregar_datos():
            carrera = self.carre_combo.get()
            carrera = carrera[0]+carrera[1]
            print(carrera)
            query = 'INSERT INTO alumno VALUES (NULL, ?, ?, ?, ?)'
            parametros = (self.entry_alumno.get(), self.entry_edad.get(), self.entry_telefono.get(), carrera)

            conn = Conectar_db()
            conn.run_db(query, parametros)

            #Limpiar campos de entrada
            self.entry_alumno.delete(0, END)
            self.entry_edad.delete(0, END)
            self.entry_telefono.delete(0, END)

            listar_datos()  #Para actualizar

        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM alumno where codigo_a = ?'
            conn = Conectar_db()
            conn.run_db(query, (codigo, ))

            listar_datos()

        def actualizar_datos(codigo_n, codigo_a, nombre_nuevo, nombre_anti, edad_nuevo, edad_anti, telefono_nuevo, telefono_anti):
            query = 'UPDATE alumno SET codigo_a = ?, nombre_a = ?, edad_a = ?, telefono_a = ? WHERE codigo_a = ? AND nombre_a = ? AND edad_a = ? AND telefono_a = ?'
            parametros = (codigo_n, nombre_nuevo, edad_nuevo, telefono_nuevo, codigo_a, nombre_anti, edad_anti, telefono_anti)

            conn = Conectar_db()
            conn.run_db(query, parametros)
            self.ventana_editar.destroy()

            listar_datos()

        #Titulo
        self.label_titulo = Label(self, text = "Registrar Alumno: ")
        self.label_titulo.grid(row = 0, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Campo nombre del alummno
        self.label_alumno = Label(self, text = "Nombre del alumno: ")
        self.label_alumno.grid(row = 1, column = 0, pady = 5, padx = 5)
        self.entry_alumno = Entry(self, state = 'readonly')
        self.entry_alumno.grid(row = 1, column = 1, pady = 5, padx = 5)

        #Campo edad del alumno
        self.label_edad = Label(self, text = "Edad del alumno: ")
        self.label_edad.grid(row = 2, column = 0, pady = 5, padx = 5)
        self.entry_edad = Entry(self, state = 'readonly')
        self.entry_edad.grid(row = 2, column = 1, pady = 5, padx = 5)

        #Campo telefono del alumno
        self.label_telefono = Label(self, text = "Telefono del alumno: ")
        self.label_telefono.grid(row = 3, column = 0, pady = 5, padx = 5)
        self.entry_telefono = Entry(self, state = 'readonly')
        self.entry_telefono.grid(row = 3, column = 1, pady = 5, padx = 5)

        #Combo box para elegir carreras
        self.label_comboCarreras = Label(self, text = "Escoger Carreras: ")
        self.label_comboCarreras.grid(row = 4, column = 0, pady = 5, padx = 5)
        self.carre_combo = ttk.Combobox(self)
        self.carre_combo.grid(row = 4, column = 1, pady = 5, padx = 5)

        #Cargar datos al combobox de carreras
        def cargar_combo():
            query = 'SELECT codigo_c, nombre_c FROM carreras'
            conn = Conectar_db()
            datos_c = conn.run_db(query)

            for carreras in datos_c:
                values = list(self.carre_combo["values"])
                self.carre_combo["values"] = values + [(carreras[0], ',', carreras[1])]

        #Ejecucion de cargar combo
        cargar_combo()

        #Boton nuevo
        self.boton_nuevo = Button(self, text = "Nuevo", command = nuevo)
        self.boton_nuevo.grid(row = 5, column = 0, pady = 5, padx = 5)

        #Boton guardar
        self.boton_guardar = Button(self, text = "Guardar", command = agregar_datos)
        self.boton_guardar.grid(row = 5, column = 1, pady = 5, padx = 5)

        #Titulo de la tabla
        self.label_titulo_tabla = Label(self, text = "Lista de alumnos")
        self.label_titulo_tabla.grid(row = 6, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Tabla
        self.tabla = ttk.Treeview(self, columns = ('', '', '', ''))
        self.tabla.grid(row = 7, column = 0, columnspan = 2, pady = 5, padx = 5)
        self.tabla.heading('#0', text = "Codigo del alumno")
        self.tabla.heading('#1', text = "Nombre del alumno")
        self.tabla.heading('#2', text = "Edad")
        self.tabla.heading('#3', text = "Telefono")
        self.tabla.heading('#4', text = "Carrera")

        #Editar datos (ventana emergente)
        def editar_datos():

            #Guardamos los valores de la tabla
            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_anti = self.tabla.item(self.tabla.selection())['values'][0]
            edad_anti = self.tabla.item(self.tabla.selection())['values'][1]
            telefono_anti = self.tabla.item(self.tabla.selection())['values'][2]

            #Arranque de ventana
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar alumno")

            #Campo de codigo de la carrera
            Label(self.ventana_editar, text = "Codigo del alumno: ").grid(row = 0, column = 0, pady = 5, padx = 5)
            self.entry_codigo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo), state = 'readonly')
            self.entry_codigo.grid(row = 0, column = 1)

            #Campo de nombre del alumno actual
            Label(self.ventana_editar, text = "Nombre del alumno actual: ").grid(row = 1, column = 0, pady = 5, padx = 5)
            self.entry_nombre_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_anti), state = 'readonly')
            self.entry_nombre_actual.grid(row = 1, column = 1)

            #Campo de nombre del alumno (nuevo)
            Label(self.ventana_editar, text = "Nombre del alumno nuevo: ").grid(row = 2, column = 0, pady = 5, padx = 5)
            self.entry_nombre_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_nombre_nuevo.grid(row = 2, column = 1)

            #Campo de edad del alumno (anterior)
            Label(self.ventana_editar, text = "Edad actual del alumno: ").grid(row = 3, column = 0, pady = 5, padx = 5)
            self.entry_edad_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = edad_anti), state = 'readonly')
            self.entry_edad_actual.grid(row = 3, column = 1)

            #Campo de edad del alumno (nueva)
            Label(self.ventana_editar, text = "Edad nueva del alumno: ").grid(row = 4, column = 0, pady = 5, padx = 5)
            self.entry_edad_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_edad_nuevo.grid(row = 4, column = 1)

            #Campo de telefono del alumno (anterior)
            Label(self.ventana_editar, text = "Telefono actual del alumno: ").grid(row = 5, column = 0, pady = 5, padx = 5)
            self.entry_telefono_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = telefono_anti), state = 'readonly')
            self.entry_telefono_actual.grid(row = 5, column = 1)

            #Campo de telefono del alumno (nueva)
            Label(self.ventana_editar, text = "Telefono nuevo del alumno: ").grid(row = 6, column = 0, pady = 5, padx = 5)
            self.entry_telefono_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_telefono_nuevo.grid(row = 6, column = 1)

            #Boton Actualizar
            self.boton_actualizar = Button(self.ventana_editar, text = "Actualizar alumno", command = lambda: actualizar_datos(codigo, codigo, self.entry_nombre_nuevo.get(), nombre_anti, self.entry_edad_nuevo.get(), edad_anti, self.entry_telefono_nuevo.get(), telefono_anti))
            self.boton_actualizar.grid(row = 7, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Boton Editar
        self.boton_editar = Button(self, text = "Editar", command = editar_datos)
        self.boton_editar.grid(row = 8, column = 0, pady = 5, padx = 5)

        #Boton Eliminar
        self.boton_eliminar = Button(self, text = "Eliminar", command = eliminar_datos)
        self.boton_eliminar.grid(row = 8, column = 1, pady = 5, padx = 5)

        listar_datos()