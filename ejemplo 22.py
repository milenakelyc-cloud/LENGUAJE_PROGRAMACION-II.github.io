class Rectangulo:
    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def set_base(self,nueva_base):
        if nueva_base > 0:
            self.__base = nueva_base
        else:
            print("base no valida")

    def set_altura(self,nueva_altura):
        if nueva_altura > 0:
            self.__altura = nueva_altura
        else:
            print("altura no valida")

    def calcular_area(self):
            return self.__base*self.__altura

    def calcular_perimetro(self):
            return 2*self.__base+2*self.__altura

rectangulo = Rectangulo(5,4)
print("El area del rectangulo",rectangulo.calcular_area())
print("El perimetro del rectangulo",rectangulo.calcular_perimetro())
