from tkinter import *
ventana = Tk()
ventana.geometry("630x360")

def seleccionar():
    cadena = ""
    if (marcar01.get()):
        cadena += "Marcado 01 "
    else:
        cadena += "Desmarcado 01 "
    if (marcar02.get()):
        cadena += "y Marcado 02"
    else:
        cadena += "y Desmarcado 02"

    mostrar.config(text = cadena)

marcar01 = IntVar()
marcar02 = IntVar()

Checkbutton(ventana, text = "Marcado 1", variable = marcar01, onvalue = 1, offvalue = 0, command = seleccionar).pack()     #onvalue es cuando esta marcado y offvalue desmarcado
Checkbutton(ventana, text = "Marcado 2", variable = marcar02, onvalue = 1, offvalue = 0, command = seleccionar).pack()

mostrar = Label(ventana)
mostrar.pack()

ventana.mainloop()