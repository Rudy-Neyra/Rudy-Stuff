from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("630x360")

#=======================Ventanas emergentes============================#
def informacion():
    messagebox.showinfo("Hola", "Se corto correctamente")
def advertencia():
    messagebox.showwarning("Alerta", "No puedes copiar el fichero")
def error():
    messagebox.showerror("Error", "Ocurrio un error inesperado")
#=======================Ventanas emergentes============================#

#================Ventanas emergentes lvl intermedio====================#
def pregunta():
    valor = messagebox.askquestion("Salir", "¿Estas seguro de salir?")  #yes/no
    if valor == "yes":
        ventana.quit()
def aceptar():
    valor = messagebox.askokcancel("Cerrar", "¿Esta seguro de cerrar?") #regresa True/False
    if valor:
        ventana.destroy()
def reintentar():
    valor = messagebox.askretrycancel("Reintentar", "Ocurrio un error") #regresa True/False
    if valor:
        pass
#================Ventanas emergentes lvl intermedio====================#

menubar = Menu(ventana)
ventana.config(menu = menubar)

#=======================Menu archivo===================================#
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Archivo", menu = filemenu)
filemenu.add_command(label = "Nuevo", command = reintentar)
filemenu.add_separator()
filemenu.add_command(label = "Abrir")
filemenu.add_command(label = "Guardar")
filemenu.add_command(label = "Cerrar", command = aceptar)
filemenu.add_separator()
filemenu.add_command(label = "Salir", command = pregunta)
#=======================Menu archivo===================================#

#=======================Menu editar====================================#
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Editar", menu = editmenu)
editmenu.add_command(label = "Copiar", command = advertencia)
editmenu.add_command(label = "Cortar", command = informacion)
editmenu.add_command(label = "Pegar", command = error)
#=======================Menu editar====================================#

#=======================Menu Ayuda=====================================#
helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Ayuda", menu = helpmenu)
helpmenu.add_command(label = "Ayuda")
#=======================Menu Ayuda=====================================#

ventana.mainloop()