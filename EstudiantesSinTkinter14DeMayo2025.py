estudiantes = {}
contador = 1

def guardar_estudiante():
    global contador
    nombre = input("Nombre: ")
    while True:
        try:
            calificacion = float(input("Calificación: "))
            break
        except ValueError:
            print("Calificación inválida. Usa un número.")
    sexo = input("Sexo (M/F): ")

    clave = f"est{contador}"
    estudiantes[clave] = {
        "nombre": nombre,
        "calificacion": calificacion,
        "sexo": sexo
    }

    contador += 1

    if contador > 4:
        print("Ya ingresaste 3 estudiantes. Presiona Enter para mostrarlos.")
        input()
        mostrar_estudiantes()
        return

def mostrar_estudiantes():
    print("\nEstudiantes:")
    for i, est in enumerate(estudiantes.values(), start=1):
        print(f"{i}. Nombre: {est['nombre']}, Calificación: {est['calificacion']}, Sexo: {est['sexo']}")

while contador <= 3:
    guardar_estudiante()
