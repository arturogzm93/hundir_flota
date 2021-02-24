from utils import buscar_coord, activar_barcos, iniciar_tablero

from constants import vidas_j, vidas_pc, tablero_j1, tablero_j2, tablero_pc1, tablero_pc2
from constants import contador_barcos, turno_j, turno_pc

import time

import numpy as np

from IPython.display import clear_output
clear_output(wait=True)

print('Bienvenido a HUNDIR LA FLOTA')

print('''Instrucciones: Los tableros están definidos.
Cada jugador tiene 10 barcos y un total de 20 vidas.
El jugador tendrá que introducir las coordenadas numéricas a donde quiere disparar.
Las coordenadas van de 0 a 9, tanto en filas como columnas.
Si acierta el disparo podrá volver a disparar, si falla pasará el turno a su rival.
Gana el que hunda todos los barcos del rival.
''')

while True:

    print('''
    1. Empieza el juego.
    2. Salir del juego.
    ''')

    entrada = int(input('Introduzca opción:'))
    if entrada == 2:
        print('¡Hasta pronto!')
        break

    elif entrada == 1:

        #activar_barcos(contador_barcos, tablero_j1, turno_j)
        #activar_barcos(contador_barcos, tablero_pc1, turno_pc)
        iniciar_tablero(tablero_j1, turno_j)
        iniciar_tablero(tablero_pc1, turno_pc)

        while vidas_pc >= 0 or vidas_j >= 0:

            if vidas_j == 0:
                print('Game over')
                tablero_j1 = np.full((10, 10), ' ')
                tablero_j2 = np.full((10, 10), ' ')
                tablero_pc1 = np.full((10, 10), ' ')
                tablero_pc2 = np.full((10, 10), ' ')
                vidas_j = 1
                vidas_pc = 1
                break

            elif vidas_pc == 0:
                print('Final del juego')
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

                seguir = input('Si quieres seguir pulsa s, de lo contrario pulsa n: ')

                if seguir == 'n':
                    break

                elif seguir == 's':
                    print('Tablero disparos JUG\n', tablero_j2)
                    print('\n')
                    print('Tablero barcos JUG\n', tablero_j1)

                    fila = int(input('Introduce fila: '))
                    columna = int(input('Introduce columna: '))

                    disparo = buscar_coord(fila, columna, tablero_pc1, tablero_j2)

                    if disparo == 'Tocado':
                        print('Tablero disparos JUG\n', tablero_j2)
                        print('Tablero barcos PC\n', tablero_pc1)
                        vidas_pc -= 1
                        print('Vidas PC: \n', vidas_pc)

                    elif disparo == 'Intentado':
                        print('Ya has disparado ahí, vuelve a disparar.\n')
                        continue

                    elif disparo == 'Agua':
                        print('Tablero disparos JUG\n', tablero_j2)
                        print('Tablero barcos PC\n', tablero_pc1)

                        while True:

                            time.sleep(2)
                            print('TURNO PC \n')

                            # fila = random.randint(0, 9)
                            # columna = random.randint(0, 9)
                            fila = int(input('Introduce fila: '))
                            columna = int(input('Introduce columna: '))

                            disparo1 = buscar_coord(fila, columna, tablero_j1, tablero_pc2)

                            if disparo1 == 'Tocado':
                                print('Tablero disparos PC\n', tablero_pc2)
                                print('Tablero barcos JUG\n', tablero_j1)
                                vidas_j -= 1
                                print('Vidas jugador: \n', vidas_j)
                                break

                            elif disparo1 == 'Intentado':
                                print('Ya has disparado ahí, vuelve a disparar.\n')
                                continue

                            elif disparo1 == 'Agua':
                                print('Tablero disparos PC\n', tablero_pc2)
                                print('Tablero barcos JUG\n', tablero_j1)
                                break
