import tkinter as tk
from tkinter import messagebox

def mostrar_saludo():
   
    nombre = entry_nombre.get()
    try:
        edad = int(entry_edad.get())
        messagebox.showinfo("Saludo", f"Buenos días {nombre}, tienes {edad} años.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una edad válida (número entero).")


ventana_principal = tk.Tk()
ventana_principal.title("Información del Usuario")

label_nombre = tk.Label(ventana_principal, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(ventana_principal)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

label_edad = tk.Label(ventana_principal, text="Edad:")
label_edad.grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry(ventana_principal)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

boton_enviar = tk.Button(ventana_principal, text="Enviar", command=mostrar_saludo)
boton_enviar.grid(row=2, column=0, columnspan=2, pady=10)

ventana_principal.mainloop()