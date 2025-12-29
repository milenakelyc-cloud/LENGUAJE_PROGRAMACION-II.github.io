import math

# Principio S
# Principio o
# Principio L
class Operacion:
    def calcular(self, a, b):
        pass


class Suma(Operacion):
    def calcular(self, a, b):
        return a + b


class Resta(Operacion):
    def calcular(self, a, b):
        return a - b


class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b


class Division(Operacion):
    def calcular(self, a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b


class Potencia(Operacion):
    def calcular(self, a, b):
        return math.pow(a, b)


class Calculadora:
    def __init__(self):
        self.operaciones = {
            '+': Suma(),
            '-': Resta(),
            '*': Multiplicacion(),
            '/': Division()
        }

    def agregar_operacion(self, simbolo, operacion):
        self.operaciones[simbolo] = operacion

    def calcular(self, a, b, operador):
        if operador in self.operaciones:
            resultado = self.operaciones[operador].calcular(a, b)
            operacion_nombre = self._obtener_nombre(operador)
            return f"La {operacion_nombre} sale: {resultado}"
        return "Operador no válido"

    def _obtener_nombre(self, operador):
        nombres = {
            '+': 'suma',
            '-': 'resta',
            '*': 'multiplicación',
            '/': 'división',
            '^': 'potencia'
        }
        return nombres.get(operador, 'operación')

calc = Calculadora()
calc.agregar_operacion('^', Potencia())

while True:
    print("\n---> CALCULADORA <---")
    print("Operaciones disponibles: +  -  *  /  ^")
    print("Escriba 'salir' para terminar")

    operador = input("Ingrese el operador: ")

    if operador.lower() == "salir":
        print("Programa finalizado 👋")
        break

    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Debe ingresar números válidos")
        continue

    resultado = calc.calcular(a, b, operador)
    print(resultado)
