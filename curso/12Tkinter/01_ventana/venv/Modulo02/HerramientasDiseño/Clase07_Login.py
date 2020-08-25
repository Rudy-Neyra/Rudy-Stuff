from tkinter import *

ventana = Tk()
ventana.geometry("630x360")
ventana.config(bg = "#3CB371")

miFrame = Frame(ventana, width = 200, height = 200)
miFrame.pack()

#======================Labels=================================#
labelUsers = Label(miFrame, text = "Usuario: ")
labelUsers.grid(row = 0, column = 0, pady = 10, padx = 10)

labelPass = Label(miFrame, text = "Password: ")
labelPass.grid(row = 1, column = 0, pady = 10, padx = 10)
#======================Labels=================================#

#======================Entrada de texto=======================#
textoUsers = Entry(miFrame, justify = "left")                       #justify puede ser left, center ó right
textoUsers.grid(row = 0, column = 1, pady = 10, padx = 10)

textPass = Entry(miFrame, justify = "left", show = "*")             #Como textPass es una contraseña, usamos show para que se muestren solo asteriscos en lugar del texto, se puede usar cualquier simbolo
textPass.grid(row = 1, column = 1, pady = 10, padx = 10)
#======================Entrada de texto=======================#

#======================Botones================================#
botonAceptar = Button(miFrame, text = "Aceptar", command = quit)                    #command = quit ó exit, sin parentesis, hara que al dar click en el boton, cierre la ventana
botonAceptar.grid(row = 2, column = 0, pady = 10, padx = 10, columnspan = 2)        #columnspan es para que utilice mas de una columna, en este caso le especificamos 2 columnas
botonAceptar.config(width = 20)                                                     #Cambio en el ancho del boton
#======================Botones================================#

ventana.mainloop()