from tkinter import *
ventana = Tk()
ventana.geometry("630x360")

def seleccionado():
    label01.config(text = opcion.get())
def reiniciar():
    opcion.set(None)
    label01.config(text = "")

opcion = IntVar()

Radiobutton(ventana, text = "Opcion 1", variable = opcion, value = 1, command = seleccionado).pack()
Radiobutton(ventana, text = "Opcion 2", variable = opcion, value = 2, command = seleccionado).pack()
Radiobutton(ventana, text = "Opcion 3", variable = opcion, value = 3, command = seleccionado).pack()

label01 = Label(ventana)
label01.pack()

Button(ventana, text = "Limpiar", command = reiniciar).pack()

ventana.mainloop()