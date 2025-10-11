class Triangulo:
    def __init__(self,catetoa,catetob):
        self.catetoa = catetoa
        self.catetob = catetob

    def CalcularHipotenusa(self):
        Hipotenusa = (catetoa**2 + catetob**2)*1/2
        return Hipotenusa

hipotenusa = Triangulo(3,4)
hipotenusa.CalcularHipotenusa()

print("La hipotenusa es ",hipotenusa.CalcularHipotenusa())
