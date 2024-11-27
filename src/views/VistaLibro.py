import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from src.controllers.LibroController import LibroController


class VistaLibro:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestionar Libros - MorpheoDB")
        self.ventana.geometry("1000x600")
        self.ventana.configure(bg='white')
        self.ventana.state('zoomed')
        self.libroController = LibroController()
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
        self.listar_libros_en_tabla()

    def abrir_vista_peliculas(self):
        from src.views.VistaPelicula import VistaPelicula
        self.ventana.destroy()
        VistaPelicula()

    def abrir_vista_libros(self):
        self.ventana.destroy()
        VistaLibro()

    def abrir_vista_juegos(self):
        from src.views.VistaJuego import VistaJuego
        self.ventana.destroy()
        VistaJuego()

    def mostrar_info_libro(self, event=None):
        seleccionado = self.treeview_tabla.focus()
        info_libro = self.treeview_tabla.item(seleccionado)
        libro_id = info_libro['values'][0]
        detalles_libro = self.libroController.buscar_libro_id(libro_id)

        self.ventana_info_libro = tk.Toplevel(self.ventana)
        self.ventana_info_libro.title("Detalles del libro")

        self.ventana_info_libro.columnconfigure(0, weight=1)

        frame_principal = ttk.Frame(self.ventana_info_libro, padding="20 20 20 20", relief="sunken")
        frame_principal.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        frame_principal.columnconfigure(0, weight=1)
        frame_principal.rowconfigure(0, weight=1)

        atributos_valores = {
            "Nombre": detalles_libro.nombre,
            "Estado": detalles_libro.estado,
            "Género": detalles_libro.genero,
            "Autor": detalles_libro.autor,
            "Editorial": detalles_libro.editorial,
            "Fecha de Publicación": detalles_libro.fecha_publicacion,
            "Página Actual": detalles_libro.pagina_actual,
            "Cantidad de Páginas": detalles_libro.cant_paginas,
            "Descripción": detalles_libro.descripcion,
            "Clasificación": detalles_libro.clasificacion,
            "Puntuación": detalles_libro.puntuacion,
            "Wiki": detalles_libro.wiki,
        }

        ttk.Label(frame_principal, text="Detalles del libro", font=("Helvetica", 16, "bold")).grid(column=0, row=0,
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
        ttk.Label(frame_principal, text=detalles_libro.puntuacion).grid(column=2, row=fila_final + 1,
                                                                        sticky=(tk.W, tk.E))
        ttk.Button(frame_principal, text="Cerrar", command=self.ventana_info_libro.destroy).grid(column=0,
                                                                                                 row=fila_final + 2,
                                                                                                 columnspan=5,
                                                                                                 pady=(10, 0))
        for child in frame_principal.winfo_children():
            child.grid_configure(pady=5, padx=5)

    def refrescar_tabla(self):
        # Limpiar todos los elementos del Treeview
        for item in self.treeview_tabla.get_children():
            self.treeview_tabla.delete(item)
        # Volver a listar libros
        self.listar_libros_en_tabla()

    def buscar_en_tabla(self, nombre):
        resultado = self.peliculaController.buscar_por_nombre(nombre)
        if resultado:
            self.treeview_tabla.delete(*self.treeview_tabla.get_children())  # Limpiar tabla actual
            for i, libro in enumerate(resultado):
                if i % 2 == 0:
                    self.treeview_tabla.insert("", "end", values=(
                        libro[0], libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7],
                        libro[8], libro[9],
                        libro[10], libro[11], libro[12]), tags=('evenrow',))
                else:
                    self.treeview_tabla.insert("", "end", values=(
                        libro[0], libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7],
                        libro[8], libro[9],
                        libro[10], libro[11], libro[12]), tags=('oddrow',))
            print("Búsqueda completada y tabla actualizada con resultados.")
        else:
            print("No se encontraron resultados para la búsqueda.")

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
            self.libroController.eliminar(id)  # Llama a un método para eliminar el libro en el controlador
            self.treeview_tabla.delete(selected_item)  # Elimina de la vista
            messagebox.showinfo("Éxito", "El libro se ha eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el libro: {e}")

    def busqueda_por_estado(self, estado):
        libros = self.libroController.buscar_por_estado(estado)

        if libros is None:
            libros = []

        for i, libro in enumerate(libros):
            if i % 2 == 0:
                self.treeview_tabla.insert("", "end", values=(
                    libro[0], libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7],
                    libro[8], libro[9],
                    libro[10], libro[11], libro[12]), tags=('evenrow',))
            else:
                self.treeview_tabla.insert("", "end", values=(
                    libro[0], libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7],
                    libro[8], libro[9],
                    libro[10], libro[11], libro[12]), tags=('oddrow',))

    def busqueda_limpia_por_estado(self, estado):
        self.limpiar_tabla()
        self.busqueda_por_estado(estado)

    def agregar_a_la_tabla(self):
        self.mostrar_formulario_agregar()

    def modificar_en_tabla(self):
        self.mostrar_formulario_actualizar()

    def listar_libros_en_tabla(self):
        libros = self.libroController.listar_libros()
        if libros is None:
            libros = []

        for i, libro in enumerate(libros):
            if i % 2 == 0:
                self.treeview_tabla.insert("", "end", values=(
                    libro[0], libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7],
                    libro[8], libro[9],
                    libro[10], libro[11], libro[12]), tags=('evenrow',))
            else:
                self.treeview_tabla.insert("", "end", values=(
                    libro[0], libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7],
                    libro[8], libro[9],
                    libro[10], libro[11], libro[12]), tags=('oddrow',))

    def mostrar_formulario_agregar(self):
        form_window = tk.Toplevel(self.ventana)
        form_window.title("Agregar libro")
        form_window.geometry("400x600")

        labels = ["Nombre", "Estado", "Genero", "Autor", "Editorial", "Fecha de publicacion", "Pagina actual", "Cantidad de paginas",
                  "Descripcion", "Clasificacion", "Puntuacion", "Wiki"]


        entries = {}
        for label in labels:
            frame = tk.Frame(form_window)
            frame.pack(fill=tk.X, padx=5, pady=5)

            tk.Label(frame, text=label, width=15).pack(side=tk.LEFT)

            if label == "Fecha de publicacion":
                entry = DateEntry(frame, date_pattern='yyyy-mm-dd')  # Selector de fecha
                entry.pack(fill=tk.X, expand=True)
            elif label == "Estado":
                entry = ttk.Combobox(frame, values=["Para leer", "Leido", "Sin leer", "En pausa"])
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
                self.libroController.create_libro(*datos)
                form_window.destroy()
                self.refrescar_tabla()
                messagebox.showinfo("Éxito", "El libro se ha agregado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear el libro: {e}")

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
        form_window.title("Actualizar libro")
        form_window.geometry("400x600")

        labels = ["Nombre", "Estado", "Genero", "Autor", "Editorial", "Fecha de publicacion", "Pagina actual", "Cantidad de paginas",
                  "Descripcion", "Clasificacion", "Puntuacion", "Wiki"]

        entries = {}
        for i, label in enumerate(labels):
            frame = tk.Frame(form_window)
            frame.pack(fill=tk.X, padx=5, pady=5)

            tk.Label(frame, text=label, width=15).pack(side=tk.LEFT)

            initial_value = values[i + 1] if i + 1 < len(values) else ""
            if label == "Fecha de publicacion":
                entry = DateEntry(frame, date_pattern='yyyy-mm-dd')
                if initial_value:
                    entry.set_date(initial_value)
                entry.pack(fill=tk.X, expand=True)
            elif label == "Estado":
                entry = ttk.Combobox(frame, values=["Para leer", "Leido", "Sin leer", "En pausa"])
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
                if label == "Fecha de publicacion":
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
                self.peliculaController.actualizar(values[0], *datos)
                form_window.destroy()
                self.refrescar_tabla()
                messagebox.showinfo("Éxito", "El libro se ha actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar el libro: {e}")

        boton_enviar = tk.Button(form_window, text="Actualizar", command=enviar_datos)
        boton_enviar.pack(pady=10)

    def crear_vista_lateral(self, frame):
        frame.config(width=400, height=600, padx=20, pady=20)
        label_menu = ttk.Label(frame, text="Menú", font=("Helvetica", 20), style="TLabel")
        label_menu.pack(pady=20)

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

    def crear_tabla_vista(self, frame):
        tk.Label(frame, text="LIBROS").pack()

        estados = ["TODOS" ,"Para leer", "Leido", "Sin leer", "En pausa"]

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
        for estado in estados:
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

        columnas = ["ID", "Nombre", "Estado", "Genero", "Autor", "Editorial", "Fecha de publicacion", "Pagina actual", "Cantidad de paginas",
                  "Descripcion", "Clasificacion", "Puntuacion", "Wiki"]
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
            self.treeview_tabla.heading(col, text=col)
        self.treeview_tabla.pack(fill=tk.BOTH, expand=True)

        h_scroll.pack(side=tk.TOP, fill=tk.X)

        self.listar_libros_en_tabla()

        # Agregar menú contextual
        self.popup_menu = tk.Menu(self.ventana, tearoff=0)
        self.popup_menu.add_command(label="Agregar", command=self.agregar_a_la_tabla)
        self.popup_menu.add_command(label="Modificar", command=self.modificar_en_tabla)
        self.popup_menu.add_command(label="Eliminar", command=self.eliminar_de_la_tabla)
        self.treeview_tabla.bind("<Button-3>", self.mostrar_menu_contextual)
        self.treeview_tabla.bind("<Double-1>", self.mostrar_info_libro)

if __name__ == "__main__":
    VistaLibro()