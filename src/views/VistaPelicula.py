import tkinter as tk
from tkinter import ttk


class VistaLibro:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestionar Libros - MorpheoDB")
        self.ventana.geometry("1000x600")
        self.ventana.configure(bg='white')

        self.estilizar()
        self.configurar_interfaz()
        self.ventana.mainloop()

    def estilizar(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=5)
        style.configure("TLabel", font=("Helvetica", 14), padding=5)
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TFrame", background="white")

    def configurar_interfaz(self):
        # Aquí definimos la interfaz específica para gestión de libros
        pass
