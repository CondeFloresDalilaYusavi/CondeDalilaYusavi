import tkinter as tk
from tkinter import messagebox

def limpiar_area():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

def area_circulo():
    limpiar_area()
    tk.Label(area_dinamica, text="Area del Circulo", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Radio:").pack()
    entrada_radio = tk.Entry(area_dinamica)
    entrada_radio.pack()

    def calcular_area():
        try:
            radio = float(entrada_radio.get())
            area = 3.1416 * radio ** 2
            messagebox.showinfo("Resultado", f"Area del círculo: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa un nUmero valido")

    tk.Button(area_dinamica, text="Calcular Area", command=calcular_area).pack(pady=10)

def area_cuadrado():
    limpiar_area()
    tk.Label(area_dinamica, text="Area del Cuadrado", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Lado:").pack()
    entrada_lado = tk.Entry(area_dinamica)
    entrada_lado.pack()

    def calcular_area():
        try:
            lado = float(entrada_lado.get())
            area = lado ** 2
            messagebox.showinfo("Resultado", f"Area del cuadrado: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa un numero valido")

    tk.Button(area_dinamica, text="Calcular Area", command=calcular_area).pack(pady=10)

def area_rectangulo():
    limpiar_area()
    tk.Label(area_dinamica, text="Area del Rectangulo", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Base:").pack()
    entrada_base = tk.Entry(area_dinamica)
    entrada_base.pack()

    tk.Label(area_dinamica, text="Altura:").pack()
    entrada_altura = tk.Entry(area_dinamica)
    entrada_altura.pack()

    def calcular_area():
        try:
            base = float(entrada_base.get())
            altura = float(entrada_altura.get())
            area = base * altura
            messagebox.showinfo("Resultado", f"Area del rectangulo: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa numeros validos")

    tk.Button(area_dinamica, text="Calcular Area", command=calcular_area).pack(pady=10)

def area_triangulo():
    limpiar_area()
    tk.Label(area_dinamica, text="Area del Triangulo", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Base:").pack()
    entrada_base = tk.Entry(area_dinamica)
    entrada_base.pack()

    tk.Label(area_dinamica, text="Altura:").pack()
    entrada_altura = tk.Entry(area_dinamica)
    entrada_altura.pack()

    def calcular_area():
        try:
            base = float(entrada_base.get())
            altura = float(entrada_altura.get())
            area = (base * altura) / 2
            messagebox.showinfo("Resultado", f"Area del triangulo: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa numeros validos")

    tk.Button(area_dinamica, text="Calcular Area", command=calcular_area).pack(pady=10)

ventana_principal = tk.Tk()
ventana_principal.title("Calculadora de Areas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=140)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Circulo", command=area_circulo, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Cuadrado", command=area_cuadrado, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Rectangulo", command=area_rectangulo, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Triangulo", command=area_triangulo, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

area_circulo()

ventana_principal.mainloop()
