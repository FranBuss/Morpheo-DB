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
        self.ventana.geometry("1000x600")
        self.ventana.configure(bg='white')
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
        from src.views.VistaPelicula import VistaPelicula
        self.ventana.destroy()
        VistaPelicula()

    def abrir_vista_libros(self):
        from src.views.VistaLibro import VistaLibro
        self.ventana.destroy()
        VistaLibro()

    def busqueda_por_estado(self, estado):
        juegos = self.juegoController.buscar_por_estado(estado)
        if juegos is None:
            juegos = []

        for juego in juegos:
            self.treeview_tabla.insert("", "end", values=(
                juego[0], juego[1], juego[2], juego[3], juego[4], juego[5], juego[6], juego[7], juego[8], juego[9],
                juego[10],
                juego[11], juego[12], juego[13]))

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

        game_id = values[0]  # Asumimos que el ID es el primer valor

        try:
            self.juegoController.eliminar(game_id)  # Llama a un método para eliminar el juego en el controlador
            self.treeview_tabla.delete(selected_item)  # Elimina de la vista
            messagebox.showinfo("Éxito", "El juego se ha eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el juego: {e}")

    def buscar_en_tabla(self, nombre):
        resultado = self.juegoController.buscar_por_nombre(nombre)
        if resultado:
            self.treeview_tabla.delete(*self.treeview_tabla.get_children())  # Limpiar tabla actual
            for juego in resultado:
                self.treeview_tabla.insert("", "end", values=(
                    juego[0], juego[1], juego[2], juego[3], juego[4], juego[5], juego[6], juego[7], juego[8], juego[9],
                    juego[10], juego[11], juego[12], juego[13]))
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

        for juego in juegos:
            self.treeview_tabla.insert("", "end", values=(
                juego[0], juego[1], juego[2], juego[3], juego[4], juego[5], juego[6], juego[7], juego[8], juego[9],
                juego[10],
                juego[11], juego[12], juego[13]))

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
        self.treeview_tabla = ttk.Treeview(frame, columns=columnas, show="headings")

        # Barra de scroll horizontal
        h_scroll = tk.Scrollbar(frame, orient="horizontal", command=self.treeview_tabla.xview)
        self.treeview_tabla.configure(xscrollcommand=h_scroll.set)

        for col in columnas:
            self.treeview_tabla.heading(col, text=col)
        self.treeview_tabla.pack(fill=tk.BOTH, expand=True)

        h_scroll.pack(side=tk.TOP, fill=tk.X)

        frame_botones_tabla = tk.Frame(frame)
        frame_botones_tabla.pack(pady=5)
        tk.Button(frame_botones_tabla, text="Agregar", command=self.agregar_a_la_tabla).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones_tabla, text="Eliminar", command=self.eliminar_de_la_tabla).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones_tabla, text="Modificar", command=self.modificar_en_tabla).grid(row=0, column=2, padx=5)

        self.listar_juegos_en_tabla()

        # Agregar menú contextual
        self.popup_menu = tk.Menu(self.ventana, tearoff=0)
        self.popup_menu.add_command(label="Agregar", command=self.agregar_a_la_tabla)
        self.popup_menu.add_command(label="Modificar", command=self.modificar_en_tabla)
        self.popup_menu.add_command(label="Eliminar", command=self.eliminar_de_la_tabla)
        self.treeview_tabla.bind("<Button-3>", self.mostrar_menu_contextual)


# Loop
if __name__ == "__main__":
    VistaJuego()
    