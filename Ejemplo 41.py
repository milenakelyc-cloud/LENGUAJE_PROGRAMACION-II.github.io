class Departamento:
    def __init__(self,nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self,nombre):
        self.nombre = nombre
        self.departamentos = []
        
    def agregar_departamento(self,departamento):
        self.departamentos.append(departamento)

dep1 = Departamento("Ingenieria Estadistica")
dep2 = Departamento("Informatica")

uni = Universidad("Universidad Nacional del Altiplano")
uni.agregar_departamento(dep1)
uni.agregar_departamento(dep2)

uni.agregar_departamento()
