import numpy as np
from constants import tablero_j1, tablero_j2, tablero_pc1, tablero_pc2, vidas_j, vidas_pc
import time
from IPython.display import clear_output
clear_output(wait=True)


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
    tablero_pc1[9, 0] = 'O'  # es 1
    tablero_pc1[9, 4] = 'O'  # es 1
    tablero_pc1[4, 9] = 'O'  # es 1


def buscar_coord(tablero_j1, tablero_pc1, tablero_j2, vidas_pc, vidas_j):

    print('TABLERO JUGADOR\n', tablero_j1)
    print('\n')
    print('TABLERO DISPAROS\n', tablero_j2)

    if tablero_pc1[fila, columna] == 'O':

        vidas_pc -= 1
        tablero_pc1[fila, columna] = 'X'
        tablero_j2[fila, columna] = 'X'
        print('TOCADO')
        print(tablero_j2)

        clear_output()
        buscar_coord_jug()

    else:

        tablero_pc1[fila, columna] = 'A'
        tablero_j2[fila, columna] = 'A'
        print('AGUA')
        print(tablero_j2)

        clear_output()
        buscar_coord_pc()


def buscar_coord_pc():
    time.sleep(2)
    fila = np.random.randint(0, 10)
    columna = np.random.randint(0, 10)

    if tablero_j1[fila, columna] == 'O':

        global vidas_j
        tablero_j1[fila, columna] = 'X'
        tablero_pc2[fila, columna] = 'X'
        print(tablero_pc2)
        vidas_j -= 1

        clear_output()
        buscar_coord_pc()

    else:

        tablero_j1[fila, columna] = 'A'
        tablero_pc2[fila, columna] = 'A'
        print(tablero_pc2)

        clear_output()
        buscar_coord_jug()