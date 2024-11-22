import tkinter as tk
from tkinter import ttk
#Treeview
from tkinter import messagebox
#Mensajitos
#from src.controllers.JuegoController import JuegoController

def agregarAlArbol():
    item = f"Elemento {len(treeview_arbol.get_children()) + 1}"
    treeview_arbol.insert("", "end", text=item)


def eliminarDelArbol():
    selected_item = treeview_arbol.selection()
    if selected_item:
        treeview_arbol.delete(selected_item)
    else:
        messagebox.showwarning("Atenti!", "Seleccioná un elemento para eliminar.")


def agregarALaTabla():
    item = f"Item {len(treeview_tabla.get_children()) + 1}"
    treeview_tabla.insert("", "end", values=(item, "Detalle", "Otro dato"))


def eliminarDeLaTabla():
    selected_item = treeview_tabla.selection()
    if selected_item:
        treeview_tabla.delete(selected_item)
    else:
        messagebox.showwarning("Atenti!", "Seleccioná un elemento para eliminar.")


def buscarEnTabla():
    query = entry_busqueda.get().lower()
    for row in treeview_tabla.get_children():
        values = treeview_tabla.item(row, "values")
        if query in " ".join(values).lower():
            treeview_tabla.selection_set(row)
            treeview_tabla.see(row)
            return
    messagebox.showinfo("Búsqueda", f"No se encontró '{query}' en la tabla.")


# Ventana principal
ventana = tk.Tk()
ventana.title("MorpheoDB")
ventana.geometry("800x600")

# Ventana dividida en dos secciones
frame_izquierda = tk.Frame(ventana)
frame_izquierda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

frame_derecha = tk.Frame(ventana)
frame_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Vista de árbol izquierda
label_arbol = tk.Label(frame_izquierda, text="Mis listas")
label_arbol.pack()

treeview_arbol = ttk.Treeview(frame_izquierda)
treeview_arbol.pack(fill=tk.BOTH, expand=True)

frame_botones_arbol = tk.Frame(frame_izquierda)
frame_botones_arbol.pack(pady=5)

boton_agregar_arbol = tk.Button(frame_botones_arbol, text="Agregar", command=agregarAlArbol)
boton_agregar_arbol.grid(row=0, column=0, padx=5)

boton_eliminar_arbol = tk.Button(frame_botones_arbol, text="Eliminar", command=eliminarDelArbol)
boton_eliminar_arbol.grid(row=0, column=1, padx=5)

# Tabla derecha
label_tabla = tk.Label(frame_derecha, text="Contenido de mi lista")
label_tabla.pack()

frame_busqueda = tk.Frame(frame_derecha)
frame_busqueda.pack(fill=tk.X, pady=5)

entry_busqueda = tk.Entry(frame_busqueda)
entry_busqueda.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

boton_buscar = tk.Button(frame_busqueda, text="Buscar", command=buscarEnTabla)
boton_buscar.pack(side=tk.RIGHT, padx=5)

treeview_tabla = ttk.Treeview(frame_derecha, columns=("Columna_1", "Columna_2", "Columna_3", "Columna_4", "Columna_5", "Columna_6", "Columna_7", "Columna_8", "Columna_9", "Columna_10", "Columna_11", "Columna_12", "Columna_13"), show="headings")
treeview_tabla.pack(fill=tk.BOTH, expand=True)

# Encabezado de la tabla
treeview_tabla.heading("Columna_1", text="Nombre")
treeview_tabla.heading("Columna_2", text="Género")
treeview_tabla.heading("Columna_3", text="Fecha de Salida")
treeview_tabla.heading("Columna_4", text="Estado")
treeview_tabla.heading("Columna_5", text="Desarrollador")
treeview_tabla.heading("Columna_6", text="Distribuidor")
treeview_tabla.heading("Columna_7", text="Plataforma")
treeview_tabla.heading("Columna_8", text="Temática")
treeview_tabla.heading("Columna_9", text="Modo de Juego")
treeview_tabla.heading("Columna_10", text="Descripción")
treeview_tabla.heading("Columna_11", text="Comentario")
treeview_tabla.heading("Columna_12", text="Clasificación")
treeview_tabla.heading("Columna_13", text="Puntuación")

frame_botones_tabla = tk.Frame(frame_derecha)
frame_botones_tabla.pack(pady=5)

boton_agregar_tabla = tk.Button(frame_botones_tabla, text="Agregar", command=agregarALaTabla)
boton_agregar_tabla.grid(row=0, column=0, padx=5)

boton_eliminar_tabla = tk.Button(frame_botones_tabla, text="Eliminar", command=eliminarDeLaTabla)
boton_eliminar_tabla.grid(row=0, column=1, padx=5)

# Loop
ventana.mainloop()

