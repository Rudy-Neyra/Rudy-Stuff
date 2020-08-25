##### Pestaña de profesores
from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *

class vistaProfesores(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def listar_datos():
            #Eliminar datos de la tabla
            recorrer_tabla = self.tabla.get_children()
            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)
            
            #Ejecutar la consulta y carga de datos
            query = 'SELECT * FROM profesor'
            conn = Conectar_db()
            datos = conn.run_db(query)

            for profesor in datos:
                self.tabla.insert('', 0, text = profesor[0], value = (profesor[1], profesor[2], profesor[3]))
        
        def agregar_datos():
            query = 'INSERT INTO profesor VALUES (NULL, ?, ?, ?)'
            parametros = (self.entry_profesor.get(), self.entry_telefono.get(), self.entry_direccion.get())

            conn = Conectar_db()
            conn.run_db(query, parametros)

            #Limpiar campos de entrada
            self.entry_profesor.delete(0, END)
            self.entry_telefono.delete(0, END)
            self.entry_direccion.delete(0, END)

            listar_datos()

        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM profesor WHERE codigo_p = ?'
            
            conn = Conectar_db()
            conn.run_db(query, (codigo, ))

            listar_datos()

        def actualizar_datos(codigo_n, codigo_a, profesor_nuevo, profesor_anti, telefono_nuevo, telefono_anti, direccion_nuevo, direccion_anti):
            query = 'UPDATE profesor SET codigo_p = ?, nombre_p = ?, telefono = ?, direccion = ? WHERE codigo_p = ? AND nombre_p = ? AND telefono = ? AND direccion = ?'
            parametros = (codigo_n, profesor_nuevo, telefono_nuevo, direccion_nuevo, codigo_a, profesor_anti, telefono_anti, direccion_anti)

            conn = Conectar_db()
            conn.run_db(query, parametros)
            self.ventana_editar.destroy()

            listar_datos()

        def nuevo():
            self.entry_profesor.config(state = 'normal')
            self.entry_telefono.config(state = 'normal')
            self.entry_direccion.config(state = 'normal')

        #Titulo
        self.label_titulo = Label(self, text = "Registrar Profesor: ")
        self.label_titulo.grid(row = 0, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Campo nombre del profesor
        self.label_profesor = Label(self, text = "Nombre del profesor: ")
        self.label_profesor.grid(row = 1, column = 0, pady = 5, padx = 5)
        self.entry_profesor = Entry(self, state = 'readonly')
        self.entry_profesor.grid(row = 1, column = 1, pady = 5, padx = 5)
        
        #Campo numero de telefono
        self.label_telefono = Label(self, text = "Numero de telefono: ")
        self.label_telefono.grid(row = 2, column = 0, pady = 5, padx = 5)
        self.entry_telefono = Entry(self, state = 'readonly')
        self.entry_telefono.grid(row = 2, column = 1, pady = 5, padx = 5)

        #Campo direccion
        self.label_direccion = Label(self, text = "Direccion: ")
        self.label_direccion.grid(row = 3, column = 0, pady = 5, padx = 5)
        self.entry_direccion = Entry(self, state = 'readonly')
        self.entry_direccion.grid(row = 3, column = 1, pady = 5, padx = 5)

        #Boton nuevo
        self.boton_nuevo = Button(self, text = "Nuevo", command = nuevo)
        self.boton_nuevo.grid(row = 4, column = 0, pady = 5, padx = 5)

        #Boton guardar
        self.boton_guardar = Button(self, text = "Guardar", command = agregar_datos)
        self.boton_guardar.grid(row = 4, column = 1, pady = 5, padx = 5)

        #Titulo de la tabla
        self.label_titulo_tabla = Label(self, text = "Lista de profesores")
        self.label_titulo_tabla.grid(row = 5, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Tabla
        self.tabla = ttk.Treeview(self, columns = ('', '', ''))
        self.tabla.grid(row = 6, column = 0, columnspan = 2, pady = 5, padx = 5)
        self.tabla.heading('#0', text = "Codigo del profesor")
        self.tabla.heading('#1', text = "Nombre del profesor")
        self.tabla.heading('#2', text = "Telefono")
        self.tabla.heading('#3', text = "Direccion")

        #Editar datos (ventana emergente)
        def editar_datos():

            #Guardar datos de la tabla
            codigo = self.tabla.item(self.tabla.selection())['text']
            profesor_anti = self.tabla.item(self.tabla.selection())['values'][0]
            telefono_anti = self.tabla.item(self.tabla.selection())['values'][1]
            direccion_anti = self.tabla.item(self.tabla.selection())['values'][2]

            #Arranque de ventana
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar profesor")

            #Campo de codigo de la carrera
            Label(self.ventana_editar, text = "Codigo del profesor: ").grid(row = 0, column = 0, pady = 5, padx = 5)
            self.entry_codigo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo), state = 'readonly')
            self.entry_codigo.grid(row = 0, column = 1)

            #Campo de nombre del profesor actual
            Label(self.ventana_editar, text = "Nombre del profesor actual: ").grid(row = 1, column = 0, pady = 5, padx = 5)
            self.entry_nombre_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = profesor_anti), state = 'readonly')
            self.entry_nombre_actual.grid(row = 1, column = 1)

            #Campo de nombre del profesor (nuevo)
            Label(self.ventana_editar, text = "Nombre del profesor nuevo: ").grid(row = 2, column = 0, pady = 5, padx = 5)
            self.entry_nombre_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_nombre_nuevo.grid(row = 2, column = 1)

            #Campo de direccion del profesor (anterior)
            Label(self.ventana_editar, text = "Direccion actual del profesor: ").grid(row = 3, column = 0, pady = 5, padx = 5)
            self.entry_direccion_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = telefono_anti), state = 'readonly')
            self.entry_direccion_actual.grid(row = 3, column = 1)

            #Campo de edad del profesor (nueva)
            Label(self.ventana_editar, text = "Direccion nueva del profesor: ").grid(row = 4, column = 0, pady = 5, padx = 5)
            self.entry_direccion_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_direccion_nuevo.grid(row = 4, column = 1)

            #Campo de telefono del profesor (anterior)
            Label(self.ventana_editar, text = "Telefono actual del profesor: ").grid(row = 5, column = 0, pady = 5, padx = 5)
            self.entry_telefono_actual = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = direccion_anti), state = 'readonly')
            self.entry_telefono_actual.grid(row = 5, column = 1)

            #Campo de telefono del profesor (nueva)
            Label(self.ventana_editar, text = "Telefono nuevo del profesor: ").grid(row = 6, column = 0, pady = 5, padx = 5)
            self.entry_telefono_nuevo = Entry(self.ventana_editar, state = 'normal')
            self.entry_telefono_nuevo.grid(row = 6, column = 1)

            #Boton Actualizar
            self.boton_actualizar = Button(self.ventana_editar, text = "Actualizar profesor", command = lambda: actualizar_datos(codigo, codigo, self.entry_nombre_nuevo.get(), profesor_anti, self.entry_telefono_nuevo.get(), telefono_anti, self.entry_direccion_nuevo.get(), direccion_anti))
            self.boton_actualizar.grid(row = 7, column = 0, columnspan = 2, pady = 5, padx = 5)

        #Boton Editar
        self.boton_editar = Button(self, text = "Editar", command = editar_datos)
        self.boton_editar.grid(row = 7, column = 0, pady = 5, padx = 5)

        #Boton Eliminar
        self.boton_eliminar = Button(self, text = "Eliminar", command = eliminar_datos)
        self.boton_eliminar.grid(row = 7, column = 1, pady = 5, padx = 5)

        listar_datos()