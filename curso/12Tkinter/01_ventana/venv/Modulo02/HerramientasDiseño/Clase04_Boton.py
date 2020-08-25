from tkinter import *

def saludar():
    label = Label(miFrame, text = "Naca tu verga")
    label.place(x = 200, y = 10)
    label.config(fon = 18)

ventana = Tk()
ventana.geometry("630x360")

miFrame = Frame(ventana, width = "630", height = "360")
miFrame.place(x = 1, y = 1)

boton01 = Button(miFrame, text = "Saludar", command = saludar)
boton01.place(x = 1)
boton01.config(bg = "black", fg = "white")
boton01.config(fon = ("arial",16))
boton01.config(cursor = "pirate")

imagen = PhotoImage(file = "spidey.png")

boton02 = Button(miFrame, image = imagen, command = saludar)
boton02.place(x = 20, y = 100)
boton02.config(cursor = "pirate")

ventana.mainloop()