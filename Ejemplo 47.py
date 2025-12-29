import tkinter as tk
from tkinter import messagebox
from typing import TypeVar, Generic

T = TypeVar('T', int, float)

# ==========================================================
#             CLASE CALCULADORA GENÉRICA
# ==========================================================
class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

    def sumar(self): return self.a + self.b
    def restar(self): return self.a - self.b
    def multiplicar(self): return self.a * self.b
    
    def dividir(self):
        if self.b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return self.a / self.b


# ==========================================================
#                 APLICACIÓN INFANTIL
# ==========================================================
class CalculadoraKids:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Mágica para Niños ✨")
        self.root.geometry("470x640")
        self.root.config(bg="#FFF4D9")  # fondo suave pastel

        self.crear_ui()

    # -------------------------------------------------------
    #               INTERFAZ PRINCIPAL
    # -------------------------------------------------------
    def crear_ui(self):

        self.personaje = tk.Label(self.root, text="🧸",
                                  font=("Comic Sans MS", 80),
                                  bg="#FFF4D9")
        self.personaje.pack(pady=10)

        self.mensaje = tk.Label(self.root, text="¡Hola! Soy Teddy 🤎\n¡Vamos a jugar con números!",
                                font=("Comic Sans MS", 18, "bold"),
                                fg="#FF7A5A", bg="#FFF4D9")
        self.mensaje.pack()

        self.entrada1 = tk.Entry(self.root, font=("Comic Sans MS", 22),
                                 justify="center", width=10)
        self.entrada1.pack(pady=10)

        self.entrada2 = tk.Entry(self.root, font=("Comic Sans MS", 22),
                                 justify="center", width=10)
        self.entrada2.pack(pady=10)

        self.resultado = tk.Label(self.root, text="✨ Resultado aquí ✨",
                                  font=("Comic Sans MS", 24, "bold"),
                                  fg="#4A7B9D", bg="#FFF4D9")
        self.resultado.pack(pady=15)

        # Botones de colores infantiles
        frame = tk.Frame(self.root, bg="#FFF4D9")
        frame.pack(pady=10)

        botones = [
            ("➕", "#FFA8A8", self.sumar),
            ("➖", "#FFD59E", self.restar),
            ("✖", "#B8FFB3", self.multiplicar),
            ("➗", "#A7D8FF", self.dividir)
        ]

        for simbolo, color, comando in botones:
            btn = tk.Button(frame, text=simbolo,
                            font=("Comic Sans MS", 26, "bold"),
                            width=4, height=1,
                            bg=color, activebackground="#FFFFFF",
                            command=lambda c=comando, s=simbolo: self.animar(s, c))
            btn.pack(side="left", padx=10)

        # Botón limpiar
        self.btn_limpiar = tk.Button(self.root, text="🧹 Limpiar",
                                     font=("Comic Sans MS", 18, "bold"),
                                     bg="#FFEB99",
                                     command=self.limpiar)
        self.btn_limpiar.pack(pady=20)

    # -------------------------------------------------------
    #                   ANIMACIÓN Y MENSAJES
    # -------------------------------------------------------
    def animar(self, simbolo, accion):

        # Pequeña animación visual
        self.mensaje.config(text=f"Teddy vio que usaste {simbolo} 😄",
                            fg="#FF6A3D")

        # Ejecutar operación
        accion()

        # Restaurar mensaje
        self.root.after(900, lambda: self.mensaje.config(
            text="¡Vamos a jugar con números!",
            fg="#FF7A5A"
        ))

    # -------------------------------------------------------
    #          LEER VALORES Y OPERACIONES
    # -------------------------------------------------------
    def obtener(self):
        try:
            a = float(self.entrada1.get())
            b = float(self.entrada2.get())
            return a, b
        except:
            self.personaje.config(text="😢")
            self.mensaje.config(text="Oh oh... eso no es un número",
                                fg="#FF0000")
            return None

    def mostrar(self, valor):
        self.personaje.config(text="😀")
        self.resultado.config(text=f"🎉 Resultado: {valor}", fg="#4A7B9D")

    def sumar(self):
        datos = self.obtener()
        if datos:
            cal = Calculadora(*datos)
            self.mostrar(cal.sumar())

    def restar(self):
        datos = self.obtener()
        if datos:
            cal = Calculadora(*datos)
            self.mostrar(cal.restar())

    def multiplicar(self):
        datos = self.obtener()
        if datos:
            cal = Calculadora(*datos)
            self.mostrar(cal.multiplicar())

    def dividir(self):
        datos = self.obtener()
        if datos:
            try:
                cal = Calculadora(*datos)
                self.mostrar(cal.dividir())
            except ZeroDivisionError:
                self.personaje.config(text="😢")
                self.mensaje.config(text="No se puede dividir entre 0 🥺",
                                    fg="#FF0000")

    # -------------------------------------------------------
    #                LIMPIAR CAMPOS
    # -------------------------------------------------------
    def limpiar(self):
        self.personaje.config(text="🧸")
        self.mensaje.config(text="¡Todo limpio! 😊",
                            fg="#7E57C2")
        self.entrada1.delete(0, tk.END)
        self.entrada2.delete(0, tk.END)
        self.resultado.config(text="✨ Resultado aquí ✨")



# -----------------------------------------------------------
#                       MAIN
# -----------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraKids(root)
    root.mainloop()
