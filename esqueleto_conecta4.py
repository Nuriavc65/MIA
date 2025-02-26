#Tamaño del tablero
FILAS = 6
COLUMNAS = 7
GANA = 4  

#Pintar el tablero
tablero = []
for _ in range(FILAS):  
    fila = [' ' for _ in range(COLUMNAS)] 
    tablero.append(fila)

#Imprimir el tablero
def imprimir_tablero():
    pass

#Comprobar si el tablero está lleno
def tablero_lleno():
    pass

#Comprobar si un jugador ha ganado
def verificar_ganador(jugador):
    pass  

#Obtener la próxima fila disponible en una columna (fila más baja de la columna, para colocar la ficha)
def obtener_fila(columna):
    pass 

#Minimax
#def minimax(tablero, jugador, oponente):
#    pass


#Bucle del juego
def jugar():
    jugador = 'X'
    jugador_ia = 'O'

    while True:
        imprimir_tablero()


#Ejecutar el juego
jugar()

