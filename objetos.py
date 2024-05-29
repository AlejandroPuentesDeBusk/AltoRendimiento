import turtle


#Turtle parameters
tur = turtle.Turtle()
speed= tur.speed(0)
screen = turtle.Screen()
screen.title("Gato")
screen.setup(600,600)
turtle.bgcolor("#729A91")

#Objeto linea

class Line():

    lenght = 0.0

    def __init__(self,x,y,x1,y1):
        
        self.x = float(x)
        self.y = float(y)
        self.x1 = float(x1)
        self.y1 = float(y1)

    def draw(self):

        tur.width(10)
        tur.color("#CC0609")

        tur.penup()
        tur.goto(self.x, self.y)
        tur.pendown()
        tur.goto(self.x1, self.y1)
        

def draw_line(x,y,x1,y1):

    line = Line(x,y,x1,y1)
    line.draw()




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
        


#screen.onclick(draw_tacha)


#Dibujamos el tablero, las dimesiones cambian junto con la pantalla
class Panel():

    def __init__(self,tur,width,height):
        
        self.tur = tur
        self.width = width
        self.height = height


    def draw(self):

        tur = self.tur

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




#Le damos el valor de x, y del mouse
class Tablero():

    def __init__(self, width):
        self.width = width
        self.turn  = True
        self.m = None

        self.jugador1 = "         "
        self.jugador2 = "         "

    def get_width(self):
        return self.width

    def coor(self,x,y):

        width = self.width

        match(x,y):

            case(x,y) if x < (-width/6) and y > (width/6):

                new_x = -width/3
                new_y = width/3
                self.m = 0

            case(x,y) if x > (-width/6) and y > (width/6) and x < (width/6):

                new_x = 0.0
                new_y = width/3
                self.m = 1

            case(x,y) if x > (width/6) and y > (width/6):

                new_x = width/3
                new_y = width/3
                self.m = 2

            case(x,y) if y < (width/6) and y > (-width/6) and x < (-width/6):

                new_x = -width/3
                new_y = 0.0
                self.m = 3

            case(x,y) if x > (-width/6) and x < (width/6) and y > (-width/6) and y < (width/6):

                new_x = 0.0
                new_y = 0.0
                self.m = 4

            case(x,y) if x > (width/6) and y > (-width/6) and y <(width/6):

                new_x = width/3
                new_y = 0.0
                self.m = 5

            case(x,y) if x < (-width/6) and y < (-width/6):

                new_x = -width/3
                new_y = -width/3
                self.m = 6

            case(x,y) if x > (-width/6) and x < (width/6) and y < (-width/6):

                new_x = 0.0
                new_y = -width/3
                self.m = 7

            case _:

                new_x = width/3
                new_y = -width/3
                self.m = 8
        print(self.m)


    #Va alternando la X y el Circulo


        if self.turn == True:
            
            tacha = Tacha(self.width/3,new_x,new_y)  
            tacha.draw()
        
           
            self.jugador1 = self.jugador1[:self.m] + '.' + self.jugador1[self.m+1:] 
           
            
        else:
            circ = Circle(width/6,new_x,new_y)
            circ.draw()
            
            
            self.jugador2 = self.jugador2[:self.m] + '.' + self.jugador2[self.m+1:] 
            

        self.win()
            
        self.turn = not self.turn  
        #print(self.turn)


    def win(self):

        escenarios_ganadores = [
            "...      ",
            "   ...   ",
            "      ...",
            ".   .   .",
            "  . . .  ",
            ".  .  .  ",
            " .  .  . ",
            "  .  .  ."
            
        ]
        #dondevarayita = [
        #    [x1,y1,x2,y2],
        #    [x1,y1,x2,y2],
        #    [x1,y1,x2,y2],
        #]

        print("'"+self.jugador1+"'")
        print(len(self.jugador1))

        if self.jugador1 in escenarios_ganadores:
            print("Gano jugador 1")
        elif self.jugador2 in escenarios_ganadores:
            print("Gano jugador 2")




#Turtle parameters

juego = Tablero(width = 600)
panel = Panel(tur, juego.get_width() , juego.get_width())
panel.draw()
screen.onclick(juego.coor)

turtle.done()

