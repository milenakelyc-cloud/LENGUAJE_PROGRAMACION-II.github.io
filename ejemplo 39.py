import gc
class Curso:
    def __init__(self,nombre,codigo,profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        print(f"Curso registrado {self.nombre} con codigo {self.codigo} del {self.profesor}")

    def mostrar_informacion(self):
        print(f"{self.nombre} con codigo {self.codigo} con {self.profesor}")

    def __del__(self):
        print(f"Curso eliminado: {self.nombre}")

curso_datos = [("LENGUAJES DE PROGRAMACION II","EST305","COYLA IDME LEONEL"),
                     ("INFERENCIA ESTADISTICA","EST306","ROQUE CLAROS ROBERTO ELVIS"),
                     ("MODELOS DISCRETOS","EST307","VARGAS VALVERDE CONFESOR MILAN"),
               (" PROGRAMACION NUMERICA","EST207","TORRES CRUZ FRED  ")]

organizacion = []

for datos in curso_datos:
    curso = Curso(*datos)
    curso.mostrar_informacion()
    organizacion.append(curso) #append es añadir

organizacion.clear()
del curso
gc.collect()
print("Fin del programa")
