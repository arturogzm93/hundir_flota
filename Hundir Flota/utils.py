from constants import tablero_j1, tablero_pc1, contador


def activar_barcos(contador):

    while contador <= 10:

        if contador <= 3:
            eslora1 = 1
            print('Introduce un barco de una eslora.')
            poner_barcos(eslora, contador)

        elif contador <= 6:
            eslora2 = 2
            print('Introduce un barco de dos esloras.')
            poner_barcos(eslora, contador)

        elif contador <= 8:
            eslora = 3
            print('Introduce un barco de tres esloras.')
            poner_barcos(eslora, contador)

        elif contador <= 9:
            eslora = 4
            print('Introduce un barco de cuatro esloras.')
            poner_barcos(eslora, contador)

        else:
            print('Has puesto todos los barcos, ¡empieza la partida!')
            break


def poner_barcos(eslora, contador):

    if eslora == 1:

        while True:
            fila = int(input('Coordenada fila: '))
            col = int(input('Coordenada columna: '))

            if tablero[fila, col] = 'O'
                print(tablero_j1)
                count_barcos += 1
                return contador


    else:

        while True:
            fila = int(input('Coordenada fila: '))
            col = int(input('Coordenada columna: '))
            orient = input('Coordenada N, S, E, O: ')

            orient = orient.lower()

            coors_posiN = tablero_j1[fila:fila - eslora:-1, col]
            coors_posiE = tablero_j1[fila, col: col + eslora]
            coors_posiS = tablero_j1[fila:fila + eslora, col]
            coors_posiO = tablero_j1[fila, col:col - eslora:-1]

            if (orient == 'n') and (len(coors_posiN) == eslora) and ('O' not in coors_posiN):
                tablero_j1[fila:fila - eslora:-1, col] = 'O'
                print(tablero_j1)
                count_barcos += 1
                break

            elif (orient == 'e') and (len(coors_posiE) == eslora) and ('O' not in coors_posiE):
                tablero_j1[fila, col: col + eslora] = 'O'
                print(tablero_j1)
                count_barcos += 1
                break

            elif (orient == 's') and (len(coors_posiS) == eslora) and ('O' not in coors_posiS):
                tablero_j1[fila:fila + eslora, col] = 'O'
                print(tablero_j1)
                count_barcos += 1
                break

            elif (orient == 'o') and (len(coors_posiO) == eslora) and ('O' not in coors_posiO):
                tablero_j1[fila, col:col - eslora:-1] = 'O'
                print(tablero_j1)
                count_barcos += 1
                break

            else:
                print('Ya hay un barco o te has salido del tablero.')

def iniciar_tablero():

    tablero_j1[0:4, 0] = 'O'  # eslora 4
    tablero_j1[2:5, 5] = 'O'  # eslora 3
    tablero_j1[-1, 2:5] = 'O'  # eslora 3
    tablero_j1[5, 6:8] = 'O'  # eslora 2
    tablero_j1[-3, 4:6] = 'O'  # eslora 2
    tablero_j1[2:4, 3] = 'O'  # es 2
    tablero_j1[5, 2] = 'O'  # es 1
    tablero_j1[2, -2] = 'O'  # es 1
    tablero_j1[8, -1] = 'O'  # es 1
    tablero_j1[9, 8] = 'O'  # es 1
    print(tablero_j1)

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