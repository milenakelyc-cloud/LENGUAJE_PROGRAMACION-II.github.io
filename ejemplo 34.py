import math
class Circulo:
    def __init__(self,radio):
        self.radio = radio
        print("Objeto circulo creado")

    def calcular_area(self):
        area = math.pi*self.radio**2
        return area

radio_usuario = float(input("Ingrese la radio del circulo: "))

circulo = Circulo(radio_usuario)
resultado = circulo.calcular_area()
print(f"El area del circulo es {resultado}")

del circulo

try:
    #circulo.calcular_area()
    print(circulo)
except NameError:
    print("El objeto ya no existe")
