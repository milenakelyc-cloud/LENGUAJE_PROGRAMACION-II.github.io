class Calculadora:
    def sumar(self,a,b):
        self.a =a
        self.b = b
        return self.a + self.b

calcular = Calculadora()
suma = calcular.sumar(1,3)

print(f"La suma de los parametros {calcular.a} y {calcular.b} es {suma}")
