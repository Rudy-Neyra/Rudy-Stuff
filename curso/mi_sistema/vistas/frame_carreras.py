##### Ventana de carreras
from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *

class vistaCarrera(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Listar datos
        def listar_datos():
            #Eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)

            #Ejecutar la consulta y cargar datos a la tabla
            query = 'SELECT * FROM carreras'
            conn = Conectar_db()
            datos = conn.run_db(query)

            for carreras in datos:
                self.tabla.insert('', 0, text = carreras[0], value = (carreras[1], carreras[2]))

        #Funcion para el boton "Nuevo", habilita los campos de texto
        def nuevo():
            self.entry_nombre.delete(0, END)
            self.entry_duracion.delete(0, END)
            self.entry_nombre.config(state = 'normal')
            self.entry_duracion.config(state = 'normal')

        #Agregar datos a la base de datos
        def agregar_datos():
            query = 'INSERT INTO carreras VALUES (NULL, ?, ?)'
            parametros = (self.entry_nombre.get(), self.entry_duracion.get())

            conn = Conectar_db()
            conn.run_db(query, parametros)

            #Limpiar campos de entrada
            self.entry_nombre.delete(0, END)
            self.entry_duracion.delete(0, END)

            listar_datos()  #Para actualizar los datos mostrados en la tabla

        #Eliminar datos
        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM carreras WHERE codigo_c = ?'
            conn = Conectar_db()
            conn.run_db(query, (codigo,))

            listar_datos()  #Para actualizar los datos mostrados en la tabla

        def actualizar_datos(codigo_n, codigo_a, nombre_nuevo, nombre_anti, duracion_nueva, duracion_anti):
            query = 'UPDATE carreras SET codigo_c = ?, nombre_c = ?, duracion_c = ? WHERE codigo_c = ? AND nombre_c = ? AND duracion_c = ?'
            parametros = (codigo_n, nombre_nuevo, duracion_nueva, codigo_a, nombre_anti, duracion_anti)

            conn = Conectar_db()
            conn.run_db(query, parametros)
            self.ventana_editar.destroy()

            listar_datos() #Para actualizar la tabla 

        #Titulo
        self.label_titulo = Label(self, text = "Registrar nueva carrera")
        self.label_titulo.grid(row = 0, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Campo de nombre de la carrera
        Label(self, text = "Nombre de la carrera: ").grid(row = 1, column = 0, pady = 5, padx = 5)
        self.entry_nombre = Entry(self, state = 'readonly')
        self.entry_nombre.grid(row = 1, column = 1)

        #Campo de duracion de la carrera
        Label(self, text = "Duracion de la carrera: ").grid(row = 2, column = 0, pady = 5, padx = 5)
        self.entry_duracion = Entry(self, state = 'readonly')
        self.entry_duracion.grid(row = 2, column = 1)

        #Boton Nuevo
        self.boton_nuevo = Button(self, text = "Nuevo", command = nuevo)
        self.boton_nuevo.grid(row = 3, column = 0, pady = 5, padx = 5)

        #Boton Guardar
        self.boton_guardar = Button(self, text = "Guardar", command = agregar_datos)
        self.boton_guardar.grid(row = 3, column = 1, pady = 5, padx = 5)

        #Titulo de la tabla
        self.label_titulo_tabla = Label(self, text = "Lista de carreras")
        self.label_titulo_tabla.grid(row = 4, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Tabla
        self.tabla = ttk.Treeview(self, columns = ('',''))
        self.tabla.grid(row = 5, column = 0, columnspan = 2, pady = 5, padx = 5)
        self.tabla.heading('#0', text = "Codigo de carrera")
        self.tabla.heading('#1', text = "Nombre de carrera")
        self.tabla.heading('#2', text = "Duracion de carrera")

        #Editar datos (ventana emergente)
        def editar_datos():

            #Guardamos los valores de la tabla
            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_anti = self.tabla.item(self.tabla.selection())['values'][0]
            duracion_anti = self.tabla.item(self.tabla.selection())['values'][1]

            #Arranque de ventana
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar carrera")

            #Campo de codigo de la carrera
            Label(self.ventana_editar, text = "Codigo de la carrera: ").grid(row = 0, column = 0, pady = 5, padx = 5)
            self.entry_codigo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo), state = 'readonly')
            self.entry_codigo.grid(row = 0, column = 1)

            #Campo de nombre de la carrera actual
            Label(self.ventana_editar, text = "Nombre de la carrera actual: ").grid(row = 1, column = 0, pady = 5, padx = 5)
            self.entry_nombre_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_anti), state = 'readonly')
            self.entry_nombre_actual.grid(row = 1, column = 1)

            #Campo de nombre de la carrera nueva
            Label(self.ventana_editar, text = "Nombre de la carrera nueva: ").grid(row = 2, column = 0, pady = 5, padx = 5)
            self.entry_nombre_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_nombre_nuevo.grid(row = 2, column = 1)

            #Campo de duracion de la carrera (anterior)
            Label(self.ventana_editar, text = "Duracion actual de la carrera: ").grid(row = 3, column = 0, pady = 5, padx = 5)
            self.entry_duracion_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = duracion_anti), state = 'readonly')
            self.entry_duracion_actual.grid(row = 3, column = 1)

            #Campo de duracion de la carrera (nueva)
            Label(self.ventana_editar, text = "Nueva duracion de la carrera: ").grid(row = 4, column = 0, pady = 5, padx = 5)
            self.entry_duracion_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_duracion_nuevo.grid(row = 4, column = 1)

            #Boton Actualizar
            self.boton_actualizar = Button(self.ventana_editar, text = "Actualizar carrera", command = lambda: actualizar_datos(codigo, codigo, self.entry_nombre_nuevo.get(), nombre_anti, self.entry_duracion_nuevo.get(), duracion_anti))
            self.boton_actualizar.grid(row = 5, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Boton Editar
        self.boton_editar = Button(self, text = "Editar", command = editar_datos)
        self.boton_editar.grid(row = 6, column = 0, pady = 5, padx = 5)

        #Boton Eliminar
        self.boton_eliminar = Button(self, text = "Eliminar", command = eliminar_datos)
        self.boton_eliminar.grid(row = 6, column = 1, pady = 5, padx = 5)

        listar_datos()