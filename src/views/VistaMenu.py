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

    def crear_menu(self, frame):
        label_bienvendio = ttk.Label(frame, text="Bienvenido a Morpheo", font=("Helvetica", 20, "underline"))
        label_bienvendio.pack(pady=20)
        label_menu = ttk.Label(frame, text="Menú", font=("Helvetica", 20))
        label_menu.pack(pady=20)

        # Crear una caja para los botones
        frame_botones_menu = ttk.LabelFrame(frame, labelanchor="n")
        frame_botones_menu.pack(pady=10)

        botones_menu_frame = ttk.Frame(frame_botones_menu)
        botones_menu_frame.pack(padx=20, pady=10)

        boton_juegos = ttk.Button(botones_menu_frame, text="Gestionar Juegos", command=self.abrir_vista_juegos,
                                  width=20)
        boton_juegos.pack(pady=5)

        boton_peliculas = ttk.Button(botones_menu_frame, text="Gestionar Peliculas", command=self.abrir_vista_peliculas,
                                     width=20)
        boton_peliculas.pack(pady=5)

        boton_libros = ttk.Button(botones_menu_frame, text="Gestionar Libros", command=self.abrir_vista_libros,
                                  width=20)
        boton_libros.pack(pady=5)

        # Crear una caja separada para el botón de salir
        frame_boton_salir = ttk.LabelFrame(frame, labelanchor="n")
        frame_boton_salir.pack(pady=50)

        # Contenedor interno para centrar el botón dentro del LabelFrame
        salir_frame = ttk.Frame(frame_boton_salir)
        salir_frame.pack(padx=20, pady=10)

        boton_salir = ttk.Button(salir_frame, text="Salir", command=self.ventana.quit, width=20)
        boton_salir.pack(pady=10)


if __name__ == "__main__":
    VistaMenu()
