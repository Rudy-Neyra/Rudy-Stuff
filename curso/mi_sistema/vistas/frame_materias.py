##### Pestaña de materias
from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *

class vistaMaterias(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def listar_datos():
            #Eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)
            
            #Ejecutar la consulta y carga de datos 
            query = 'SELECT * FROM materia'
            conn = Conectar_db()
            datos = conn.run_db(query)

            for materia in datos:
                self.tabla.insert('', 0, text = materia[0], value = (materia[1], materia[2]))

        def nuevo():
            self.entry_materia.config(state = 'normal')
            self.entry_creditos.config(state = 'normal')

        def agregar_datos():
            query = 'INSERT INTO materia VALUES (NULL, ?, ?)'
            parametros = (self.entry_materia.get(), self.entry_creditos.get())

            conn = Conectar_db()
            conn.run_db(query, parametros)

            #Limpiar campos de entrada
            self.entry_materia.delete(0, END)
            self.entry_creditos.delete(0, END)

            listar_datos()
        
        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM materia WHERE codigo_m = ?'
            conn = Conectar_db()
            conn.run_db(query, (codigo, ))

            listar_datos()

        def actualizar_datos(codigo_n, codigo_a, nombre_nuevo, nombre_anti, creditos_nuevo, creditos_anti):
            query = 'UPDATE materia SET codigo_m = ?, nombre_m = ?, creditos_m = ? WHERE codigo_m = ? AND nombre_m = ? AND creditos_m = ?'
            parametros = (codigo_n, nombre_nuevo, creditos_nuevo, codigo_a, nombre_anti, creditos_anti)

            conn = Conectar_db()
            conn.run_db(query, parametros)
            self.ventana_editar.destroy()

            listar_datos()

        #Titulo
        self.label_titulo = Label(self, text = "Registrar nueva materia")
        self.label_titulo.grid(row = 0, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Campo nombre de la materia
        self.label_materia = Label(self, text = "Nombre de la materia: ")
        self.label_materia.grid(row = 1, column = 0, pady = 5, padx = 5)
        self.entry_materia = Entry(self, state = 'readonly')
        self.entry_materia.grid(row = 1, column = 1, pady = 5, padx = 5)

        #Campo para creditos de la materia
        self.label_creditos = Label(self, text = "Creditos de la materia: ")
        self.label_creditos.grid(row = 2, column = 0, pady = 5, padx = 5)
        self.entry_creditos = Entry(self, state = 'readonly')
        self.entry_creditos.grid(row = 2, column = 1, pady = 5, padx = 5)

        #Boton nuevo
        self.boton_nuevo = Button(self, text = "Nuevo", command = nuevo)
        self.boton_nuevo.grid(row = 3, column = 0, pady = 5, padx = 5)

        #Boton guardar
        self.boton_guardar = Button(self, text = "Guardar", command = agregar_datos)
        self.boton_guardar.grid(row = 3, column = 1, pady = 5, padx = 5)

        #Titulo de la tabla
        self.label_titulo_tabla = Label(self, text = "Lista de materias")
        self.label_titulo_tabla.grid(row = 4, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Tabla
        self.tabla = ttk.Treeview(self, columns = ('', ''))
        self.tabla.grid(row = 5, column = 0, columnspan = 2, pady = 5, padx = 5)
        self.tabla.heading('#0', text = "Codigo de materia")
        self.tabla.heading('#1', text = "Nombre de la materia")
        self.tabla.heading('#2', text = "Creditos de la materia")

        #Editar datos (ventana emergente)
        def editar_datos():

            #Guardar datos de la tabla
            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_anti = self.tabla.item(self.tabla.selection())['values'][0]
            creditos_anti = self.tabla.item(self.tabla.selection())['values'][1]

            #Arranque de ventana
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar materia")

            #Campo de codigo de la carrera
            Label(self.ventana_editar, text = "Codigo de la materia: ").grid(row = 0, column = 0, pady = 5, padx = 5)
            self.entry_codigo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo), state = 'readonly')
            self.entry_codigo.grid(row = 0, column = 1)

            #Campo de nombre de la materia actual
            Label(self.ventana_editar, text = "Nombre de la materia actual: ").grid(row = 1, column = 0, pady = 5, padx = 5)
            self.entry_materia_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_anti), state = 'readonly')
            self.entry_materia_actual.grid(row = 1, column = 1)

            #Campo de nombre de la materia nueva
            Label(self.ventana_editar, text = "Nombre de la materia nueva: ").grid(row = 2, column = 0, pady = 5, padx = 5)
            self.entry_materia_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_materia_nuevo.grid(row = 2, column = 1)

            #Campo de creditos de la materia (anterior)
            Label(self.ventana_editar, text = "Creditos actuales de la materia: ").grid(row = 3, column = 0, pady = 5, padx = 5)
            self.entry_creditos_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = creditos_anti), state = 'readonly')
            self.entry_creditos_actual.grid(row = 3, column = 1)

            #Campo de creditos de la materia (nueva)
            Label(self.ventana_editar, text = "Creditos nuevos de la materia: ").grid(row = 4, column = 0, pady = 5, padx = 5)
            self.entry_creditos_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_creditos_nuevo.grid(row = 4, column = 1)

            #Boton Actualizar
            self.boton_actualizar = Button(self.ventana_editar, text = "Actualizar materia", command = lambda: actualizar_datos(codigo, codigo, self.entry_materia_nuevo.get(), nombre_anti, self.entry_creditos_nuevo.get(), creditos_anti))
            self.boton_actualizar.grid(row = 5, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Boton Editar
        self.boton_editar = Button(self, text = "Editar", command = editar_datos)
        self.boton_editar.grid(row = 6, column = 0, pady = 5, padx = 5)

        #Boton Eliminar
        self.boton_eliminar = Button(self, text = "Eliminar", command = eliminar_datos)
        self.boton_eliminar.grid(row = 6, column = 1, pady = 5, padx = 5)

        listar_datos()