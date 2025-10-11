import tkinter as tk
from tkinter import messagebox
import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre} | Edad: {self.edad} | Carrera: {self.carrera}"

    def __del__(self):
        print(f"Estudiante eliminado: {self.nombre}")

# Lista de estudiantes
grupo = []

# Función para agregar estudiante
def agregar_estudiante():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    carrera = entry_carrera.get()

    if not nombre or not edad or not carrera:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    try:
        edad = int(edad)
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número")
        return

    estudiante = Estudiante(nombre, edad, carrera)
    grupo.append(estudiante)

    text_salida.insert(tk.END, estudiante.mostrar_informacion() + "\n")

    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)

# Función para limpiar estudiantes
def limpiar_estudiantes():
    grupo.clear()
    gc.collect()
    text_salida.delete("1.0", tk.END)
    messagebox.showinfo("Información", "Lista de estudiantes eliminada")

# ------------------- INTERFAZ -------------------
ventana = tk.Tk()
ventana.title("Registro de Estudiantes")

# Etiquetas y cajas de texto
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Carrera:").grid(row=2, column=0, padx=5, pady=5)
entry_carrera = tk.Entry(ventana)
entry_carrera.grid(row=2, column=1, padx=5, pady=5)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar Estudiante", command=agregar_estudiante)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

btn_limpiar = tk.Button(ventana, text="Limpiar Estudiantes", command=limpiar_estudiantes)
btn_limpiar.grid(row=4, column=0, columnspan=2, pady=5)

# Cuadro de texto para mostrar resultados
text_salida = tk.Text(ventana, width=50, height=10)
text_salida.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
