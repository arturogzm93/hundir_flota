from constants import tablero_j1, tablero_j2, tablero_pc1, tablero_pc2, vidas_j, vidas_pc
import utils as ut
import numpy as np
from IPython.display import clear_output
clear_output(wait=True)

print('Bienvenido a HUNDIR LA FLOTA')
print('''Instrucciones: Los tableros están definidos.
Cada jugador tiene 10 barcos y un total de 20 vidas.
El jugador tendrá que introducir las coordenadas numéricas a donde quiere disparar.
Si acierta el disparo podrá volver a disparar, si falla pasará el turno a su rival.
Gana el que hunda todos los barcos del rival.
''')

ut.iniciar_tablero()

while vidas_j > 0 or vidas_pc > 0:

    print('''
    1. Empieza el juego.
    2. Salir del juego.
    ''')

    entrada = int(input('Introduzca opción:'))
    if entrada == 2:
        print('¡Hasta pronto!')
        break
    elif entrada == 1:

        print('TABLERO JUGADOR\n', tablero_j1)
        print('\n')
        print('TABLERO DISPAROS\n', tablero_j2)

        fila = int(input('Introduce fila: '))
        columna = int(input('Introduce columna: '))

        buscar_coord(fila, columna)



