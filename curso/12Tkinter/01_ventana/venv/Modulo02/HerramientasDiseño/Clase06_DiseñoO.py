from tkinter import *

ventana = Tk()
ventana.geometry("630x360")
ventana.config(bg = "#3CB371")

espacio01 = Frame(ventana, width = 200, height = 200, bg = "#2E8B57")
espacio01.pack()

#=======================Funciones===========================#
def enterNombre():
    textoNombre.delete(0, END)
    textoNombre.icursor(END)
def enterApellido():
    textoApellido.delete(0, END)
    textoApellido.icursor(END)
def enterTel():
    textoTel.delete(0, END)
    textoTel.icursor(END)
#=======================Funciones===========================#

#=====================Labels================================#
labelNombre = Label(espacio01, text = "Nombre: ")
labelNombre.grid(row = 0, column = 0, pady = 10, padx = 10)

labelApellido = Label(espacio01, text = "Apellido: ")
labelApellido.grid(row = 1, column = 0, pady = 10, padx = 10)

labelTel = Label(espacio01, text = "Telefono: ")
labelTel.grid(row = 2, column = 0, pady = 10, padx = 10)
#=====================Labels================================#

#=====================Campo de textos=======================#
textoNombre = Entry(espacio01)
textoNombre.grid(row = 0, column = 1, pady = 10, padx = 10)

textoApellido = Entry(espacio01)
textoApellido.grid(row = 1, column = 1, pady = 10, padx = 10)

textoTel = Entry(espacio01)
textoTel.grid(row = 2, column = 1, pady = 10, padx = 10)
#=====================Campo de textos=======================#

#=======================Botones=============================#
#Incluir botones
boton01 = Button(espacio01, text = "Enter", command = enterNombre)
boton01.grid(row = 0, column = 2, pady = 10, padx = 10)

boton02 = Button(espacio01, text = "Enter", command = enterApellido)
boton02.grid(row = 1, column = 2, pady = 10, padx = 10)

boton03 = Button(espacio01, text = "Enter", command = enterTel)
boton03.grid(row = 2, column = 2, pady = 10, padx = 10)
#=======================Botones=============================#

ventana.mainloop()