from constants import tablero_j1, tablero_pc1, tablero_j2, tablero_pc2


def iniciar_tablero():
    tablero_j1[0:4, 0] = 'O'  # eslora 4
    tablero_j1[2:5, 5] = 'O'  # eslora 3
    tablero_j1[-1, 2:5] = 'O'  # eslora 3
    tablero_j1[5, 6:8] = 'O'  # eslora 2
    tablero_j1[-3, 4:6] = 'O'  # eslora 2
    tablero_j1[2:4, 3] = 'O'  # es 2
    tablero_j1[5:6, 2] = 'O'  # es 1
    tablero_j1[2:3, -2] = 'O'  # es 1
    tablero_j1[8:9, -1] = 'O'  # es 1
    tablero_j1[9, 8:9] = 'O'  # es 1

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
