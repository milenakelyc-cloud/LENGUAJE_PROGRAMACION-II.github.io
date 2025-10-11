class Estudiante:
    def __init__(self,nombre,dni,codigo_estudiante):
        self.nombre = nombre
        self.dni = dni
        self.codigo_estudiante = codigo_estudiante
        self.cursos = []
        
    def inscribirse(self,curso):
        self.curso = curso
        curso.agregar_estudiante(self)

    def mostrar_informacio(self):
        print(f"\nEstudiante: {self.nombre} DNI:{self.dni} Codigo:{self.codigo_estudiante}")
        print("Cursos inscritos: ")
        for curso in self.curso:
            print(f"{curso.nombre_curso}")

class Profesor:
    def __init__(self,nombre,dni,especialidad):
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad
        
    def mostrar_informacion(self):
        print(f"Profesor: {self.nombre} DNI:{self.dni} Especialidad:{self.especialidad}")

class Curso:
    def __init__(self,nombre_curso,profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []
        
    def agregar_estudiante(self,estudiante):
        if estudiante not in self.estudiante:
            self.estudiantes.append(estudiante)
            
    def mostrar_detalles(self):
        print(f"\nCurso: {self.nombre_curso}")
        print("profesor")
        self.profesor.mostrar_informacion()
        print("Estudiantes inscritos: ")
        for est in self.estudiante:
            print(f"{est.nombre} {est.cdigo_estudiante}")

class Univercidad:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cursos = []
        
    def agregar_curso(self,curso):
        self.cursos.append(curso)
        
    def mostrar_curso(self):
        print(f"Universidad: {self.nombre}")
        for curso in self.cursos:
            curso.mostrar_detalles()
            
prof1 = Profesor("Ing. Juan Carlos","01323043","Programacion")

curso1 = Curso("Lenguaje de programacion II",prof1)
curso2 = Curso("Estructura de datos",prof1)

est1 = Estudiante("Milena Kely","12345678","2025007")
est2 = Estudiante("Henrry Quisoe Ramos","98765432","2025078")

univ = Univercidad("Uiversidad Nacional del Altiplano")
univ.agregar_curso(curso1)
univ.agregar_curso(curso2)

est1.inscribirse(curso1)
est1.inscribirse(curso2)
est2.inscribirse(curso2)

univ.mostrar_cursos()
est1.mostrar_informacion()
est2.mostrar_informacion()
