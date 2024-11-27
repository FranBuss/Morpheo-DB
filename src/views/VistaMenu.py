import tkinter as tk
from tkinter import ttk
from src.views.VistaJuego import VistaJuego
from src.views.VistaPelicula import VistaPelicula
from src.views.VistaLibro import VistaLibro


class VistaMenu:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Menú Principal - MorpheoDB")
        self.ventana.state('zoomed')
        self.ventana.geometry("1000x600")
        self.ventana.configure(bg='white')
        self.popup_menu = None  # Añadido
        self.estilizar()
        self.configurar_interfaz()
        self.ventana.mainloop()

    def estilizar(self):
        style = ttk.Style()
        # Estilos para botones
        style.configure("TButton",
                        font=("Helvetica", 12),
                        padding=10,
                        borderwidth=3,
                        relief="raised",
                        background="#004080",
                        foreground="black")
        style.map("TButton",
                  foreground=[('pressed', 'white'), ('active', '#3399ff')],
                  background=[('pressed', '!disabled', '#004080'), ('active', '#0059b3')])

        # Estilos para etiquetas
        style.configure("TLabel", font=("Helvetica", 16), padding=10, background='#f2f2f2', foreground="#333333")
        style.configure("TEntry", font=("Helvetica", 12), padding=5)
        style.configure("TFrame", background="#f2f2f2")

    def abrir_vista_juegos(self):
        self.ventana.destroy()
        VistaJuego()

    def abrir_vista_peliculas(self):
        self.ventana.destroy()
        VistaPelicula()

    def abrir_vista_libros(self):
        self.ventana.destroy()
        VistaLibro()

    def mostrar_menu_contextual(self, event):
        self.popup_menu.post(event.x_root, event.y_root)

    def configurar_interfaz(self):
        frame_medio = self.crear_frame(self.ventana, side=tk.TOP)
        frame_derecha = self.crear_frame(self.ventana, side=tk.RIGHT)
        self.crear_menu(frame_medio)
        #self.crear_presentacion(frame_derecha)

    def crear_frame(self, parent, side):
        frame = ttk.Frame(parent)
        frame.pack(side=side, fill=tk.BOTH, expand=True, padx=10, pady=10)
        return frame

    """
    def crear_presentacion(self, frame):
        label_titulo = ttk.Label(frame, text="Bienvenido a MorpheoDB", font=("Helvetica", 20), style="TLabel")
        label_titulo.pack(pady=20)

        credits_text = Autores:
        Franco Bussano
        Gaspar Mansilla
        Martin Dezotti
        Marcos Gamba
        

        label_creditos = ttk.Label(frame, text=credits_text, font=("Helvetica", 14), style="TLabel", justify=tk.LEFT)
        label_creditos.pack(pady=10, padx=10)"""

    def crear_menu(self, frame):
        label_bienvendio = ttk.Label(frame, text="Bienvenido a Morpheo", font=("Helvetica", 20), style="TLabel")
        label_bienvendio.pack(pady=20)

        label_menu = ttk.Label(frame, text="Menú", font=("Helvetica", 20), style="TLabel")
        label_menu.pack(pady=20)

        frame_botones_menu = ttk.Frame(frame)
        frame_botones_menu.pack(pady=5)

        boton_juegos = ttk.Button(frame_botones_menu, text="Gestionar Juegos", command=self.abrir_vista_juegos, width=20)
        boton_juegos.grid(row=0, column=0, padx=10, pady=10)

        boton_peliculas = ttk.Button(frame_botones_menu, text="Gestionar Peliculas", command=self.abrir_vista_peliculas, width=20)
        boton_peliculas.grid(row=1, column=0, padx=10, pady=10)

        boton_libros = ttk.Button(frame_botones_menu, text="Gestionar Libros", command=self.abrir_vista_libros, width=20)
        boton_libros.grid(row=2, column=0, padx=10, pady=10)

        boton_salir = ttk.Button(frame_botones_menu, text="Salir", command=self.ventana.quit, width=20)
        boton_salir.grid(row=3, column=0, padx=5, pady=100)


if __name__ == "__main__":
    VistaMenu()
