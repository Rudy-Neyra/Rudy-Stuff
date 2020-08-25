from tkinter import *
from tkinter import ttk
from vistas.frame_carreras import *
from vistas.frame_materias import *
from vistas.frame_alumno import *
from vistas.frame_profesores import *

##### Diseño de la ventana

class Aplicacion(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        ##### Configuracion de ventana inicial
        self.mi_ventana = ventana
        self.mi_ventana.iconbitmap("img/icono_mi_sistema.ico")
        self.mi_ventana.title("Sistema universitario")
        self.mi_ventana.geometry("1020x900")

        ##### Contenedor de paneles
        self.navegador = ttk.Notebook(self)

        ##### Asignacion de pestañas
        ##### Panel de inicio
        self.inicio = Label(self.navegador, text = "Pagina de inicio")
        self.navegador.add(self.inicio, text = "Inicio ")

        ##### Panel de carrera
        self.reg_carrera = vistaCarrera(self.navegador)
        self.navegador.add(self.reg_carrera, text = "Carrera ")

        ##### Panel de materias
        self.reg_materias = vistaMaterias(self.navegador)
        self.navegador.add(self.reg_materias, text = "Materias")
        ##### Asignacion de pestañas

        ##### Panel de alumno
        self.reg_alumno = vistaAlumnos(self.navegador)
        self.navegador.add(self.reg_alumno, text = "Alumno")

        ##### Panel de profesor
        self.reg_prof = vistaProfesores(self.navegador)
        self.navegador.add(self.reg_prof, text = "Profesor")

        self.navegador.pack()
        self.pack()