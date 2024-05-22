import math
import turtle

screen = turtle.Screen()
screen.title("Gato")
tur = turtle.Turtle()
speed= tur.speed(0)
    
class Rectangulo():

    altura = 0.0
    base = 0.0
    

    def __init__(self,altura,base):
        self.altura = float(altura)
        self.base = float(base)

    def __str__(self):
        return "Es un rectangulo, con area: " + str(self.area())
        
    def area(self):
        return self.altura * self.base
    
    def dibujo(self):

        for i in range(2):
            tur.forward(self.altura)
            tur.left(90)
            tur.forward(self.base)
            tur.left(90)   


class Circulo():

    radio = 0.0
   
    
    def __init__(self, radio):

        self.radio = float(radio)
       

    def area(self):

        return math.pi * self.radio **2
    
    def __text__(self):

        return "Area del circulo =" + str(self.area())
    
    def dibujo(self):

        tur.circle(self.radio)
       

class Reg():

    line = 0.0 
    

    def __init__(self,line):

        self.line = float(line)

    def dibujo(self):

        tur.penup()
        tur.goto(-100,100)
        tur.right(90)
        tur.pendown
        tur.forward(self.line)

class Triangulo():

    base = 0.0
    altura = 0.0

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura


    def area(self):

        return self.base * self.altura /2
    
    def __text__(self):

        return "Area del triángulo" + str(self.area())



screen.setup(width=400, height=300)
width = screen.window_width()
height = screen.window_height()


initial_position = tur.position()
print(f"La posición inicial de la tortuga es {initial_position}")


tur.penup()
 

R1W = width/6
R1H = height/6

tur.goto(-width/2, R1H)
tur.pendown()
tur.forward(width)
tur.penup()

tur.goto(-width/2, -R1H)
tur.pendown()
tur.forward(width)
tur.penup()

tur.goto(-R1W, height/2)
tur.pendown()
tur.goto(-R1W,-height/2)
tur.penup()

tur.goto(R1W, height/2)
tur.pendown()
tur.goto(R1W, -height/2)



circ = Circulo(45)
rect = Rectangulo(100, 200)

#print(line,rect, circ)
#rect.dibujo()
circ.dibujo()


turtle.done()