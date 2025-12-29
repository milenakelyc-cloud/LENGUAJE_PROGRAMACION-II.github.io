def main():
    try:
        n = int(input("¿Cuántos términos de la serie Fibonacci desea generar? "))
        
        if n <= 0:
            raise ValueError("Debe ingresar un número positivo")
        
        if n == 1:
            print("Serie de Fibonacci: 0")
        elif n == 2:
            print("Serie de Fibonacci: 0, 1")
        else:
            a, b = 0, 1
            resultado = "0, 1"
            
            for i in range(2, n):
                c = a + b
                resultado = resultado + ", " + str(c)
                a = b
                b = c
            
            print(f"Serie de Fibonacci: {resultado}")
        
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Ocurrio un error inesperado:", e)

if __name__ == "__main__":
    main()