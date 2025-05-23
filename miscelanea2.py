import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def mostrar_mensaje_bienvenida():
    # Muestra un mensaje de bienvenida en el área dinámica.
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="¡Bienvenido, Dalila Yusavi! ", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar Mensaje", command=lambda: messagebox.showinfo("Bienvenida", "Hola, yusaviii!!")).pack()

def mostrar_datos_alumno():
    # Muestra una interfaz para ingresar datos del alumno.
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Información del Alumno", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre del Alumno:").pack()
    nombre_alumno = tk.Entry(area_dinamica)
    nombre_alumno.pack(pady=5)

    tk.Label(area_dinamica, text="Selección:").pack()
    opcion_elegida = tk.StringVar(value="Opción 1")
    tk.Radiobutton(area_dinamica, text="Opción 1", variable=opcion_elegida, value="Opción 1").pack()
    tk.Radiobutton(area_dinamica, text="Opción 2", variable=opcion_elegida, value="Opción 2").pack()

    tk.Label(area_dinamica, text="Lista desplegable:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Uno", "Dos", "Tres"])
    combo.pack()
    combo.current(0)

    def guardar_datos():
        try:
            nombre = nombre_alumno.get()
            if not nombre:
                raise ValueError("El campo de nombre no puede estar vacío.")
            messagebox.showinfo("Revisión", f"Nombre: {nombre}\nSelección: {opcion_elegida.get()}\nLista: {combo.get()}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(area_dinamica, text="Guardar Datos", command=guardar_datos).pack(pady=10)


def cambiar_tema():
    # Permite al usuario cambiar el tema de color de la interfaz.
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Cambiar Tema", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    
    def aplicar_color(color):
        try:
            ventana_principal.config(bg=color)
            menu_lateral.config(bg=color)
            area_dinamica.config(bg=color)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cambiar el color: {e}")

    for color in colores:
        tk.Button(area_dinamica, text=color, bg=color, width=20, command=lambda col=color: aplicar_color(col)).pack(pady=2)


def mostrar_ayuda():
    # Muestra una sección de ayuda para el usuario.
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Ayuda", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Instrucciones:\n\n"
        "- Botón 'Mostrar Mensaje': Muestra un mensaje de bienvenida.\n"
        "- Botón 'Guardar Datos': Guarda el nombre del alumno, una selección y una opción de una lista desplegable.\n"
        "- Sección 'Cambiar Tema': Permite cambiar el color de fondo de la aplicación.\n"
        "- Para cambiar un texto, edita directamente el texto en el código fuente.\n"
        "- Para cambiar un color, usa la sección 'Cambiar Tema'."
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)


def limpiar_area_dinamica():
     # Limpia el área dinámica para mostrar una nueva interfaz.
    for widget in area_dinamica.winfo_children():
        widget.destroy()


# Creación de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para Prácticas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

# Creación del menú lateral
menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

# Creación del área dinámica
area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")


# Botones del menú lateral
tk.Button(menu_lateral, text="Inicio", command=mostrar_mensaje_bienvenida, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos Alumno", command=mostrar_datos_alumno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Cambiar Tema", command=cambiar_tema, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ayuda", command=mostrar_ayuda, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

# Mostrar la pantalla inicial
mostrar_mensaje_bienvenida()

# Iniciar el bucle principal de la aplicación
ventana_principal.mainloop()