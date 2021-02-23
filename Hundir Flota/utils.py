from constants import tablero_j1, tablero_pc1, tablero_j2, tablero_pc2

count_barcos = 0

def activar_barcos():
    global count_barcos

    while count_barcos <= 10:

        if count_barcos <= 3:
            eslora = 1
            print('Introduce un barco de una eslora.')
            poner_barcos(eslora)

        elif count_barcos <= 6:
            eslora = 2
            print('Introduce un barco de dos esloras.')
            poner_barcos(eslora)

        elif count_barcos <= 8:
            eslora = 3
            print('Introduce un barco de tres esloras.')
            poner_barcos(eslora)

        elif count_barcos == 9:
            eslora = 4
            print('Introduce un barco de cuatro esloras.')
            poner_barcos(eslora)

        else:
            print('Has puesto todos los barcos, ¡empieza la partida!')
            break


def poner_barcos(eslora):
    global count_barcos

    if eslora == 1:

        while True:
            fila = int(input('Coordenada fila: '))
            col = int(input('Coordenada columna: '))

            if tablero_j1[fila, col] == 'O':
                print('Ya has puesto un barco ahí, vuelve a intentarlo.')
                print(tablero_j1)
                break
            else:
                tablero_j1[fila, col] = 'O'
                print(tablero_j1)
                count_barcos += 1
                break

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

            if (orient == 'n') and (len(coors_posiN) == eslora) and ('O' in coors_posiN):
                print('Ya has puesto un barco ahí, vuelve a intentarlo.')
                print(tablero_j1)
                break
            elif (orient == 'n') and (len(coors_posiN) == eslora) and ('O' not in coors_posiN):
                tablero_j1[fila:fila - eslora:-1, col] = 'O'
                print(tablero_j1)
                count_barcos += 1
                break

            elif (orient == 'e') and (len(coors_posiE) == eslora) and ('O' in coors_posiE):
                print('Ya has puesto un barco ahí, vuelve a intentarlo.')
                print(tablero_j1)
                break
            elif (orient == 'e') and (len(coors_posiE) == eslora) and ('O' not in coors_posiE):
                tablero_j1[fila, col: col + eslora] = 'O'
                print(tablero_j1)
                count_barcos += 1
                break

            elif (orient == 's') and (len(coors_posiS) == eslora) and ('O' in coors_posiS):
                print('Ya has puesto un barco ahí, vuelve a intentarlo.')
                print(tablero_j1)
                break
            elif (orient == 's') and (len(coors_posiS) == eslora) and ('O' not in coors_posiS):
                tablero_j1[fila:fila + eslora, col] = 'O'
                print(tablero_j1)
                count_barcos += 1
                break

            elif (orient == 'o') and (len(coors_posiO) == eslora) and ('O' in coors_posiO):
                print('Ya has puesto un barco ahí, vuelve a intentarlo.')
                print(tablero_j1)
                break
            elif (orient == 'o') and (len(coors_posiO) == eslora) and ('O' not in coors_posiO):
                tablero_j1[fila, col:col - eslora:-1] = 'O'
                print(tablero_j1)
                count_barcos += 1
                break

def iniciar_tablero():

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


def buscar_coord(turno, fila, columna):

    if turno == 'jugador_1':

        if tablero_pc1[fila, columna] == 'O':
            tablero_j2[fila, columna] = 'X'
            tablero_pc1[fila, columna] = 'X'
            return 'Tocado'

        elif tablero_pc1[fila, columna] == 'A':
            return 'Intentado'

        else:
            tablero_j2[fila, columna] = 'A'
            tablero_pc1[fila, columna] = 'A'

    elif turno == 'pc_1':

        if tablero_j1[fila, columna] == 'O':
            tablero_j1[fila, columna] = 'X'
            tablero_pc2[fila, columna] = 'X'
            return 'Tocado'

        elif tablero_j1[fila, columna] == 'A':
            return 'Intentado'

        elif tablero_j1[fila, columna] == ' ':
            return 'Agua'
