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

        entrada = int(input('\nIntroduzca opción: '))

        if entrada == 2:
            print('\n¡Hasta pronto!')
            break

        elif entrada == 1:
            activar_barcos(contador_barcos, tablero_j1, turno_j)
            activar_barcos(contador_barcos, tablero_pc1, turno_pc)

        else:
            print('\nLa opción no es válida.')
            continue

        while vidas_pc >= 0 or vidas_j >= 0:

            if vidas_j == 0:
                print('\nGame over...')
                tablero_j1 = np.full((10, 10), ' ')
                tablero_j2 = np.full((10, 10), ' ')
                tablero_pc1 = np.full((10, 10), ' ')
                tablero_pc2 = np.full((10, 10), ' ')
                vidas_j = 20
                vidas_pc = 20
                break

            elif vidas_pc == 0:
                print('\n¡Has ganado! Fin del juego.')
                tablero_j1 = np.full((10, 10), ' ')
                tablero_j2 = np.full((10, 10), ' ')
                tablero_pc1 = np.full((10, 10), ' ')
                tablero_pc2 = np.full((10, 10), ' ')
                vidas_j = 20
                vidas_pc = 20
                break

            else:
                print('\nTURNO JUGADOR')

                seguir = input('\nSi quieres seguir pulsa s, de lo contrario pulsa n: ')
                seguir = seguir.lower()

                if seguir == 'n':
                    tablero_j1 = np.full((10, 10), ' ')
                    tablero_j2 = np.full((10, 10), ' ')
                    tablero_pc1 = np.full((10, 10), ' ')
                    tablero_pc2 = np.full((10, 10), ' ')
                    vidas_j = 20
                    vidas_pc = 20
                    break

                elif seguir == 's':
                    print('\nTablero disparos\n', tablero_j2)

                    try:
                        fila = int(input('\nIntroduce fila: '))
                        columna = int(input('Introduce columna: '))

                        disparo = buscar_coord(fila, columna, tablero_pc1, tablero_j2)

                        if disparo == 'Tocado':
                            print('\n¡¡Le has dado!!')
                            print('\nTablero disparos\n', tablero_j2)
                            vidas_pc -= 1
                            continue

                        elif disparo == 'Intentado':
                            print('\nYa has disparado en esa coordenada, vuelve a disparar.')
                            continue

                        elif disparo == 'Agua':
                            print('\n¡AGUA!')
                            print('\nTablero disparos\n', tablero_j2)

                        while vidas_pc > 0:

                            print('\nTURNO PC')
                            time.sleep(3)

                            fila = np.random.randint(10)
                            columna = np.random.randint(10)

                            disparo1 = buscar_coord(fila, columna, tablero_j1, tablero_pc2)

                            if disparo1 == 'Tocado':
                                print('\n¡¡Te ha dado!!')
                                print('\nTablero barcos\n', tablero_j1)
                                vidas_j -= 1
                                continue

                            elif disparo1 == 'Intentado':
                                print('Ya había disparado en esa coordenada, le vuelve a tocar.')
                                continue

                            elif disparo1 == 'Agua':
                                print('\n¡Ha fallado el disparo!')
                                print('\nTablero barcos\n', tablero_j1)
                                break

                    except ValueError:
                        print('\nHas introducido una fila o columna no válida, ' +
                                'vuelve a introducirlas.')
                    except IndexError:
                        print('\nHas introducido una fila o columna no válida, ' +
                                'vuelve a introducirlas.')

    except ValueError:
        print('\nHas escrito una opción no válida. Introduce 1 o 2.')
