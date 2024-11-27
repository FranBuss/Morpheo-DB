import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from src.controllers.JuegoController import JuegoController


class VistaJuego:

    def __init__(self):
        self.treeview_tabla = None
        self.popup_menu = None
        self.juegoController = JuegoController()
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
        self.listar_juegos_en_tabla()

    def on_peliculas_button_pressed(self):
        self.limpiar_tabla()
        self.abrir_vista_peliculas()

    def on_libros_button_pressed(self):
        self.limpiar_tabla()
        self.abrir_vista_libros()

    def on_general_button_pressed(self):
        self.limpiar_tabla()
        self.abrir_vista_general()

    def abrir_vista_general(self):
        from src.views.VistaGeneral import VistaGeneral
        self.ventana.destroy()
        VistaGeneral()

    def abrir_vista_peliculas(self):
        from src.views.VistaPelicula import VistaPelicula
        self.ventana.destroy()
        VistaPelicula()

    def abrir_vista_libros(self):
        from src.views.VistaLibro import VistaLibro
        self.ventana.destroy()
        VistaLibro()

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
        ttk.Label(frame_principal, text="Detalles del Juego", font=("Helvetica", 16, "bold underline")).grid(column=0, row=0,
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

    def agregar_a_la_tabla(self):
        self.mostrar_formulario_agregar()

    def modificar_en_tabla(self):
        self.mostrar_formulario_actualizar()

    def eliminar_de_la_tabla(self):
        selected_item = self.treeview_tabla.selection()
        if not selected_item:
            messagebox.showwarning("Atenti!", "Seleccioná un elemento para eliminar.")
            return

        # Obtener ID del juego (es almacenado en la primera columna)
        item = self.treeview_tabla.item(selected_item)
        values = item['values']
        if not values:
            messagebox.showerror("Error", "El elemento seleccionado no tiene valores.")
            return

        id = values[0]  # Asumimos que el ID es el primer valor

        try:
            self.juegoController.eliminar(id)  # Llama a un método para eliminar el juego en el controlador
            self.treeview_tabla.delete(selected_item)  # Elimina de la vista
            messagebox.showinfo("Éxito", "El juego se ha eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el juego: {e}")

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
        self.listar_juegos_en_tabla()

    def listar_juegos_en_tabla(self):
        juegos = self.juegoController.listar_juegos()
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

    def mostrar_formulario_agregar(self):
        form_window = tk.Toplevel(self.ventana)
        form_window.title("Agregar Juego")
        form_window.geometry("400x600")

        labels = ["Nombre", "Género", "Fecha de Salida", "Estado", "Desarrollador", "Distribuidor", "Plataforma",
                  "Temática", "Modo de Juego", "Descripción", "Comentario", "Clasificación", "Puntuación"]

        entries = {}
        for label in labels:
            frame = tk.Frame(form_window)
            frame.pack(fill=tk.X, padx=5, pady=5)

            tk.Label(frame, text=label, width=15).pack(side=tk.LEFT)

            if label == "Fecha de Salida":
                entry = DateEntry(frame, date_pattern='yyyy-mm-dd')  # Selector de fecha
                entry.pack(fill=tk.X, expand=True)
            elif label == "Estado":
                entry = ttk.Combobox(frame, values=["En juego", "Terminado", "Sin terminar", "Para jugar"])
                entry.set("Para Jugar")
                entry.pack(fill=tk.X, expand=True)
            elif label == "Puntuación":
                entry = ttk.Combobox(frame, values=[str(i) for i in range(11)], state="readonly")  # Opciones de 0 a 10
                entry.set("0")  # Valor por defecto 0
                entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            else:
                entry = tk.Entry(frame)
                entry.pack(fill=tk.X, expand=True)

            entries[label] = entry

        def enviar_datos():
            datos = []
            for label in labels:
                if label == "Nombre" and not entries[label].get():
                    messagebox.showerror("Error", "El campo 'Nombre' es obligatorio.")
                    return  # No continuar si el campo 'Nombre' está vacío
                if label == "Puntuación":
                    valor_puntuacion = entries[label].get()
                    datos.append(valor_puntuacion)
                else:
                    datos.append(entries[label].get() if entries[label].get() else "")

            # Completar los valores predeterminados para otros campos si es necesario
            datos = [dato if dato else "" for dato in datos]

            print("Datos a enviar:", datos)  # Verificar cuántos datos se están enviando

            try:
                # Pasar exactamente 14 parámetros
                self.juegoController.create_game(*datos)
                form_window.destroy()
                self.refrescar_tabla()
                messagebox.showinfo("Éxito", "El juego se ha agregado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear el juego: {e}")

        boton_enviar = tk.Button(form_window, text="Agregar", command=enviar_datos)
        boton_enviar.pack(pady=10)

    def mostrar_formulario_actualizar(self):
        selected_item = self.treeview_tabla.selection()
        if not selected_item:
            messagebox.showwarning("Atenti!", "Seleccioná un elemento para actualizar.")
            return

        item = self.treeview_tabla.item(selected_item)
        values = item['values']
        if not values:
            messagebox.showerror("Error", "El elemento seleccionado no tiene valores.")
            return

        form_window = tk.Toplevel(self.ventana)
        form_window.title("Actualizar Juego")
        form_window.geometry("400x600")

        labels = ["Nombre", "Género", "Fecha de Salida", "Estado", "Desarrollador", "Distribuidor", "Plataforma",
                  "Temática", "Modo de Juego", "Descripción", "Comentario", "Clasificación", "Puntuación"]

        entries = {}
        for i, label in enumerate(labels):
            frame = tk.Frame(form_window)
            frame.pack(fill=tk.X, padx=5, pady=5)

            tk.Label(frame, text=label, width=15).pack(side=tk.LEFT)

            initial_value = values[i + 1] if i + 1 < len(values) else ""
            if label == "Fecha de Salida":
                entry = DateEntry(frame, date_pattern='yyyy-mm-dd')
                if initial_value:
                    entry.set_date(initial_value)
                entry.pack(fill=tk.X, expand=True)
            elif label == "Estado":
                entry = ttk.Combobox(frame, values=["En juego", "Terminado", "Sin terminar", "Para jugar"])
                entry.set(initial_value)
                entry.pack(fill=tk.X, expand=True)
            else:
                entry = tk.Entry(frame)
                entry.insert(0, initial_value)
                entry.pack(fill=tk.X, expand=True)
            entries[label] = entry

        def enviar_datos():
            datos = []
            for i, (label, entry) in enumerate(entries.items()):
                if label == "Fecha de Salida":
                    fecha_str = entry.get()
                    try:
                        fecha = entry.get_date()
                        fecha_str = fecha.strftime('%Y-%m-%d')
                    except:
                        fecha_str = ''
                    if not fecha_str and values[i + 1] == "":
                        datos.append("")
                    else:
                        datos.append(fecha_str)
                else:
                    entry_value = entry.get()
                    if entry_value == "" and (i + 1 >= len(values) or values[i + 1] == ""):
                        datos.append("")
                    else:
                        datos.append(entry_value)

            print("Datos a enviar:", datos)

            try:
                self.juegoController.actualizar(values[0], *datos)
                form_window.destroy()
                self.refrescar_tabla()
                messagebox.showinfo("Éxito", "El juego se ha actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar el juego: {e}")

        boton_enviar = tk.Button(form_window, text="Actualizar", command=enviar_datos)
        boton_enviar.pack(pady=10)

    def configurar_interfaz(self):
        self.ventana.title("MorpheoDB")
        self.ventana.geometry("800x600")

        frame_izquierda = self.crear_frame(self.ventana, side=tk.LEFT)
        self.crear_vista_lateral(frame_izquierda)

        frame_derecha = self.crear_frame(self.ventana, side=tk.RIGHT)
        self.crear_tabla_vista(frame_derecha)

        self.ventana.mainloop()

    def crear_frame(self, parent, side):
        frame = tk.Frame(parent)
        frame.pack(side=side, fill=tk.BOTH, expand=True, padx=10, pady=10)
        return frame

    def limpiar_tabla(self):
        if self.treeview_tabla:
            self.treeview_tabla.delete(*self.treeview_tabla.get_children())

    def crear_vista_lateral(self, frame):
        frame.config(width=400, height=600, padx=20, pady=20)
        label_menu = ttk.Label(frame, text="Menú", font=("Helvetica", 20), style="TLabel")
        label_menu.pack(pady=20)

        # Panel izquierdo para los botones de vistas
        boton_frame = ttk.Frame(frame)  # Asegúrate de que sea ttk.Frame si usas ttk
        boton_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Botones de vista
        self.boton_general = ttk.Button(boton_frame, text="General", command=self.on_general_button_pressed, width=20)
        self.boton_general.pack(pady=10, padx=10)
        self.aplicar_estilo_boton(self.boton_general)

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

    def crear_tabla_vista(self, frame):
        tk.Label(frame, text="JUEGOS").pack()

        estados_juego = ["TODOS" ,"En juego", "Terminado", "Sin terminar", "Para jugar"]

        # Frame contenedor para los botones de acción (Agregar, Modificar, Eliminar)
        frame_botones_accion = tk.Frame(frame)
        frame_botones_accion.pack(side=tk.TOP, fill=tk.X, padx=10, pady=0)
        tk.Button(frame_botones_accion, text="Agregar", command=self.agregar_a_la_tabla).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones_accion, text="Eliminar", command=self.eliminar_de_la_tabla).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones_accion, text="Modificar", command=self.modificar_en_tabla).pack(side=tk.LEFT, padx=5)

        # Agregar un separador
        separator = ttk.Separator(frame, orient="horizontal")
        separator.pack(fill=tk.X, padx=10, pady=10)

        # Frame contenedor para los botones y la barra de búsqueda
        frame_superior = ttk.Frame(frame)
        frame_superior.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Frame para los botones
        frame_botones = ttk.Frame(frame_superior)
        frame_botones.pack(side=tk.LEFT)

        # Crear botones para cada estado del juego
        for estado in estados_juego:
            if estado == "TODOS":
                btn = ttk.Button(frame_botones, text=estado,
                                 command=self.refrescar_tabla)
            else:
                btn = ttk.Button(frame_botones, text=estado,
                                 command=lambda x=estado: self.busqueda_limpia_por_estado(x))
            btn.pack(side=tk.LEFT, padx=5)

        # Frame para la barra de búsqueda
        frame_busqueda = ttk.Frame(frame_superior)
        frame_busqueda.pack(side=tk.RIGHT, padx=5)

        self.entry_busqueda = ttk.Entry(frame_busqueda)
        self.entry_busqueda.pack(side=tk.LEFT, padx=5)

        btn_buscar = ttk.Button(frame_busqueda, text="Buscar", command=lambda: self.buscar_en_tabla(self.entry_busqueda.get()))
        btn_buscar.pack(side=tk.LEFT, padx=5)

        columnas = ["ID", "Nombre", "Género", "Fecha de Salida", "Estado", "Desarrollador", "Distribuidor",
                    "Plataforma",
                    "Temática", "Modo de Juego", "Descripción", "Comentario", "Clasificación", "Puntuación"]

        # Estilos para Treeview
        style = ttk.Style()
        style.configure("Treeview",
                        rowheight=25,
                        bordercolor="#e0e0e0",
                        borderwidth=1,
                        relief="groove")  # Ajuste de estilo general

        style.configure("Treeview.Heading",
                        font=('Calibri', 10, 'bold'),
                        bordercolor="#e0e0e0",
                        borderwidth=1,
                        relief="flat",
                        background="lightgrey")  # Estilo para encabezados

        style.map("Treeview.Heading",
                  background=[('active', 'grey')],
                  relief=[('active', 'flat')])

        self.treeview_tabla = ttk.Treeview(frame, columns=columnas, show="headings", style="Treeview")

        # Estilo para las filas
        self.treeview_tabla.tag_configure('evenrow', background='#e8e8e8')
        self.treeview_tabla.tag_configure('oddrow', background='#d0d0d0')

        # Barra de scroll horizontal
        h_scroll = tk.Scrollbar(frame, orient="horizontal", command=self.treeview_tabla.xview)
        self.treeview_tabla.configure(xscrollcommand=h_scroll.set)

        for col in columnas:
            if col == "ID":
                self.treeview_tabla.column(col, width=50)  # Ajusta el ancho de la columna "ID"
            else:
                self.treeview_tabla.column(col, width=150)  # Ajusta el ancho de otras columnas según sea necesario
            self.treeview_tabla.heading(col, text=col)
        self.treeview_tabla.pack(fill=tk.BOTH, expand=True)

        h_scroll.pack(side=tk.TOP, fill=tk.X)

        self.listar_juegos_en_tabla()

        # Agregar menú contextual
        self.popup_menu = tk.Menu(self.ventana, tearoff=0)
        self.popup_menu.add_command(label="Agregar", command=self.agregar_a_la_tabla)
        self.popup_menu.add_command(label="Modificar", command=self.modificar_en_tabla)
        self.popup_menu.add_command(label="Eliminar", command=self.eliminar_de_la_tabla)
        self.treeview_tabla.bind("<Button-3>", self.mostrar_menu_contextual)

        self.treeview_tabla.bind("<Double-1>", self.mostrar_info_juego)


# Loop
if __name__ == "__main__":
    VistaJuego()
    