class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def respomde(self):
        print(f"Hola {self.nombre}")

persona1 = Persona("Carlos")
persona1.saludar()

persona2 = Persona("maria")
persona2.respomde()
