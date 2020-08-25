from tkinter import *

ventana = Tk()
ventana.geometry("630x360")

miFrame = Frame(ventana, width = "1080", height = "720", bg = "black")
miFrame.place(x = 1, y = 1)

label01 = Label(miFrame, text = "Hola Mundo")
label01.place(x = 10, y = 10)
label01.config(bg = "gray", fg = "white")
label01.config(fon = ("arial", 20))

print(label01.cget('text'))         #Imprime por consola el timpo de letra y tamaño
print(label01.cget('fg'))           #Imprime por consola el color de letra
print(label01.configure('bg'))      #Imprime por consola el color del fondo

imagen = PhotoImage(file = "spidey.png")
label02 = Label(miFrame, image = imagen).place(x = 50, y = 50)

ventana.mainloop()