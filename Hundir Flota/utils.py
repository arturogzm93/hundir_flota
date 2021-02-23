from constants import tablero_j1, tablero_pc1

def activar_barcos(contador, tablero):

    while contador < 10:

        if contador < 4:
            eslora = 1
            print('Introduce un barco de una eslora.')
            print('contador1', contador)
            contador = poner_barcos(eslora, contador, tablero)

        elif contador < 7:
            eslora = 2
            print('Introduce un barco de dos esloras.')
            print('contador2', contador)
            contador = poner_barcos(eslora, contador, tablero)

        elif contador < 9:
            eslora = 3
            print('Introduce un barco de tres esloras.')
            print('contador3', contador)
            contador = poner_barcos(eslora, contador, tablero)

        elif contador < 10:
            eslora = 4
            print('Introduce un barco de cuatro esloras.')
            print('contador4', contador)
            contador = poner_barcos(eslora, contador, tablero)

        else:
            print('Has puesto todos los barcos, ¡empieza la partida!')
            break


def poner_barcos(eslora, contador, tablero):

    if eslora == 1:

        while True:
            fila = int(input('Coordenada fila: '))
            col = int(input('Coordenada columna: '))

            if 'O' not in tablero[fila, col]:
                tablero[fila, col] = 'O'
                print(tablero_j1)
                contador += 1
                print('contador11', contador)
                return contador
            else:
                print('Ya hay un barco o te has salido del tablero.')

    else:
        while True:
            fila = int(input('Coordenada fila: '))
            col = int(input('Coordenada columna: '))
            orient = input('Coordenada N, S, E, O: ')

            orient = orient.lower()

            coors_posiN = tablero[fila:fila - eslora:-1, col]
            coors_posiE = tablero[fila, col: col + eslora]
            coors_posiS = tablero[fila:fila + eslora, col]
            coors_posiO = tablero[fila, col:col - eslora:-1]

            if (orient == 'n') and (len(coors_posiN) == eslora) and ('O' not in coors_posiN):
                tablero[fila:fila - eslora:-1, col] = 'O'
                print(tablero)
                contador += 1
                print('contador234', contador)
                return contador

            elif (orient == 'e') and (len(coors_posiE) == eslora) and ('O' not in coors_posiE):
                tablero[fila, col: col + eslora] = 'O'
                print(tablero)
                contador += 1
                print('contador234', contador)
                return contador

            elif (orient == 's') and (len(coors_posiS) == eslora) and ('O' not in coors_posiS):
                tablero[fila:fila + eslora, col] = 'O'
                print(tablero)
                contador += 1
                print('contador234', contador)
                return contador

            elif (orient == 'o') and (len(coors_posiO) == eslora) and ('O' not in coors_posiO):
                tablero[fila, col:col - eslora:-1] = 'O'
                print(tablero)
                contador += 1
                print('contador234', contador)
                return contador

            else:
                print('Ya hay un barco o te has salido del tablero.')
                return contador

def iniciar_tablero():

    #tablero_j1[0:4, 0] = 'O'  # eslora 4
    #tablero_j1[2:5, 5] = 'O'  # eslora 3
    #tablero_j1[-1, 2:5] = 'O'  # eslora 3
    #tablero_j1[5, 6:8] = 'O'  # eslora 2
    #tablero_j1[-3, 4:6] = 'O'  # eslora 2
    #tablero_j1[2:4, 3] = 'O'  # es 2
    #tablero_j1[5, 2] = 'O'  # es 1
    #tablero_j1[2, -2] = 'O'  # es 1
    #tablero_j1[8, -1] = 'O'  # es 1
    #tablero_j1[9, 8] = 'O'  # es 1
    #print(tablero_j1)

    tablero_pc1[5, 2:6] = 'O'  # eslora 4
    tablero_pc1[0:3, 8] = 'O'  # eslora 3
    tablero_pc1[8, 6:9] = 'O'  # eslora 3
    tablero_pc1[7:9, 2] = 'O'  # eslora 2
    tablero_pc1[0, 3:5] = 'O'  # eslora 2
    tablero_pc1[2:4, 1] = 'O'  # es 2
    tablero_pc1[3, -4] = 'O'  # es 1
    tablero_pc1[9, 0] = 'O'  # es 1
    tablero_pc1[9, 4] = 'O'  # es 1
    tablero_pc1[4, 9] = 'O'  # es 1

    return tablero_j1

def buscar_coord(fila, columna, tablero_1, tablero_2):

    if tablero_1[fila, columna] == 'O':
        tablero_1[fila, columna] = 'X'
        tablero_2[fila, columna] = 'X'
        print('Tocado')

        return tablero_1, tablero_2

    elif tablero_1[fila, columna] == 'A':

        print('Intentado')

    else:
        tablero_1[fila, columna] = 'A'
        tablero_2[fila, columna] = 'A'
        print('Agua')

        return tablero_1, tablero_2

#def reiniciar_tablero(vidas_pc, vidas_j):