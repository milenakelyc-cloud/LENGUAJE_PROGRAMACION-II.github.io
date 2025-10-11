class Coche:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_info(self):
        print(f"Coche:{self.marca} {self.modelo} {self.color}")

    def arrancar(self):
        print(f"Coche {self.marca} {self.modelo} ha arrancado ")

#Solicitar daros al usuario
marca = input("Ingrese la marca del coche")
modelo = input("Ingrese el modelo del auto")
color = input("Ingrese el color del coche")
        
#crear un objeto
        
mi_coche = Coche(marca, modelo, color)

#Usar los metodos

mi_coche.mostrar_info()
mi_coche.arrancar()
