from tkinter import *
from tkinter import ttk

class vistaEwos(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Titulo
        self.label_titulo = Label(self, text = "Registrar Dato 1: ")
        self.label_titulo.grid(row = 0, column = 0, columnspan = 2, pady = 5, padx = 5)