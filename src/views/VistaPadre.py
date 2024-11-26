class VistaPadre:

    def __init__(self):
        pass

    def aplicar_estilo_boton(self, boton):
        boton.config(style="TButton")

    def mostrar_menu_contextual(self, event):
        self.popup_menu.post(event.x_root, event.y_root)

    def on_juegos_button_pressed(self):
        self.limpiar_tabla()
        self.listar_juegos_en_tabla()

    def on_peliculas_button_pressed(self):
        self.limpiar_tabla()
        self.abrir_vista_peliculas()

    def on_libros_button_pressed(self):
        self.limpiar_tabla()
        self.abrir_vista_libros()

    def abrir_vista_peliculas(self):
        self.ventana.destroy()
        VistaPelicula()

    def abrir_vista_libros(self):
        self.ventana.destroy()
        VistaLibro()