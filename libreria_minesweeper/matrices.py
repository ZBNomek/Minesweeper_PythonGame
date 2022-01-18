from nntplib import GroupInfo
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


def print_old(matriz: list) -> None:
    print('\n'.join(['\t'.join([str(cell) for cell in row])
          for row in matriz]))


"""
    n = 1
    for i in matriz:
        print(str(n), " ".join(str(num)for num in i))
        n += 1
    indices_X = []
    for i in range(len(matriz[-1])):
        indices_X.append(i+1)

    print(" ", " ".join(str(num)for num in indices_X))
    #t = ""+str(n)
    #print(t.join(str(cell) for cell in matriz))
    # print(''.join([' '.join([str(cell) for cell in row])
    # for row in matriz]))
"""


def crear_matriz(x: int, y: int, symbol) -> list:
    matriz = []
    for e in range(y):
        a = []
        for i in range(x):
            a.append(symbol)
        matriz.append(a)
    return matriz


def print_matriz(grid):

    gridsize = len(grid[-1])

    tab: str = ""

    if gridsize == 5:
        tab = ('\t' * 6) + "  "
    elif gridsize == 10:
        tab = ('\t' * 5)
    elif gridsize == 15:
        tab = ('\t' * 4)

    horizontal = '   ' + (4 * gridsize * '-') + '-'

    # Print top column letters
    toplabel = '    '

    for i in range(gridsize):
        if i < 9:
            toplabel = toplabel + str(i+1) + '   '
        else:
            toplabel = toplabel + str(i+1) + '  '

    print(tab+toplabel + '\n' + tab+horizontal)

    # Print left row numbers

    for x, y in enumerate(grid):
        if x <= 8:
            row = str(x+1) + ' |'
        else:
            row = str(x+1) + '|'
        #row = '{0:2} |'.format(Fore.RED + str(x))
        for i in y:
            i = str(i)
            if i == "0":
                f = Fore.WHITE
            elif i == "1":
                f = Fore.BLUE
            elif i == "2":
                f = Fore.GREEN
            elif i == "3":
                f = Fore.YELLOW
            elif i == "4":
                f = Fore.MAGENTA
            elif i == "5":
                f = Fore.CYAN
            elif i == "6":
                f = Fore.LIGHTGREEN_EX
            elif i == "7":
                f = Fore.WHITE
            elif i == "8":
                f = Fore.LIGHTCYAN_EX
            elif i == "f":
                f = Fore.RED
            elif i == "X":
                f = Fore.RED + Style.BRIGHT
            elif i == "¤":
                f = Fore.RED
            else:
                f = Fore.BLACK

            row = row + ' ' + f + i + Fore.RESET + Style.NORMAL + ' |'
        print(tab+row + '\n' + tab+horizontal)
    print('')


a = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

print_matriz(a)
