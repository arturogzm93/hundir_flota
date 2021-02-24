from utils import buscar_coord, activar_barcos

from constants import vidas_j, vidas_pc, tablero_j1, tablero_j2, tablero_pc1, tablero_pc2
from constants import turno_j, turno_pc, contador_barcos, men_bienvenida, men_instrucciones

import time

import numpy as np

print(men_bienvenida)

print(men_instrucciones)

while True:

    print('''
    1. Empieza el juego.\n
    2. Salir del juego.
    ''')

    try:

        entrada = int(input('Introduzca opción:\n'))

        if entrada == 2:
            print('¡Hasta pronto!\n')
            break

        elif entrada == 1:
            activar_barcos(contador_barcos, tablero_j1, turno_j)
            activar_barcos(contador_barcos, tablero_pc1, turno_pc)

        else:
            print('La opción no es válida.\n')
            continue

        while vidas_pc >= 0 or vidas_j >= 0:

            if vidas_j == 0:
                print('Game over\n')
                tablero_j1 = np.full((10, 10), ' ')
                tablero_j2 = np.full((10, 10), ' ')
                tablero_pc1 = np.full((10, 10), ' ')
                tablero_pc2 = np.full((10, 10), ' ')
                vidas_j = 1
                vidas_pc = 1
                break

            elif vidas_pc == 0:
                print('¡Has ganado! Fin del juego.\n')
                tablero_j1 = np.full((10, 10), ' ')
                tablero_j2 = np.full((10, 10), ' ')
                tablero_pc1 = np.full((10, 10), ' ')
                tablero_pc2 = np.full((10, 10), ' ')
                vidas_j = 1
                vidas_pc = 1
                break

            else:
                print('\n')
                print('TURNO JUGADOR \n')

                seguir = input('Si quieres seguir pulsa s, de lo contrario pulsa n: \n')
                seguir = seguir.lower()

                if seguir == 'n':
                    break

                elif seguir == 's':
                    print('Tablero disparos.\n', tablero_j2)
                    print('\n')
                    print('Tablero barcos.\n', tablero_j1)

                    try:
                        fila = int(input('Introduce fila: '))
                        columna = int(input('Introduce columna: '))

                        disparo = buscar_coord(fila, columna, tablero_pc1, tablero_j2)

                        if disparo == 'Tocado':
                            print('Tablero disparos JUG\n', tablero_j2)
                            vidas_pc -= 1

                        elif disparo == 'Intentado':
                            print('Ya has disparado ahí, vuelve a disparar.\n')
                            continue

                        elif disparo == 'Agua':
                            print('¡AGUA!\n')
                            print('Tablero disparos JUG\n', tablero_j2)

                        while vidas_pc > 0:

                            time.sleep(2)
                            print('TURNO PC\n')

                            fila = int(input('Introduce fila: '))
                            columna = int(input('Introduce columna: '))

                            disparo1 = buscar_coord(fila, columna, tablero_j1, tablero_pc2)

                            if disparo1 == 'Tocado':
                                print('Tablero barcos JUG\n', tablero_j1)
                                vidas_j -= 1
                                break

                            elif disparo1 == 'Intentado':
                                print('Ya has disparado ahí, vuelve a disparar.\n')
                                continue

                            elif disparo1 == 'Agua':
                                print('Tablero barcos JUG\n', tablero_j1)
                                break

                    except ValueError:
                        print('Has introducido una fila o columna no válida,\
                         vuelve a introducirlas.')
                    except IndexError:
                        print('Has introducido una fila o columna no válida,\
                         vuelve a introducirlas.')

    except ValueError:
        print('Has escrito una opción no válida. Introduce 1 o 2.')
