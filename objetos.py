import turtle

width = 600

screen = turtle.Screen()
screen.setup( width , width)
screen.title("Gato")
tur = turtle.Turtle()
speed= tur.speed(0)
    
class Rectangulo():

    altura = 0.0
    base = 0.0
    

    def __init__(self,altura,base):
        self.altura = float(altura)
        self.base = float(base)
    
    def dibujo(self):

        for i in range(2):
            tur.forward(self.altura)
            tur.left(90)
            tur.forward(self.base)
            tur.left(90)   


class Circulo():

    radio = 0.0
    x = 0
    y = 0
   
    
    def __init__(self, radio,x=0,y=0):

        self.radio = float(radio)
        self.x = int(x)
        self.y = int(y)
       
    def dibujo(self):

        tur.penup()
        tur.goto(self.x, self.y-self.radio)
        tur.pendown()
        tur.circle(self.radio)

def dibujar_circulo(x,y):

    circ = Circulo(width/6,x,y)
    circ.dibujo()


screen.onclick(dibujar_circulo)
       

class Tacha():

    line = 0.0
    x = 0
    y = 0

    def __init__(self,line,x=0,y=0):

        self.line = float(line)
        self.x = int(x)
        self.y = int(y)

    def dibujo(self):

        tur.penup()
        tur.goto(self.x, self.y)
        tur.pendown()

        for i in range(4):

            tur.penup()
            tur.goto(self.x,self.y)
            tur.pendown()
            tur.right(45)
            tur.forward(self.line/2)
            tur.right(45)
           

def dibujar_tacha(x, y):
    tacha = Tacha(width/3, x, y)  
    tacha.dibujo()


screen.onclick(dibujar_tacha)


class Reg():

    def __init__(self,width,height):
        
        self.width = width
        self.height = height


    def dibujo(self):


        lw = self.width/6
        lh = self.height/6

        tur.penup()
        tur.goto(-self.width/2, lw)
        tur.pendown()
        tur.forward(self.width)
        tur.penup()

        tur.goto(-self.width/2, -lh)
        tur.pendown()
        tur.forward(self.width)
        tur.penup()

        tur.goto(-lw, self.height/2)
        tur.pendown()
        tur.goto(-lw,-self.height/2)
        tur.penup()

        tur.goto(lw, self.height/2)
        tur.pendown()
        tur.goto(lw, -self.height/2)

        tur.penup()

def tablero():

    reg=Reg(width,width)
    reg.dibujo()

tablero()



turno = True

def turnos(x, y):

    global turno 


    if turno == True:
        tacha = Tacha(width/3, x, y)  
        tacha.dibujo()
    else:
        circ = Circulo(width/6,x,y)
        circ.dibujo()

    turno = not turno   

screen.onclick(turnos)


turtle.done()

