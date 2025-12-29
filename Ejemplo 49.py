import tkinter as tk
from tkinter import *
from math import pi

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras Geométricas Mágicas")
        self.root.geometry("600x650")
        self.root.config(bg="#A6E4FA")

        self.canvas = Canvas(root, width=300, height=300, bg="#FFFFFF", highlightthickness=5, highlightbackground="#FF7F50")
        self.canvas.place(x=150, y=30)

        self.lbl_titulo = Label(root, text="FIGURAS MÁGICAS ✨", font=("Comic Sans MS", 25, "bold"), bg="#A6E4FA", fg="#FF1493")
        self.lbl_titulo.place(x=150, y=340)

        self.btn_rect = Button(root, text="RECTÁNGULO 🟥", font=("Comic Sans MS", 14, "bold"),
                               bg="#FF6B6B", fg="white", width=15, command=self.mostrar_rect)
        self.btn_rect.place(x=50, y=400)

        self.btn_circ = Button(root, text="CÍRCULO 🔵", font=("Comic Sans MS", 14, "bold"),
                               bg="#4D96FF", fg="white", width=15, command=self.mostrar_circ)
        self.btn_circ.place(x=350, y=400)

        self.lbl_descripcion = Label(root, text="", font=("Comic Sans MS", 14, "italic"), bg="#A6E4FA", fg="#3A3A3A", wraplength=500)
        self.lbl_descripcion.place(x=50, y=450)

        self.lbl_resultado = Label(root, text="", font=("Comic Sans MS", 16, "bold"), bg="#A6E4FA", fg="#2B2B2B")
        self.lbl_resultado.place(x=100, y=520)

        self.carita = Label(root, text="", font=("Comic Sans MS", 30), bg="#A6E4FA")
        self.carita.place(x=260, y=560)

        self.animacion_activa = False
        self.dx = 3
        self.dy = 3

    def animar(self):
        if not self.animacion_activa:
            return
        self.canvas.move(self.figura, self.dx, self.dy)
        x1, y1, x2, y2 = self.canvas.coords(self.figura)
        if x1 <= 0 or x2 >= 300:
            self.dx *= -1
        if y1 <= 0 or y2 >= 300:
            self.dy *= -1
        self.root.after(30, self.animar)

    def mostrar_rect(self):
        self.canvas.delete("all")

        self.figura = self.canvas.create_rectangle(80, 80, 220, 160, fill="#FFB703", outline="#FB8500", width=4)

        base = 10
        altura = 5
        area = base * altura
        perimetro = 2 * (base + altura)

        self.lbl_descripcion.config(text="El rectángulo es una figura con cuatro lados. "
                                         "Tiene dos lados largos iguales llamados base y dos lados cortos llamados altura.")
        self.lbl_resultado.config(text=f"Base: {base}   |   Altura: {altura}   |   Área: {area}   |   Perímetro: {perimetro}")
        self.carita.config(text="😊")

        self.animacion_activa = True
        self.animar()

    def mostrar_circ(self):
        self.canvas.delete("all")

        self.figura = self.canvas.create_oval(80, 80, 220, 220, fill="#90E0EF", outline="#0077B6", width=4)

        radio = 7
        area = round(pi * (radio ** 2), 2)
        perimetro = round(2 * pi * radio, 2)

        self.lbl_descripcion.config(text="El círculo es una figura redonda perfecta. "
                                         "Todos sus puntos están a la misma distancia del centro, llamada radio.")
        self.lbl_resultado.config(text=f"Radio: {radio}   |   Área: {area}   |   Perímetro: {perimetro}")
        self.carita.config(text="😀")

        self.animacion_activa = True
        self.animar()


root = tk.Tk()
app = App(root)
root.mainloop()
