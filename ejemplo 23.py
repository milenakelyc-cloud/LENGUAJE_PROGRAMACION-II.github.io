class Calculadora:
    def __init__(self, numero1, numero2):
        self.__numero1 = numero1   
        self.__numero2 = numero2

    def get_numero1(self):
        return self.__numero1

    def get_numero2(self):
        return self.__numero2

    def set_numero1(self, nuevo_numero1):
        self.__numero1 = nuevo_numero1

    def set_numero2(self, nuevo_numero2):
        self.__numero2 = nuevo_numero2

    def sumar(self):
        return self.__numero1 + self.__numero2

    def restar(self):
        return self.__numero1 - self.__numero2

    def multiplicar(self):
        return self.__numero1 * self.__numero2

    def dividir(self):
        if self.__numero2 != 0:
            return self.__numero1 / self.__numero2
        else:
            return "Error: División entre 0"

calculadora = Calculadora(2, 5)

print("Número 1:", calculadora.get_numero1())
print("Número 2:", calculadora.get_numero2())

print("Suma:", calculadora.sumar())
print("Resta:", calculadora.restar())
print("Multiplicación:", calculadora.multiplicar())
print("División:", calculadora.dividir())

calculadora.set_numero1(10)
calculadora.set_numero2(4)

print("\nNuevos valores:")
print("Número 1:", calculadora.get_numero1())
print("Número 2:", calculadora.get_numero2())
print("Suma:", calculadora.sumar())



