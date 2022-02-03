import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


def crear_matriz(x: int, y: int, cell_symbol: object) -> list:
    matriz = []
    for i in range(y):
        matriz_in = []
        for e in range(x):
            matriz_in.append(cell_symbol)
        matriz.append(matriz_in)
    return matriz


def print_matriz(matriz) -> None:

    tamano_matriz: int = len(matriz[-1])

    tab: str = ""
    if tamano_matriz == 5:
        tab = ('\t' * 6) + "    "
    elif tamano_matriz == 10:
        tab = ('\t' * 5) + "  "
    elif tamano_matriz == 15:
        tab = ('\t' * 4)+" "
    elif tamano_matriz == 3:
        tab = ('\t' * 7)

    # Linea horizontal para la cuadricula
    lineas_horizontales: str = '   ' + (4 * tamano_matriz * '-') + '-'
    indice_columnas: str = '    '

    # linea horizontal + indices de las columnas
    for i in range(tamano_matriz):
        if i < 9:
            indice_columnas += str(i+1) + '   '
        else:
            indice_columnas += str(i+1) + '  '

    print(tab + indice_columnas + '\n' + tab + lineas_horizontales)

    # datos almacenados en las filas + color
    color: str
    for x, y in enumerate(matriz):

        fila: str
        if x <= 8:
            fila = str(x+1) + ' |'
        else:
            fila = str(x+1) + '|'

        # color dependiendo del numero de minas
        for i in y:
            i = str(i)
            if i == "0":
                color = Fore.WHITE
            elif i == "1":
                color = Fore.BLUE
            elif i == "2":
                color = Fore.GREEN
            elif i == "3":
                color = Fore.YELLOW
            elif i == "4":
                color = Fore.MAGENTA
            elif i == "5":
                color = Fore.CYAN
            elif i == "6":
                color = Fore.LIGHTGREEN_EX
            elif i == "7":
                color = Fore.WHITE
            elif i == "8":
                color = Fore.LIGHTCYAN_EX
            elif i == "color":
                color = Fore.RED
            elif i == "X":
                color = Fore.RED + Style.BRIGHT
            elif i == "¤":
                color = Fore.RED
            elif i == "f":
                color = Fore.RED
            else:
                color = Fore.BLACK

            # Datos + lineas verticales de la cuadricula
            fila = fila + ' ' + color + i + Fore.RESET + Style.NORMAL + ' |'

        # Datos + lineas horizontales
        print(tab+fila + '\n' + tab+lineas_horizontales)
    print('')
