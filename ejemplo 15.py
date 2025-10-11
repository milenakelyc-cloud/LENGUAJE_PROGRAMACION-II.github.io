class Numero:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.contador = 0
    def generarNumero(self):
        print("Imprimir Numero")
        while self.contador <= self.cantidad:
            print(self.contador , end = " ")
            self.contador+=1

def main():
    miNumero = Numero(10)
    miNumero.generarNumero()
if __name__=="__main__":
    main()
