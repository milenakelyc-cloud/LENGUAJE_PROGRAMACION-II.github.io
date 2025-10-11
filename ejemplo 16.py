class CalculadoraSuma:
    def __init__(self):
        self.total = 0
        
    def sumarNumero(self):
        print("Calcular la suma de numeros ingresados")
        print("Escribe numeros para sumar. Escribr 'fin' para terminar")
        entrada=""
        while entrada.lower() != "fin":
            entrada = input("Ingrese un numero: ")
            if entrada.isdigit():
                self.total+= int(entrada)

            elif entrada.lower() != "fin":
                print("Entrada invalida: Ecribir un numero o 'fin' ")
        print(f"La suma total es: {self.total}")

def main():
    calculadora = CalculadoraSuma()
    calculadora.sumarNumero()
if __name__=="__main__":
    main()
