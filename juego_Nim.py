import random


def mover_ia(fichas_totales):
    #optmizar para que gane la IA 
    if(fichas_totales - 1) % 3 ==0:
        return 1
    else:
       return 2


def mover_jugador(fichas_totales):
    numero_fichas_tablero = fichas_totales
    print("numero de fichas en el tablero: " ,numero_fichas_tablero)
    fichas = int(input("Cuantas fichas quieres mover (1/2): "))
    if fichas > 2:
        print("ERROR: no puedes retirar mas de dos fichas")
        fichas = int(input("Ingrese de nuevo numero de fichas: "))
        return fichas
    else:
        return fichas


def jugar(fichas):
    while fichas > 0:
        print(" hay ",fichas," en el tablero")
        movimiento_ia = mover_ia(fichas)
        print("IA mueve ", movimiento_ia)
        fichas -= movimiento_ia
        if (fichas == 0):
            print("Final de juego: GANA IA  ")
            break
        else:
            movimiento_jugador = mover_jugador(fichas)
            fichas -= movimiento_jugador
            if fichas == 0:
                print("Final de juego: GANA JUGADOR  ")
                break
# # # # Juego 
jugar(10)

