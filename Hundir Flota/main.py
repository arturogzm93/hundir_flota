import random

import barcos

from utils import iniciar_tablero, buscar_coord, activar_barcos

from constants import vidas_j, vidas_pc, count, tablero_j1, tablero_j2, tablero_pc1, tablero_pc2

import time

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

        activar_barcos()
        iniciar_tablero()

        while vidas_pc >= 0 or vidas_j >= 0:

            if vidas_j == 0:
                print('Game over')
                break

            elif vidas_pc == 0:
                print('Final del juego')
                break

            else:
                print('\n')
                print('TURNO JUGADOR \n')

                seguir = input('Si quieres seguir pulsa s, de lo contrario pulsa n: ')

                if seguir == 'n':
                    break

                elif seguir == 's':
                    print('Tablero disparos\n', tablero_j2)
                    print('\n')
                    print('Tablero barcos\n', tablero_j1)

                    turno = 'jugador_1'
                    fila = int(input('Introduce fila: '))
                    columna = int(input('Introduce columna: '))

                    disparo = buscar_coord(turno, fila, columna)

                    if disparo == 'Tocado':
                        print('Tablero disparos J\n', tablero_j2)
                        print('Tablero PC\n', tablero_pc1)
                        vidas_pc -= 1
                        print('Vidas PC: \n', vidas_pc)

                    elif disparo == 'Intentado':
                        print('Ya has disparado ahí, vuelve a disparar.\n')
                        continue

                    else:
                        print('Tablero disparos J\n', tablero_j2)
                        print('Tablero PC\n', tablero_pc1)

                        while vidas_j > 0 and count <= 3:

                            time.sleep(2)
                            print('TURNO PC \n')

                            turno = 'pc_1'
                            # fila = random.randint(0, 9)
                            # columna = random.randint(0, 9)
                            fila = int(input('Introduce fila: '))
                            columna = int(input('Introduce columna: '))

                            disparo = buscar_coord(turno, fila, columna)

                            if disparo == 'Agua' and count < 2:
                                count += 1
                                print('Sigue intentando ', count)

                            elif disparo == 'Agua' and count < 3:
                                tablero_pc2[fila, columna] = 'A'
                                tablero_j1[fila, columna] = 'A'
                                print('Tablero disparos PC\n', tablero_pc2)
                                print('Tablero JUG\n', tablero_j1)
                                print('Final ', count)
                                break

                            elif disparo == 'Intentado':
                                print('intentado ', count)

                            elif disparo == 'Tocado':
                                print('Tablero disparos J\n', tablero_j2)
                                print('Tablero PC\n', tablero_pc1)
                                vidas_j -= 1
                                print('Vidas jugador: \n', vidas_j)
                                break