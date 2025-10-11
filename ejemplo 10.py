class TabladeMultiplicar:
    def __init__(self,numero):
        self.numero = numero

    def generarTabla(self):
        for i in range(1, 11):
            resultado = self.numero*i
            print(f"{self.numero} x {i} = {resultado}")

def main():
    numero = int(input("Ingrese un numero "))
    miTabla = TabladeMultiplicar(numero)
    miTabla.generarTabla()

if __name__=="__main__":
    main()
