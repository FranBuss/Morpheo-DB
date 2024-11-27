import tkinter as tk
from tkinter import ttk

from src.controllers.GeneralController import GeneralController
from src.controllers.JuegoController import JuegoController
from src.controllers.LibroController import LibroController
from src.controllers.PeliculaController import PeliculaController


class VistaGeneral:

    def __init__(self):
        self.treeview_tabla = None
        self.popup_menu = None
        self.juegoController = JuegoController()
        self.libroController = LibroController()
        self.peliculaController = PeliculaController()
        self.generalController = GeneralController()
        self.ventana = tk.Tk()
        self.ventana.title("MorpheoDB - Gestión de Juegos")
        self.ventana.state('zoomed')
        self.ventana.geometry("1000x600")
        self.ventana.configure(bg='white')
        self.estilizar()
        self.configurar_interfaz()
        self.ventana.mainloop()


    def estilizar(self):
        style = ttk.Style()
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


    def aplicar_estilo_boton(self, boton):
        boton.config(style="TButton")


    def mostrar_menu_contextual(self, event):
        self.popup_menu.post(event.x_root, event.y_root)


    def on_juegos_button_pressed(self):
        self.limpiar_tabla()
        self.abrir_vista_juegos()


    def on_peliculas_button_pressed(self):
        self.limpiar_tabla()
        self.abrir_vista_peliculas()


    def on_libros_button_pressed(self):
        self.limpiar_tabla()
        self.abrir_vista_libros()


    def abrir_vista_peliculas(self):
        from src.views.VistaPelicula import VistaPelicula
        self.ventana.destroy()
        VistaPelicula()


    def abrir_vista_libros(self):
        from src.views.VistaLibro import VistaLibro
        self.ventana.destroy()
        VistaLibro()

    def abrir_vista_juegos(self):
        from src.views.VistaJuego import VistaJuego
        self.ventana.destroy()
        VistaJuego()


    def mostrar_info_juego(self, event=None):
        seleccionado = self.treeview_tabla.focus()
        info_juego = self.treeview_tabla.item(seleccionado)
        juego_id = info_juego['values'][0]
        detalles_juego = self.juegoController.buscar_juego_id(juego_id)
        self.ventana_info_juego = tk.Toplevel(self.ventana)
        self.ventana_info_juego.title("Detalles del Juego")
        self.ventana_info_juego.columnconfigure(0, weight=1)
        frame_principal = ttk.Frame(self.ventana_info_juego, padding="20 20 20 20", relief="sunken")
        frame_principal.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        frame_principal.columnconfigure(0, weight=1)
        frame_principal.rowconfigure(0, weight=1)
        atributos_valores = {
            "Nombre": detalles_juego.nombre,
            "Género": detalles_juego.genero,
            "Fecha de Salida": detalles_juego.fecha_salida,
            "Estado": detalles_juego.estado,
            "Desarrollador": detalles_juego.desarrollador,
            "Distribuidor": detalles_juego.distribuidor,
            "Plataforma": detalles_juego.plataforma,
            "Temática": detalles_juego.tematica,
            "Modo de Juego": detalles_juego.modo_juego,
            "Descripción": detalles_juego.descripcion,
            "Comentario": detalles_juego.comentario,
            "Clasificación": detalles_juego.clasificacion,
        }
        ttk.Label(frame_principal, text="Detalles del Juego", font=("Helvetica", 16, "bold underline")).grid(column=0,
                                                                                                             row=0,
                                                                                                             columnspan=5,
                                                                                                             pady=(0, 10))
        num_columnas = 2
        atributos = list(atributos_valores.items())
        filas = len(atributos) // num_columnas + (len(atributos) % num_columnas > 0)
        for i in range(filas):
            for j in range(num_columnas):
                index = i * num_columnas + j
                if index < len(atributos):
                    atributo, valor = atributos[index]
                    col = j * 2 if j == 0 else j * 2 + 1
                    ttk.Label(frame_principal, text=f"{atributo}:", font=("Helvetica", 10, "bold")).grid(column=col,
                                                                                                         row=(
                                                                                                                     i * 2) + 1,
                                                                                                         sticky=tk.E,
                                                                                                         padx=(0, 5))
                    ttk.Label(frame_principal, text=valor).grid(column=col + 1, row=(i * 2) + 1, sticky=(tk.W, tk.E))
                if j == 0 and i * num_columnas + 1 < len(atributos):
                    # Agrega un separador vertical
                    ttk.Separator(frame_principal, orient=tk.VERTICAL).grid(column=2, row=(i * 2) + 1,
                                                                            sticky=(tk.N, tk.S))
            if i < filas - 1:
                ttk.Separator(frame_principal, orient=tk.HORIZONTAL).grid(column=0, row=2 * (i + 1), columnspan=5,
                                                                          sticky=(tk.W, tk.E))
        fila_final = 2 * filas + 1
        ttk.Separator(frame_principal, orient=tk.HORIZONTAL).grid(column=0, row=fila_final, columnspan=5,
                                                                  sticky=(tk.W, tk.E))
        ttk.Label(frame_principal, text="Puntuación:", font=("Helvetica", 10, "bold")).grid(column=1,
                                                                                            row=fila_final + 1,
                                                                                            sticky=tk.E, padx=(0, 5))
        ttk.Label(frame_principal, text=detalles_juego.puntuacion).grid(column=2, row=fila_final + 1,
                                                                        sticky=(tk.W, tk.E))
        ttk.Button(frame_principal, text="Cerrar", command=self.ventana_info_juego.destroy).grid(column=0,
                                                                                                 row=fila_final + 2,
                                                                                                 columnspan=5,
                                                                                                 pady=(10, 0))
        for child in frame_principal.winfo_children():
            child.grid_configure(pady=5, padx=5)


    def busqueda_por_estado(self, estado):
        juegos = self.juegoController.buscar_por_estado(estado)
        if juegos is None:
            juegos = []

        for i, juego in enumerate(juegos):
            # Determinar si la fila es par o impar
            if i % 2 == 0:
                self.treeview_tabla.insert("", "end", values=(
                    juego[0], juego[1], juego[2], juego[3], juego[4], juego[5], juego[6], juego[7], juego[8], juego[9],
                    juego[10], juego[11], juego[12], juego[13]), tags=('evenrow',))
            else:
                self.treeview_tabla.insert("", "end", values=(
                    juego[0], juego[1], juego[2], juego[3], juego[4], juego[5], juego[6], juego[7], juego[8], juego[9],
                    juego[10], juego[11], juego[12], juego[13]), tags=('oddrow',))


    def busqueda_limpia_por_estado(self, estado):
        self.limpiar_tabla()
        self.busqueda_por_estado(estado)


    def buscar_en_tabla(self, nombre):
        resultado = self.juegoController.buscar_por_nombre(nombre)
        if resultado:
            self.treeview_tabla.delete(*self.treeview_tabla.get_children())  # Limpiar tabla actual
            for i, juego in enumerate(resultado):
                # Determinar si la fila es par o impar
                if i % 2 == 0:
                    self.treeview_tabla.insert("", "end", values=(
                        juego[0], juego[1], juego[2], juego[3], juego[4], juego[5], juego[6], juego[7], juego[8],
                        juego[9],
                        juego[10], juego[11], juego[12], juego[13]), tags=('evenrow',))
                else:
                    self.treeview_tabla.insert("", "end", values=(
                        juego[0], juego[1], juego[2], juego[3], juego[4], juego[5], juego[6], juego[7], juego[8],
                        juego[9],
                        juego[10], juego[11], juego[12], juego[13]), tags=('oddrow',))
            print("Búsqueda completada y tabla actualizada con resultados.")
        else:
            print("No se encontraron resultados para la búsqueda.")


    def refrescar_tabla(self):
        # Limpiar todos los elementos del Treeview
        for item in self.treeview_tabla.get_children():
            self.treeview_tabla.delete(item)
        # Volver a listar juegos
        self.listar_en_tabla()

    def listar_en_tabla(self):
        lista = self.generalController.listar_sin_filtro()
        if lista is None:
            lista = []

        for i, objeto in enumerate(lista):
            values = (objeto[0], objeto[1], objeto[2], objeto[3], objeto.tipo)
            if i % 2 == 0:
                self.treeview_tabla.insert("", "end", values=values, tags=('evenrow',))
            else:
                self.treeview_tabla.insert("", "end", values=values, tags=('oddrow',))


    def configurar_interfaz(self):
        self.ventana.title("MorpheoDB")
        self.ventana.geometry("800x600")
        frame_izquierda = self.crear_frame(self.ventana, side=tk.LEFT)
        self.crear_vista_completa(frame_izquierda)
        self.treeview_tabla.bind("<Double-1>",
                                 self.mostrar_info_elemento)  # Bind doble clic a la función mostrar_info_elemento
        self.ventana.mainloop()

    def mostrar_info_elemento(self, event=None):
        seleccionado = self.treeview_tabla.focus()
        info_elemento = self.treeview_tabla.item(seleccionado)
        elemento_id, nombre, estado, puntuacion, tipo = info_elemento['values']

        if tipo == "juego":
            detalles_elemento = self.juegoController.buscar_juego_id(elemento_id)
            self.mostrar_detalles_juego(detalles_elemento)
        elif tipo == "pelicula":
            detalles_elemento = self.peliculaController.buscar_pelicula_id(elemento_id)
            self.mostrar_detalles_pelicula(detalles_elemento)
        elif tipo == "libro":
            detalles_elemento = self.libroController.buscar_libro_id(elemento_id)
            self.mostrar_detalles_libro(detalles_elemento)

    def mostrar_detalles_juego(self, detalles_juego):
        # Aquí iría el código para mostrar los detalles de un juego
        pass

    def mostrar_detalles_pelicula(self, detalles_pelicula):
        # Aquí iría el código para mostrar los detalles de una película
        pass

    def mostrar_detalles_libro(self, detalles_libro):
        # Aquí iría el código para mostrar los detalles de un libro
        pass

    def crear_frame(self, parent, side):
        frame = tk.Frame(parent)
        frame.pack(side=side, fill=tk.BOTH, expand=True, padx=10, pady=10)
        return frame


    def limpiar_tabla(self):
        if self.treeview_tabla:
            self.treeview_tabla.delete(*self.treeview_tabla.get_children())

    def crear_vista_completa(self, frame):
        frame.config(width=400, height=600, padx=20, pady=20)
        label_menu = ttk.Label(frame, text="Menú", font=("Helvetica", 20), style="TLabel")
        label_menu.pack(side=tk.TOP, pady=20)

        # Panel izquierdo para los botones de vistas
        boton_frame = ttk.Frame(frame)
        boton_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Botones de vista
        self.boton_juegos = ttk.Button(boton_frame, text="Juegos", command=self.on_juegos_button_pressed, width=20)
        self.boton_juegos.pack(pady=10, padx=10)
        self.aplicar_estilo_boton(self.boton_juegos)

        self.boton_peliculas = ttk.Button(boton_frame, text="Películas", command=self.on_peliculas_button_pressed,
                                          width=20)
        self.boton_peliculas.pack(pady=10, padx=10)
        self.aplicar_estilo_boton(self.boton_peliculas)

        self.boton_libros = ttk.Button(boton_frame, text="Libros", command=self.on_libros_button_pressed, width=20)
        self.boton_libros.pack(pady=10, padx=10)
        self.aplicar_estilo_boton(self.boton_libros)

        # Crear el frame principal del contenido a la derecha del panel lateral
        frame_contenido = ttk.Frame(frame)
        frame_contenido.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Aquí empieza la parte original de crear_tabla_vista
        tk.Label(frame_contenido, text="GENERAL").pack()

        # Agregar un separador
        separator = ttk.Separator(frame_contenido, orient="horizontal")
        separator.pack(fill=tk.X, padx=10, pady=10)

        # Frame contenedor para los botones y la barra de búsqueda
        frame_superior = ttk.Frame(frame_contenido)
        frame_superior.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Frame para los botones
        frame_botones = ttk.Frame(frame_superior)
        frame_botones.pack(side=tk.LEFT)

        # Frame para la barra de búsqueda
        frame_busqueda = ttk.Frame(frame_superior)
        frame_busqueda.pack(side=tk.RIGHT, padx=5)

        self.entry_busqueda = ttk.Entry(frame_busqueda)
        self.entry_busqueda.pack(side=tk.LEFT, padx=5)

        btn_buscar = ttk.Button(frame_busqueda, text="Buscar",
                                command=lambda: self.buscar_en_tabla(self.entry_busqueda.get()))
        btn_buscar.pack(side=tk.LEFT, padx=5)

        columnas = ["ID", "Nombre", "Estado", "Puntuación", "Tipo"]

        # Estilos para Treeview
        style = ttk.Style()
        style.configure("Treeview", rowheight=25, bordercolor="#e0e0e0", borderwidth=1, relief="groove")
        style.configure("Treeview.Heading", font=('Calibri', 10, 'bold'), bordercolor="#e0e0e0", borderwidth=1,
                        relief="flat", background="lightgrey")
        style.map("Treeview.Heading", background=[('active', 'grey')], relief=[('active', 'flat')])

        self.treeview_tabla = ttk.Treeview(frame_contenido, columns=columnas, show="headings", style="Treeview")

        # Estilo para las filas
        self.treeview_tabla.tag_configure('evenrow', background='#e8e8e8')
        self.treeview_tabla.tag_configure('oddrow', background='#d0d0d0')

        # Barra de scroll horizontal
        h_scroll = tk.Scrollbar(frame_contenido, orient="horizontal", command=self.treeview_tabla.xview)
        self.treeview_tabla.configure(xscrollcommand=h_scroll.set)

        for col in columnas:
            if col == "ID":
                self.treeview_tabla.column(col, width=50)  # Ajusta el ancho de la columna "ID"
            else:
                self.treeview_tabla.column(col, width=150)  # Ajusta el ancho de otras columnas según sea necesario
            self.treeview_tabla.heading(col, text=col)

        self.treeview_tabla.pack(fill=tk.BOTH, expand=True)
        h_scroll.pack(side=tk.TOP, fill=tk.X)

        self.listar_en_tabla()

if __name__ == "__main__":
    VistaGeneral()