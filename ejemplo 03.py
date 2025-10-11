class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura)

    def perimetro(self):
        return (self.base*2 + self.altura*2)

operacion_area = Rectangulo(5,6)
operacion_perimetro = Rectangulo(5,6)

print("El area es ",operacion_area.area())

print("El perimetro es ",operacion_perimetro.perimetro())
