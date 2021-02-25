import numpy as np

tablero_j1 = np.full((10, 10), ' ')
tablero_j2 = np.full((10, 10), ' ')
tablero_pc1 = np.full((10, 10), ' ')
tablero_pc2 = np.full((10, 10), ' ')

vidas_j = 20
vidas_pc = 20
turno_j = 'jug'
turno_pc = 'pc'
contador_barcos = 0

eslora_1 = 1
eslora_2 = 2
eslora_3 = 3
eslora_4 = 4


men_bienvenida = ('''
,-----.  ,--.                                     ,--.   ,--.
|  |) /_ `--' ,---. ,--,--,--.  ,--.,---. ,--,--, `--' ,-|  | ,---.      ,--,--.
|  .-.  \,--.| .-. :|      \  `'  /| .-. :|      \,--.' .-. || .-. |    ' ,-.  |
|  '--' /|  |\   --.|  ||  |\    / \   --.|  ||  ||  |\ `-' |' '-' '    \ '-'  |
`------' `--' `----'`--''--' `--'   `----'`--''--'`--' `---'  `---'      `--`--'


,--.  ,--.,--. ,--.,--.  ,--.,------.  ,--.,------.     ,--.     ,---.      ,------.,--.    ,-----.,--------. ,---.
|  '--'  ||  | |  ||  ,'.|  ||  .-.  \ |  ||  .--. '    |  |    /  O  \     |  .---'|  |   '  .-.  '--.  .--'/  O  \
|  .--.  ||  | |  ||  |' '  ||  |  \  :|  ||  '--'.'    |  |   |  .-.  |    |  `--, |  |   |  | |  |  |  |  |  .-.  |
|  |  |  |'  '-'  '|  | `   ||  '--'  /|  ||  |\  \     |  '--.|  | |  |    |  |`   |  '--.'  '-'  '  |  |  |  | |  |
`--'  `--' `-----' `--'  `--'`-------' `--'`--' '--'    `-----'`--' `--'    `--'    `-----' `-----'   `--'  `--' `--' 
''')

men_instrucciones = ('''Instrucciones:\n
   - Los tableros están definidos.\n
   - Cada jugador tiene 10 barcos y un total de 20 vidas.\n
   - El jugador tendrá que introducir las coordenadas numéricas a donde quiere disparar.\n
   - Las coordenadas van de 0 a 9, tanto en filas como columnas.\n
   - Si acierta el disparo podrá volver a disparar, si falla pasará el turno a su rival.\n
   - Gana el que hunda todos los barcos del rival.\n ''')

