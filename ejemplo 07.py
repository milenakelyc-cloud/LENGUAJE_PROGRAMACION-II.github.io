class Empleado:
    def __init__(self,Nombre,Cargo,Salario):
        self.Nombre = Nombre
        self.Cargo = Cargo
        self.Salario = Salario

    def AplicarAumento(self):
        if self.Cargo == "Gerente":
            porcentaje = 0.1
        elif self.Cargo == "Supervisor":
            porcentaje = 0.07
        elif self.Cargo == "Operario":
            porcentaje = 0.05
        else:
            porcentaje = 0

        NuevoSalario = self.Salario *(1 + porcentaje)
        return NuevoSalario
    
Nombre = float(input("Ingrese Nombre"))
Cargo = float(input("Ingrese Cargo"))
Salarion = float(input("Ingrese Salario"))

nuevo = self.Salario *(1 + porcentaje)
    
print(f"{emp.Nombre} {emp.Cargo}: salario nuevo = {nuevo:2f}")
