import turtle


#Turtle parameters
width = 600
tur = turtle.Turtle()
screen = turtle.Screen()
screen.setup( width , width)
turtle.bgcolor("#729A91")
screen.title("Gato")
speed= tur.speed(0)

    


#Creamos el objeto circulo, se dibuja en el punto donde das click
class Circle():

    radio = 0.0
    x = 0
    y = 0
   
    
    def __init__(self, radio,x=0,y=0):

        self.radio = float(radio)-10
        self.x = int(x)
        self.y = int(y)
       
    def draw(self):

        tur.width(5)
        tur.color("#E0E8E6")

        tur.penup()
        tur.goto(self.x, self.y-self.radio)
        tur.pendown()
        tur.circle(self.radio)

def draw_circle(x,y):

    circ = Circle(width/6,x,y)
    circ.draw()


#screen.onclick(draw_circle)
       

#Creamos el objeto tacha y que se dibuje donde damos click
class Tacha():

    
    line = 0.0
    x = 0
    y = 0

    def __init__(self,line,x=0,y=0):

        self.line = float(line)
        self.x = int(x)
        self.y = int(y)

    def draw(self):

        tur.width(5)
        tur.color("#272727")

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
           

def draw_tacha(new_x,new_y):
    tacha = Tacha(width/3, new_x, new_y)  
    tacha.draw()


#screen.onclick(draw_tacha)


#Dibujamos el tablero, las dimesiones cambian junto con la pantalla
class Panel():

    def __init__(self,width,height):
        
        self.width = width
        self.height = height


    def draw(self):

        lw = self.width/6
        lh = self.height/6

        tur.penup()
        tur.goto(-self.width/2, lw)
        tur.pendown()
        tur.width(10)
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

def draw_panel():

    reg=Panel(width,width)
    reg.draw()

draw_panel()

turn = True

#Funcion para que cheque que revisa en que rango esta la coordenada del mouse 

def coor(x,y):

    global width
    global turn 

    match(x,y):

        case(x,y) if x < (-width/6) and y > (width/6):

            new_x = -width/3
            new_y = width/3

        case(x,y) if x > (-width/6) and y > (width/6) and x < (width/6):

            new_x = 0.0
            new_y = width/3

        case(x,y) if x > (width/6) and y > (width/6):

            new_x = width/3
            new_y = width/3

        case(x,y) if y < (width/6) and y > (-width/6) and x < (-width/6):

            new_x = -width/3
            new_y = 0.0

        case(x,y) if x > (-width/6) and x < (width/6) and y > (-width/6) and y < (width/6):

            new_x = 0.0
            new_y = 0.0

        case(x,y) if x > (width/6) and y > (-width/6) and y <(width/6):

            new_x = width/3
            new_y = 0.0

        case(x,y) if x < (-width/6) and y < (-width/6):

            new_x = -width/3
            new_y = -width/3

        case(x,y) if x > (-width/6) and x < (width/6) and y < (-width/6):

            new_x = 0.0
            new_y = -width/3

        case _:

            new_x = width/3
            new_y = -width/3



    if turn == True:
        
        tacha = Tacha(width/3,new_x,new_y)  
        tacha.draw()
        
    else:
        circ = Circle(width/6,new_x,new_y)
        circ.draw()
        

    turn = not turn  
           


screen.onclick(coor)
#screen.onclick(turns)



turtle.done()

