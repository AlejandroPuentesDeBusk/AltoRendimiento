import math

class Figuras():

    ubicacion_x = 0
    ubicacion_y = 0
    
    def __init__(self):
        None

    def dibujaFigura(self):
        None
        
    def get_area(self):
        return 999999999.9

    def modificar_x(self, x):
        self.ubicacion_x = x
    
    def modificar_y(self, y):
        self.ubicacion_y = y
    
class Rectangulo(Figuras):

    altura = 0.0
    base = 0.0
    
    def __init__(self,altura,base):
        self.altura = float(altura)
        self.base = float(base)

    def __str__(self):
        return "Es un rectangulo, con area: " + str(self.area())
        
    def area(self):
        return self.altura * self.base


class Circulo(Figuras):

    radio = 0.0

    def __init__(self, radio):

        self.radio = float(radio)

    def area(self):

        return math.pi * self.radio **2
    
    def __text__(self):

        return "Area del circulo =" + str(self.area())

class Triangulo(Figuras):

    base = 0.0
    altura = 0.0

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura


    def area(self):

        return self.base * self.altura /2
    
    def __text__(self):

        return "Area del triángulo" + str(self.area())


rect = Rectangulo(6,9)
print(rect.area())


tri = Triangulo(2,2)
print(tri.area())

circ = Circulo(15)
print(circ.area())