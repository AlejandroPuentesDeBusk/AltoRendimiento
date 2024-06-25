import turtle


#Turtle parameters
#tur = turtle.Turtle()
#speed= tur.speed(0)
#screen = turtle.Screen()  ######
turtle.bgcolor("#729A91")
#screen.title("Gato")    ########
#width= 600
#screen.setup(width,width)



class Line():

    lenght = 0.0

    def __init__(self,x,y,x1,y1):

        self.tur = turtle.Turtle() #################
        self.speed= self.tur.speed(0)
      
        
        
        self.x = float(x)
        self.y = float(y)
        self.x1 = float(x1)
        self.y1 = float(y1)

    def draw(self):

        tur= self.tur ###############
        self.speed= tur.speed(0)


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

        self.tur = turtle.Turtle() ################
        self.speed= self.tur.speed(0)
        self.radio = float(radio)-10
        self.x = int(x)
        self.y = int(y)
       
    def draw(self):

        tur = self.tur  ##################
        self.speed= tur.speed(0)

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

        self.tur = turtle.Turtle()  ##############
        self.speed= self.tur.speed(0)

        self.line = float(line)
        self.x = int(x)
        self.y = int(y)

    def draw(self):

        tur = self.tur  ################
        self.speed= tur.speed(0)

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

    def __init__(self,width,height):    ###########(tur:2)
        

        self.tur = turtle.Turtle()
        self.speed= self.tur.speed(0)
        
        self.screen = turtle.Screen()  #########
        self.screen.setup(width,width) #########
        #self.tur = tur     #################
        self.width = width
        self.height = height


    def draw(self):

      

        tur = self.tur
        self.speed= tur.speed(0)
        self.screen = turtle.Screen()
        self.screen.setup(self.width,self.width)


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

        self.combination_1 = []
        self.combination_2 = []

        self.jugador1 = "         "
        self.jugador2 = "         "

        self.positions =[" "," "," "," "," "," "," "," "," "]
        self.conditions=[True, True, True,True, True, True,True, True, True,True]

        self.screen = turtle.Screen()
        
        

    def get_width(self):
        return self.width
    
    def state(self, m):

        self.conditions[m-1] += 1
        print(self.conditions)
    
    def ia(self,m,icon):

        self.positions[m-1] = icon
        jugadas = "".join(self.positions)
        print (jugadas)

        #notas = open("IA_10.txt", "a")
        #notas.write(jugadas+ "\n")
        #notas.close()
    

    def coor(self,x,y):

        width = self.width
        


        match(x,y):

            case(x,y) if x < (-width/6) and y > (width/6):

                new_x = -width/3
                new_y = width/3
                self.m = 1
               

            case(x,y) if x > (-width/6) and y > (width/6) and x < (width/6):

                new_x = 0.0
                new_y = width/3
                self.m = 2

            case(x,y) if x > (width/6) and y > (width/6):

                new_x = width/3
                new_y = width/3
                self.m = 3

            case(x,y) if y < (width/6) and y > (-width/6) and x < (-width/6):

                new_x = -width/3
                new_y = 0.0
                self.m = 4

            case(x,y) if x > (-width/6) and x < (width/6) and y > (-width/6) and y < (width/6):

                new_x = 0.0
                new_y = 0.0
                self.m = 5

            case(x,y) if x > (width/6) and y > (-width/6) and y <(width/6):

                new_x = width/3
                new_y = 0.0
                self.m = 6

            case(x,y) if x < (-width/6) and y < (-width/6):

                new_x = -width/3
                new_y = -width/3
                self.m = 7

            case(x,y) if x > (-width/6) and x < (width/6) and y < (-width/6):

                new_x = 0.0
                new_y = -width/3
                self.m = 8

            case _:

                new_x = width/3
                new_y = -width/3
                self.m = 9
        print(self.m)

        
    #Va alternando la X y el Circulo


        if self.turn == True and self.conditions[self.m] == True:
            
            tacha = Tacha(self.width/3,new_x,new_y)  
            tacha.draw()

            
            self.combination_1.append(self.m)
            print(self.combination_1)
            self.ia(self.m,"x")

            self.turn = not self.turn  
            
            
            
        elif self.turn == False and self.conditions[self.m] == True:
            circ = Circle(width/6,new_x,new_y)
            circ.draw()
            
            self.combination_2.append(self.m)
            print(self.combination_2)
            self.ia(self.m,"o")

            self.turn = not self.turn  
            
             
            

        self.win()
        self.conditions[self.m] = False


    def win(self):
       
       a,b,c = 1,4,7
       z,x,y = 1,2,3
       o,p,q = 1,5,9
      
       w = "You win"

    #comprobador de las x

       match self.combination_1:
           
           #PARADAS
           case self.combination_1:
                
                for i in range(3):

        
                    if a in self.combination_1 and b in self.combination_1 and c in self.combination_1:

                        print(f"{w} : player x")

                        if i == 0:

                            draw_line(-self.width/3,self.width/2,-self.width/3,-self.width/2 )

                        elif i == 1:

                            draw_line(0.0,self.width/2,0.0,-self.width/2 )
                        
                        else:

                            draw_line(self.width/3,self.width/2,self.width/3,-self.width/2 )

                    a += 1
                    b += 1
                    c += 1
        
        #ACOSTADAS
       match self.combination_1:
            

           case self.combination_1:
               
                for i in range(3):


                    if z in self.combination_1 and x in self.combination_1 and y in self.combination_1:

                        print(f"{w} : player x")

                        if i == 0:

                            draw_line(-self.width/2,self.width/3,self.width/2,self.width/3 )

                        elif i == 1:

                            draw_line(-self.width/2,0.0,self.width/2,0.0 )
                        
                        else:

                            draw_line(-self.width/2,-self.width/3,self.width/2,-self.width/3 )

                    z += 3
                    x += 3
                    y += 3  


       match self.combination_1:

           case self.combination_1:
               
                for i in range(2):

                    if o in self.combination_1 and p in self.combination_1 and q in self.combination_1:

                        print(f"{w} : player x")

                        if i == 0:

                            draw_line(-self.width/2,self.width/2,self.width/2,-self.width/2 )

                        elif i == 1:

                            draw_line(self.width/2,self.width/2,-self.width/2,-self.width/2 )

                    o += 2
                    q +=-2

       a,b,c = 1,4,7
       z,x,y = 1,2,3
       o,p,q = 1,5,9
                

    #comprobador del circulo
       match self.combination_2:
           
           
           case self.combination_2:
                
                for i in range(3):

        
                    if a in self.combination_2 and b in self.combination_2 and c in self.combination_2:

                        print(f"{w} : player O")

                        if i == 0:

                            draw_line(-self.width/3,self.width/2,-self.width/3,-self.width/2 )

                        elif i == 1:

                            draw_line(0.0,self.width/2,0.0,-self.width/2 )
                        
                        else:

                            draw_line(self.width/3,self.width/2,self.width/3,-self.width/2 )


                    a += 1
                    b += 1
                    c += 1

       match self.combination_2:
            

           case self.combination_2:
               
                for i in range(3):


                    if z in self.combination_2 and x in self.combination_2 and y in self.combination_2:

                        print(f"{w} : player O")

                        if i == 0:

                            draw_line(-self.width/2,self.width/3,self.width/2,self.width/3 )

                        elif i == 1:

                            draw_line(-self.width/2,0.0,self.width/2,0.0 )
                        
                        else:

                            draw_line(-self.width/2,-self.width/3,self.width/2,-self.width/3 )


                    z += 3
                    x += 3
                    y += 3  

       match self.combination_2:

           case self.combination_2:
               
                for i in range(2):

                    if o in self.combination_2 and p in self.combination_2 and q in self.combination_2:

                        print(f"{w} : player O")

                        if i == 0:

                            draw_line(-self.width/2,self.width/2,self.width/2,-self.width/2 )

                        elif i == 1:

                            draw_line(self.width/2,self.width/2,-self.width/2,-self.width/2 )

                    o += 2
                    q +=-2

    def open(self):

        juego = Tablero(600)
        panel = Panel( juego.get_width() , juego.get_width())
        panel.draw()
        self.screen.onclick(juego.coor)

        turtle.done()

                

#Open

#juego = Tablero(width)


#panel = Panel( juego.get_width() , juego.get_width())
#panel.draw()
#screen.onclick(juego.coor)

#turtle.done()