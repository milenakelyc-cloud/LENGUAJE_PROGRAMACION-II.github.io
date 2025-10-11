class leerNumero:
    def __init__(self,numero):
        self.numero = numero

    def Rango_Numero(self):
        if 1 <= self.numero <= 10:
            print(f"El numero {self.numero} esta dentro de los 10 primeros")
        elif self.numero < 1:
            diferencia = 0 - self.numero
            print(f"El numero {self.numero} es {diferencia} menos que 1")
        else:
            diferencia = self.numero - 10
            print(f"El numero {self.numero} es {diferencia} mas que 10")

def main():
    valor = int(input("Ingresa un numero del 1 al 10: "))
    numero = leerNumero(valor)
    numero.Rango_Numero()
if __name__=="__main__":
    main()
