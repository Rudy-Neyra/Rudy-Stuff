from tkinter import *

#Ventana
ventana = Tk()
ventana.geometry("630x360")

#Frame u organizador
miFrame = Frame(ventana, width = "630", height = "360")
miFrame.place(x = 1, y = 1)

#Campo de texto
texto01 = Entry(miFrame)
texto01.pack()
texto01.config(fon = ("arial", 14))
texto01.config(bg = "black", fg = "green")

def imprimir():
    label01 = Label(miFrame, text = ("-- > "+texto01.get()))    #text = ("--> "+texto01.get(), isinstance(texto01.get(), str) #La ultima parte imprime True/False si el text ingresado es de tipo string
    label01.pack()                                              #texto01.index(END)  #Regresa la cantidad de caracteres desde la posicion 0 al final, con (ANCHOR), la cantidad de caracteres de 0 a donde este seleccionado
    label01.config(bg = "black", fg = "green")
    label01.config(fon = ("arial black", 14))

    texto01.delete(0, END)                                      #Borra el texto en la casilla de entry, de la posicion 0 al final
    texto01.insert(0, "Jeje")                                   #Inserta a partir de la posicion 0, el texto indicado
    texto01.icursor(END)                                        #Reubica el cursor en la posicion indicada (posicion), si ponemos (END), se reubicara en la posicion final

boton01 = Button(miFrame, text = "Imprimir", command = imprimir)
boton01.pack()

#Ventana en Ejecucion
ventana.mainloop()