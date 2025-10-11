    class CantidadLadrillos:
    def __init__(self,longuitud,altura,ancho,Jh,Jv):
        self.longuitud = longuitud
        self.altura = altura
        self.ancho = ancho
        self.Jh = 0.015
        self.Jv = 0.015

    def Cantidad_de_ladrillos(self):
        return (1/((longuitud + Jh) * (altura + Jv)))

#Solicitar

longuitud = float(input("Ingresar longuitud: "))
altura = float(input("Ingresar altura: "))
ancho = float(input("Ingresar ancho: "))
Jh = 0.015
Jv = 0.015

operacion = CantidadLadrillos(longuitud,altura,ancho,Jh,Jv)

print("La cantidad es ",operacion.Cantidad_de_ladrillos(),"m^2 sin desperdicio")

print("La cantidad es ",operacion.Cantidad_de_ladrillos()*1.05,"m^2 con desperdicio")

print("el area",operacion.Cantidad_de_ladrillos()*8.05*ancho,"m^2")
