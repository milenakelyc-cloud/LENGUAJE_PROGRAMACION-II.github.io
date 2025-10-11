class Operaciones:
    def Sumar(self,a,b,c = None):
        if c is not None:
            return a+b+c
        else:
            return a+b
operacion1 = Operaciones()
operacion2 = Operaciones()

print("Suma con dos numeros",operacion1.sumar(5,7))
print("Suma con tres numeros",operacion2.sumar(1,2,3))
