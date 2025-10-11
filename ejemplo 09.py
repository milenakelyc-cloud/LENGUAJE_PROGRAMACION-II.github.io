class Fibonaci:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.serie = []

    def generarSerie(self):
        a,b =0,1
        for _ in range(self.cantidad):
            self.serie.append(a)
            a,b=b,a+b
        return self.serie

def main():
    miFibonaci = Fibonaci(10)
    resultado = miFibonaci.generarSerie()
    print(resultado)
if __name__=="__main__":
    main()
