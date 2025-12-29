import math
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# ================== MODELO ==================
class FiguraGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Circulo(FiguraGeometrica):

    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(FiguraGeometrica):

    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y altura deben ser mayores que cero")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


# ================== INTERFAZ ==================
def calcular_circulo():
    try:
        radio = float(entry_radio.get())
        c = Circulo(radio)
        lbl_resultado_circulo.config(
            text=f"Área: {c.calcular_area():.2f}\nPerímetro: {c.calcular_perimetro():.2f}"
        )
    except:
        messagebox.showerror("Error", "Ingrese un radio válido")


def calcular_rectangulo():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        r = Rectangulo(base, altura)
        lbl_resultado_rectangulo.config(
            text=f"Área: {r.calcular_area():.2f}\nPerímetro: {r.calcular_perimetro():.2f}"
        )
    except:
        messagebox.showerror("Error", "Ingrese valores válidos")


# ================== VENTANA ==================
ventana = tk.Tk()
ventana.title("Figuras Geométricas - SOLID")
ventana.geometry("850x500")
ventana.config(bg="#1e1e2f")

# ================== TITULO ==================
titulo = tk.Label(
    ventana,
    text="Cálculo de Figuras Geométricas",
    font=("Arial Black", 20),
    bg="#1e1e2f",
    fg="#f9d342"
)
titulo.pack(pady=10)

# ================== CONTENEDOR ==================
frame_principal = tk.Frame(ventana, bg="#1e1e2f")
frame_principal.pack()

# ================== CIRCULO ==================
frame_circulo = tk.Frame(frame_principal, bg="#2a2a40", padx=20, pady=20)
frame_circulo.grid(row=0, column=0, padx=20)

tk.Label(
    frame_circulo,
    text="CÍRCULO",
    font=("Arial Black", 14),
    bg="#2a2a40",
    fg="#4dd0e1"
).pack()

# Imagen círculo
try:
    img_circulo = tk.PhotoImage(file="circulo.png")
    tk.Label(frame_circulo, image=img_circulo, bg="#2a2a40").pack(pady=5)
except:
    pass

tk.Label(frame_circulo, text="Radio:", bg="#2a2a40", fg="white").pack()
entry_radio = tk.Entry(frame_circulo, justify="center")
entry_radio.pack(pady=5)

tk.Button(
    frame_circulo,
    text="Calcular",
    command=calcular_circulo,
    bg="#4dd0e1",
    fg="black",
    font=("Arial", 10, "bold")
).pack(pady=5)

lbl_resultado_circulo = tk.Label(
    frame_circulo,
    text="Área:\nPerímetro:",
    bg="#2a2a40",
    fg="#ffffff",
    font=("Arial", 11)
)
lbl_resultado_circulo.pack(pady=5)

# ================== RECTÁNGULO ==================
frame_rectangulo = tk.Frame(frame_principal, bg="#2a2a40", padx=20, pady=20)
frame_rectangulo.grid(row=0, column=1, padx=20)

tk.Label(
    frame_rectangulo,
    text="RECTÁNGULO",
    font=("Arial Black", 14),
    bg="#2a2a40",
    fg="#ff8a65"
).pack()

# Imagen rectángulo
try:
    img_rectangulo = tk.PhotoImage(file="rectangulo.png")
    tk.Label(frame_rectangulo, image=img_rectangulo, bg="#2a2a40").pack(pady=5)
except:
    pass

tk.Label(frame_rectangulo, text="Base:", bg="#2a2a40", fg="white").pack()
entry_base = tk.Entry(frame_rectangulo, justify="center")
entry_base.pack(pady=3)

tk.Label(frame_rectangulo, text="Altura:", bg="#2a2a40", fg="white").pack()
entry_altura = tk.Entry(frame_rectangulo, justify="center")
entry_altura.pack(pady=3)

tk.Button(
    frame_rectangulo,
    text="Calcular",
    command=calcular_rectangulo,
    bg="#ff8a65",
    fg="black",
    font=("Arial", 10, "bold")
).pack(pady=5)

lbl_resultado_rectangulo = tk.Label(
    frame_rectangulo,
    text="Área:\nPerímetro:",
    bg="#2a2a40",
    fg="#ffffff",
    font=("Arial", 11)
)
lbl_resultado_rectangulo.pack(pady=5)

# ================== PIE ==================
footer = tk.Label(
    ventana,
    text="Programación Orientada a Objetos – Principios SOLID",
    bg="#1e1e2f",
    fg="#aaaaaa",
    font=("Arial", 9)
)
footer.pack(pady=10)

ventana.mainloop()
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod
import math
from PIL import Image, ImageTk


# ================== MODELO ==================
class FiguraGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Circulo(FiguraGeometrica):

    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(FiguraGeometrica):

    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser mayores que cero")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


# ================== VISTA (TKINTER) ==================
ventana = tk.Tk()
ventana.title("Figuras Geométricas")
ventana.geometry("700x550")
ventana.configure(bg="#E3F2FD")


# ---------- TÍTULO ----------
titulo = tk.Label(
    ventana,
    text="Cálculo de Áreas y Perímetros",
    font=("Arial", 20, "bold"),
    bg="#1E88E5",
    fg="white",
    pady=10
)
titulo.pack(fill="x")


# ---------- MARCO PRINCIPAL ----------
frame = tk.Frame(ventana, bg="#E3F2FD")
frame.pack(pady=20)


# ---------- IMÁGENES ----------
img_circulo = Image.open("circulo.png").resize((150, 150))
img_circulo = ImageTk.PhotoImage(img_circulo)

img_rectangulo = Image.open("rectangulo.png").resize((150, 150))
img_rectangulo = ImageTk.PhotoImage(img_rectangulo)


label_img_circulo = tk.Label(frame, image=img_circulo, bg="#E3F2FD")
label_img_circulo.grid(row=0, column=0, padx=30)

label_img_rectangulo = tk.Label(frame, image=img_rectangulo, bg="#E3F2FD")
label_img_rectangulo.grid(row=0, column=1, padx=30)


# ---------- ENTRADAS ----------
tk.Label(frame, text="Radio del círculo:", bg="#E3F2FD", font=("Arial", 11)).grid(row=1, column=0)
entry_radio = tk.Entry(frame, font=("Arial", 11))
entry_radio.grid(row=2, column=0)

tk.Label(frame, text="Base del rectángulo:", bg="#E3F2FD", font=("Arial", 11)).grid(row=1, column=1)
entry_base = tk.Entry(frame, font=("Arial", 11))
entry_base.grid(row=2, column=1)

tk.Label(frame, text="Altura del rectángulo:", bg="#E3F2FD", font=("Arial", 11)).grid(row=3, column=1)
entry_altura = tk.Entry(frame, font=("Arial", 11))
entry_altura.grid(row=4, column=1)


# ---------- RESULTADOS ----------
resultado = tk.Label(
    ventana,
    text="Resultados aparecerán aquí",
    font=("Arial", 12),
    bg="#BBDEFB",
    fg="#0D47A1",
    pady=10
)
resultado.pack(fill="x", padx=40, pady=15)


# ---------- FUNCIONES ----------
def calcular():
    try:
        radio = float(entry_radio.get())
        base = float(entry_base.get())
        altura = float(entry_altura.get())

        c = Circulo(radio)
        r = Rectangulo(base, altura)

        texto = (
            f"CÍRCULO\n"
            f"Área: {c.calcular_area():.2f}\n"
            f"Perímetro: {c.calcular_perimetro():.2f}\n\n"
            f"RECTÁNGULO\n"
            f"Área: {r.calcular_area():.2f}\n"
            f"Perímetro: {r.calcular_perimetro():.2f}"
        )

        resultado.config(text=texto)

    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos y mayores que cero")


# ---------- BOTÓN ----------
btn = tk.Button(
    ventana,
    text="Calcular",
    command=calcular,
    bg="#43A047",
    fg="white",
    font=("Arial", 14, "bold"),
    width=15
)
btn.pack(pady=15)


ventana.mainloop()
