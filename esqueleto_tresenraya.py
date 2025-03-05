import random


#Creo un array, no una matriz, pero lo pinto como si fuera una, para simplificar
def pintar_tablero(tablero):
    print("\n")
    for i in range(3):
        #Imprimo cada fila directamente 
        print(f"| {tablero[i*3]} | {tablero[i*3+1]} | {tablero[i*3+2]} |")
        
        #Si no es la última fila, imprimo separador
        if i < 2:
            print("-------------") 
    print("\n")

#Comproamos si uno de los jugadores ha ganado la partida
def comprobar_ganador(tablero, jugador):

    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  #Comprobación filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  #Comprobación columnas
        [0, 4, 8], [2, 4, 6]              #COmprobación diagonales (no era necesarias)
    ]
    
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == jugador and \
           tablero[combinacion[1]] == jugador and \
           tablero[combinacion[2]] == jugador:
            return True
    return False

#Evaluación del tablero para IA (puntuar cada estado)
#Para usar en Algoritmo MinMax
def evaluar_posible_jugada(tablero):
    if comprobar_ganador(tablero, "X"):  #Gana el jugador
        return -1
    elif comprobar_ganador(tablero, "O"):  #Gana la IA
        return 1
    elif all(isinstance(i, str) for i in tablero):  #Hay un empate
        return 0
    return None

#Devuelve las posiciones libres, para quela IA no use una ocupada
def obtener_movimientos_disponibles(tablero):
    posiciones_disponibles = []
    for i in range(9):
        if isinstance(tablero[i], (int)):
            posiciones_disponibles.append(i)
    return posiciones_disponibles

#IA: movimiento, por ahora, al azar entre las posiciones disponibles
def movimiento_ia(tablero):

    movimientos_posibles = obtener_movimientos_disponibles(tablero)
    movimiento_elegido = random.choice(movimientos_posibles)
    return movimiento_elegido

#Bucle del juego
def jugar():

    tablero = [] 
    for i in range(9):
        tablero.append((i+1))

    turno_jugador = True  #Empiezas a jugar tú, en la consola
    
    #Continuamos mientras queden números en el array
    while any(isinstance(i, (int)) for i in tablero):  
        pintar_tablero(tablero)  #PIntamos el tablero
        
        if turno_jugador:
            movimiento = int(input("Elige una posición entre 1 y 9: "))
            movimiento -= 1
            movimiento_erroneo = True
            while movimiento_erroneo:
                if movimiento < 0 or movimiento > 8:
                    movimiento = int(input("Número fuera de rango. Introduce un número entre 1 y 9: "))
                    movimiento -= 1
                else: 
                    if tablero[movimiento] == "X" or tablero[movimiento] == "O":
                        movimiento = int(input("Esa posición ya está ocupada. Intenta con otra: "))
                        movimiento -= 1
                    else:
                        movimiento_erroneo = False
        else:
            movimiento = movimiento_ia(tablero)
            print(f"La IA elige la posición {movimiento}")
        
        #Colocamos el símbolo del jugador en el tablero
        if turno_jugador:
            tablero[movimiento] = "X"
        else:
            tablero[movimiento] = "O"
        
        #COmprobamos si hay un ganador
        if comprobar_ganador(tablero, "X" if turno_jugador else "O"):
            pintar_tablero(tablero)
            if turno_jugador:
                print("Has ganado.")
            else:
                print("La IA ha ganado")
            return
        
        #Cambiamos de turno para qu juegue la IA
        turno_jugador = not turno_jugador
    
    #Si se sale del bucle, es un empate
    pintar_tablero(tablero)
    print("¡Es un empate!")

jugar()
