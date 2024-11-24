import tkinter as tk
from tkinter import ttk
from src.views.vistaJuego import VistaJuego  # Asegúrate de que VistaJuegos esté definida en este módulo


class VistaMenu:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Menú Principal - MorpheoDB")
        self.ventana.geometry("1000x600")
        self.ventana.configure(bg='white')
        self.popup_menu = None  # Añadido
        self.estilizar()
        self.configurar_interfaz()
        self.ventana.mainloop()

    def estilizar(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=5)
        style.configure("TLabel", font=("Helvetica", 14), padding=5)
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TFrame", background="white")

    def abrir_vista_juegos(self):
        self.ventana.destroy()
        VistaJuego()

    def mostrar_menu_contextual(self, event):
        self.popup_menu.post(event.x_root, event.y_root)

    def configurar_interfaz(self):
        frame_izquierda = self.crear_frame(self.ventana, side=tk.LEFT)
        frame_derecha = self.crear_frame(self.ventana, side=tk.RIGHT)
        self.crear_menu(frame_izquierda)
        self.crear_presentacion(frame_derecha)

    def crear_frame(self, parent, side):
        frame = ttk.Frame(parent)
        frame.pack(side=side, fill=tk.BOTH, expand=True, padx=10, pady=10)
        return frame

    def crear_presentacion(self, frame):
        label_titulo = ttk.Label(frame, text="Bienvenido a MorpheoDB", font=("Helvetica", 20), style="TLabel")
        label_titulo.pack(pady=20)

        credits_text = """Autores:
        Franco Bussano
        Gaspar Mansilla
        Martin Dezotti
        Marcos Gamba
        """

        label_creditos = ttk.Label(frame, text=credits_text, font=("Helvetica", 14), style="TLabel", justify=tk.LEFT)
        label_creditos.pack(pady=10, padx=10)

    def crear_menu(self, frame):
        label_menu = ttk.Label(frame, text="Menú", font=("Helvetica", 20), style="TLabel")
        label_menu.pack(pady=20)

        frame_botones_menu = ttk.Frame(frame)
        frame_botones_menu.pack(pady=5)

        boton_juegos = ttk.Button(frame_botones_menu, text="Gestionar Juegos", command=self.abrir_vista_juegos)
        boton_juegos.grid(row=0, column=0, padx=5)

        boton_salir = ttk.Button(frame_botones_menu, text="Salir", command=self.ventana.quit)
        boton_salir.grid(row=1, column=0, padx=5, pady=10)


if __name__ == "__main__":
    VistaMenu()
