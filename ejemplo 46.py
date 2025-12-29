from typing import TypeVar
import math

T = TypeVar('T', int, float)

class TrianguloRectangulo:
    def __init__(self, a: T, b: T):
        self.a = a 
        self.b = b
        self.h = math.sqrt(a**2 + b**2)
        
    def calcular_hipotenusa(self) -> float:
        return self.h
    
    def calcular_area(self) -> float:
        return (self.a * self.b) / 2
    
    def calcular_perimetro(self) -> float:
        return self.a + self.b + self.h
        
def main():
    try:
        a = float(input("Ingrese el valor de A: "))
        b = float(input("Ingrese el valor de B: "))
        
        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser numeros positivos")
        
        triangulo = TrianguloRectangulo(a, b)
        
        print(f"La hipotenusa es: {triangulo.calcular_hipotenusa():.6f}")
        print(f"El area es: {triangulo.calcular_area():.6f}")
        print(f"El perimetro es: {triangulo.calcular_perimetro():.6f}")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()