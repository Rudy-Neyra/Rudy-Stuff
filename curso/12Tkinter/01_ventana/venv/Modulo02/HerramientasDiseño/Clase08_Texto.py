from tkinter import *
ventana = Tk()
ventana.config(bg = "black")
ventana.geometry("630x360")

miFrame = Frame(ventana)
miFrame.pack()

campoTexto = Text(miFrame)
campoTexto.grid(row = 0, column = 0)
campoTexto.config(width = 30, height = 10)
campoTexto.config(bg = "white", fg = "black", fon = ("arial", 20))

scrolVert = Scrollbar(miFrame, command = campoTexto.yview)
scrolVert.grid(row = 0, column = 1, sticky = "nesw")
campoTexto.config(yscrollcommand = scrolVert.set)

ventana.mainloop()