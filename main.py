
from objetos import  Tablero, Panel


class Jugador:
    def __init__(self, tipo):
        self.computadora = bool(tipo)
        self.estado = "         "


def main():
    jugador1 = Jugador(input("Primer jugador: (0) Humano (1) Computadora: "))
    jugador2 = Jugador(input("Segundo jugador: (0) Humano (1) Computadora: "))

    
    juego = Tablero(600)
    lineas = Panel(600,600)
    lineas.draw()
    juego.coor()




main()