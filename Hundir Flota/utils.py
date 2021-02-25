import numpy as np

import random


def activar_barcos(contador, tablero, turno):
    '''
    Pide al jugador introducir los barcos. Usando un contador dentro de un bucle
    se gestionan las esloras que se tienen que poner. Así como las funciones que
    que debe ejecutar el pc y el jugador.

    :param contador: cada vez que se pone un barco, se cuenta 1, para cambiar de
    esloras.
    :param tablero: indica el tablero que se va a modificar.
    :param turno: indica que si es el tablero del jugador o del pc el que se va
    a modificar, teniendo cada uno sus funciones.
    '''

    while contador < 10:

        if turno == 'jug':

            try:

                if contador < 4:
                    eslora = 1
                    print(tablero)
                    print('\nIntroduce un barco de una eslora.\n')
                    contador = poner_barcos(eslora, contador, tablero, turno)

                elif contador < 7:
                    eslora = 2
                    print(tablero)
                    print('\nIntroduce un barco de dos esloras.\n')
                    contador = poner_barcos(eslora, contador, tablero, turno)

                elif contador < 9:
                    eslora = 3
                    print(tablero)
                    print('\nIntroduce un barco de tres esloras.\n')
                    contador = poner_barcos(eslora, contador, tablero, turno)

                else:
                    eslora = 4
                    print(tablero)
                    print('\nIntroduce un barco de cuatro esloras.\n')
                    contador = poner_barcos(eslora, contador, tablero, turno)
                    print(tablero)
                    print('Has puesto todos los barcos, ¡empieza la partida!\n')

            except ValueError:
                print('\nCoordenada mal introducida, vuelve a intentarlo.\n')
                continue
            except IndexError:
                print('\nCoordenada mal introducida, vuelve a intentarlo.\n')
                continue


        elif turno == 'pc':
            if contador < 4:
                eslora = 1
                contador = poner_barcos(eslora, contador, tablero, turno)

            elif contador < 7:
                eslora = 2
                contador = poner_barcos(eslora, contador, tablero, turno)

            elif contador < 9:
                eslora = 3
                contador = poner_barcos(eslora, contador, tablero, turno)

            else:
                eslora = 4
                contador = poner_barcos(eslora, contador, tablero, turno)


def poner_barcos(eslora, contador, tablero, turno):
    '''
    Se encuentra dentro de la función activar_barcos y en función de la eslora,
    pide al jugador que indique coordenadas para 1 una sola eslora y para el resto,
    que indique también la orientación en la que quiere poner el barco. Una vez
    ejecutada, si está correcta, devolverá una O por el número de esloras en la posición
    indicada.
    :param eslora: número de posiciones que tiene el barco.
    :param contador: si pone una eslora, cuenta uno para que la función activar_barcos
    sepa cuantas esloras tiene que pedir al usuario.
    :param tablero: tablero del jugador o del pc a modificar.
    :param turno: del jugador o del pc para que sepa que funciones ejecutar.
    :return: devuelve contador para que siga contando en la función activar_barcos.
    '''

    if eslora == 1 and turno == 'jug':

        fila = int(input('Coordenada fila: '))
        col = int(input('Coordenada columna: '))

        if 'O' not in tablero[fila, col]:
            tablero[fila, col] = 'O'
            contador += 1
            return contador

        else:
            print('Ya hay un barco o te has salido del tablero.\n')

    else:
        if turno == 'jug':
            fila = int(input('Coordenada fila: '))
            col = int(input('Coordenada columna: '))
            orient = input('Coordenada N, S, E, O: ')
            orient = orient.lower()

        elif turno == 'pc':
            orient = random.choice(['n', 's', 'e', 'o'])
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
                if turno == 'jug':
                    print('\nYa hay un barco o te has salido del tablero.')
                    return contador

                else:
                    return contador


def buscar_coord(fila, columna, tablero_1, tablero_2):
    '''
    Busca en las coordenadas indicadas fuera de la función por el jugador o el pc
    en automático, y busca en el tablero para disparar. Si hay una O la cambia por
    una X de tocado, si no hay nada por A de agua, y si ya hay agua le dejará volver
    a tirar.
    :param fila: coordenada de las filas.
    :param columna: coordenada de las columnas.
    :param tablero_1: tablero de barcos del jugador o pc a modificar.
    :param tablero_2: tablero de barcos del jugador o pc a modificar.
    :return: Devuelve Tocado, Agua o Intentado como se explica al principio.
    '''

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
