from tkinter import *

ventana = Tk()
ventana.geometry("630x360")

miFrame = Frame()
#miFrame.place(x = 20, y = 1)               #En lugar de usar pack, le damos una posicion con coordenadas
miFrame.pack(side = "left", anchor = "n")
miFrame.config(width = "200", height = "200")
miFrame.config(bg = "blue", bd = 25)
miFrame.config(relief = "groove", cursor = "pirate")

ventana.mainloop()