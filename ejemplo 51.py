# Principio S: 
class CalculadoraFibonacci:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método a calcular")

# Principio O y L
class SerieFibonacci(CalculadoraFibonacci):
    def __init__(self, cantidad):  
        self.cantidad = cantidad

    def calcular(self):
        if self.cantidad <= 0:
            return []
        elif self.cantidad == 1:
            return [0]
        
        fibonacci = [0, 1]
        for i in range(2, self.cantidad):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        return fibonacci

fibonacci = SerieFibonacci(10)
resultado = fibonacci.calcular()
print(f"La serie de Fibonacci es: {resultado}")