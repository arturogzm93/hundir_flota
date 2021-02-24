import numpy as np

import random


def activar_barcos(contador, tablero, turno):

    while contador < 10:

        try:

            if contador < 4:
                eslora = 1
                print('Introduce un barco de una eslora.')
                contador = poner_barcos(eslora, contador, tablero, turno)

            elif contador < 7:
                eslora = 2
                print('Introduce un barco de dos esloras.')
                contador = poner_barcos(eslora, contador, tablero, turno)

            elif contador < 9:
                eslora = 3
                print('Introduce un barco de tres esloras.')
                contador = poner_barcos(eslora, contador, tablero, turno)

            elif contador < 10:
                eslora = 4
                print('Introduce un barco de cuatro esloras.')
                contador = poner_barcos(eslora, contador, tablero, turno)

            else:
                print('Has puesto todos los barcos, ¡empieza la partida!')

        except ValueError:
            print('error')
            continue


def poner_barcos(eslora, contador, tablero, turno):

    if eslora == 1 and turno == 'jug':

        fila = int(input('Coordenada fila: '))
        col = int(input('Coordenada columna: '))

        if 'O' not in tablero[fila, col]:
            tablero[fila, col] = 'O'
            print(tablero)
            contador += 1
            return contador

        else:
            print('Ya hay un barco o te has salido del tablero.')

    else:
        if turno == 'jug':
            fila = int(input('Coordenada fila: '))
            col = int(input('Coordenada columna: '))
            orient = input('Coordenada N, S, E, O: ')
            orient = orient.lower()

        elif turno == 'pc':
            orient = random.choice(['N', 'S', 'E', 'O'])
            orient = orient.lower()
            current_pos = np.random.randint(10, size=2)
            fila = current_pos[0]
            col = current_pos[1]

        while True:

            coors_posiN = tablero[fila:fila - eslora:-1, col]
            coors_posiE = tablero[fila, col: col + eslora]
            coors_posiS = tablero[fila:fila + eslora, col]
            coors_posiO = tablero[fila, col:col - eslora:-1]

            if (orient == 'n') and (len(coors_posiN) == eslora) and ('O' not in coors_posiN):
                tablero[fila:fila - eslora:-1, col] = 'O'
                contador += 1
                return contador

            elif (orient == 'e') and (len(coors_posiE) == eslora) and ('O' not in coors_posiE):
                tablero[fila, col: col + eslora] = 'O'
                contador += 1
                return contador

            elif (orient == 's') and (len(coors_posiS) == eslora) and ('O' not in coors_posiS):
                tablero[fila:fila + eslora, col] = 'O'
                contador += 1
                return contador

            elif (orient == 'o') and (len(coors_posiO) == eslora) and ('O' not in coors_posiO):
                tablero[fila, col:col - eslora:-1] = 'O'
                contador += 1
                return contador

            else:
                print('Ya hay un barco o te has salido del tablero.')
                return contador


def buscar_coord(fila, columna, tablero_1, tablero_2):
    try:
        if tablero_1[fila, columna] == 'O':
            tablero_1[fila, columna] = 'X'
            tablero_2[fila, columna] = 'X'

            return 'Tocado'

        elif tablero_1[fila, columna] == 'A':

            return 'Intentado'

        else:
            tablero_1[fila, columna] = 'A'
            tablero_2[fila, columna] = 'A'

            return 'Agua'

    except NameError or ValueError:
        print('error')
