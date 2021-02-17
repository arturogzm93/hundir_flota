import numpy as np
import constants as ct


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


def buscar_coord_jug():
    fila = int(input('Introducir coordenada de la fila: '))
    columna = int(input('Introducir coordenada de la columna: '))

    if tablero_pc1[fila, columna] == 'O':

        global ct.vidas_pc
        ct.vidas_pc -= 1
        tablero_pc1[fila, columna] = 'X'
        tablero_j2[fila, columna] = 'X'
        print('TOCADO')
        print(tablero_j2)

        buscar_coord_jug()

    else:

        tablero_pc1[fila, columna] = 'A'
        tablero_j2[fila, columna] = 'A'
        print('AGUA')
        print(tablero_j2)

        buscar_coord_pc()


def buscar_coord_pc():

    fila = np.random.randint(0, 10)
    columna = np.random.randint(0, 10)

    if tablero_j1[fila, columna] == 'O':

        global ct.vidas_j
        tablero_j1[fila, columna] = 'X'
        tablero_pc2[fila, columna] = 'X'
        print(tablero_pc2)
        ct.vidas_j -= 1

        buscar_coord_pc()

    else:

        tablero_j1[fila, columna] = 'A'
        tablero_pc2[fila, columna] = 'A'
        print(tablero_pc2)

        buscar_coord_jug()