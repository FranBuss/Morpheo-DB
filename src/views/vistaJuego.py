import tkinter as tk
from tkinter import ttk, messagebox
from src.controllers.JuegoController import JuegoController

class VistaJuego:

    def __init__(self):
        self.juegoController = JuegoController()
        self.ventana = tk.Tk()
        self.treeview_arbol = None
        self.treeview_tabla = None
        self.entry_busqueda = None
        self.configurar_interfaz()

    def agregar_al_arbol(self):
        item = f"Elemento {len(self.treeview_arbol.get_children()) + 1}"
        self.treeview_arbol.insert("", "end", text=item)

    def eliminar_del_arbol(self):
        selected_item = self.treeview_arbol.selection()
        if selected_item:
            self.treeview_arbol.delete(selected_item)
        else:
            messagebox.showwarning("Atenti!", "Seleccioná un elemento para eliminar.")

    def agregar_a_la_tabla(self):
        self.mostrar_formulario_agregar()

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
            self.juegoController.eliminar_juego(game_id)  # Llama a un método para eliminar el juego en el controlador
            self.treeview_tabla.delete(selected_item)  # Elimina de la vista
            messagebox.showinfo("Éxito", "El juego se ha eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el juego: {e}")

    def buscar_en_tabla(self):
        query = self.entry_busqueda.get().lower()
        for row in self.treeview_tabla.get_children():
            values = self.treeview_tabla.item(row, "values")
            if query in " ".join(values).lower():
                self.treeview_tabla.selection_set(row)
                self.treeview_tabla.see(row)
                return
        messagebox.showinfo("Búsqueda", f"No se encontró '{query}' en la tabla.")

    def refrescar_tabla(self):
        # Limpiar todos los elementos del Treeview
        for item in self.treeview_tabla.get_children():
            self.treeview_tabla.delete(item)
        # Volver a listar juegos
        self.listar_juegos_en_tabla()

    def listar_juegos_en_tabla(self):
        juegos = self.juegoController.listar_juegos()
        if juegos is None:
            juegos = []  # Aseguramos que juegos no sea None
        for juego in juegos:
            self.treeview_tabla.insert("", "end", values=juego[:13])

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
            entry = tk.Entry(frame)
            entry.pack(fill=tk.X, expand=True)
            entries[label] = entry

        def enviar_datos():
            datos = [entry.get() if entry.get() else "" for entry in entries.values()]
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

    def configurar_interfaz(self):
        self.ventana.title("MorpheoDB")
        self.ventana.geometry("800x600")

        frame_izquierda = self.crear_frame(self.ventana, side=tk.LEFT)
        self.crear_arbol_vista(frame_izquierda)

        frame_derecha = self.crear_frame(self.ventana, side=tk.RIGHT)
        self.crear_tabla_vista(frame_derecha)

        self.ventana.mainloop()

    def crear_frame(self, parent, side):
        frame = tk.Frame(parent)
        frame.pack(side=side, fill=tk.BOTH, expand=True, padx=10, pady=10)
        return frame

    def crear_arbol_vista(self, frame):
        tk.Label(frame, text="Mis listas").pack()
        self.treeview_arbol = ttk.Treeview(frame)
        self.treeview_arbol.pack(fill=tk.BOTH, expand=True)

        frame_botones_arbol = tk.Frame(frame)
        frame_botones_arbol.pack(pady=5)
        tk.Button(frame_botones_arbol, text="Agregar", command=self.agregar_al_arbol).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones_arbol, text="Eliminar", command=self.eliminar_del_arbol).grid(row=0, column=1, padx=5)

    def crear_tabla_vista(self, frame):
        tk.Label(frame, text="Contenido de mi lista").pack()

        frame_busqueda = tk.Frame(frame)
        frame_busqueda.pack(fill=tk.X, pady=5)

        self.entry_busqueda = tk.Entry(frame_busqueda)
        self.entry_busqueda.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        tk.Button(frame_busqueda, text="Buscar", command=self.buscar_en_tabla).pack(side=tk.RIGHT, padx=5)

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

        self.listar_juegos_en_tabla()

"""
vista_juego = VistaJuego()
frame_botones_tabla = tk.Frame(frame_derecha)
frame_botones_tabla.pack(pady=5)

boton_agregar_tabla = tk.Button(frame_botones_tabla, text="Agregar", command=agregarALaTabla)
boton_agregar_tabla.grid(row=0, column=0, padx=5)

boton_eliminar_tabla = tk.Button(frame_botones_tabla, text="Eliminar", command=eliminarDeLaTabla)
boton_eliminar_tabla.grid(row=0, column=1, padx=5)
"""

# Loop
if __name__ == "__main__":
    VistaJuego()
    