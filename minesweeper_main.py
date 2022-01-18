from libreria_minesweeper.matrices import *
from libreria_minesweeper.minas_banderas import *
from libreria_minesweeper.checkers import *
from libreria_minesweeper.ascii import *


def dificultad_datos(x: int):
    h: tuple
    m: int
    if x == 1:
        h = 5
        m = 6
    elif x == 2:
        h = 10
        m = 24
    elif x == 3:
        h = 15
        m = 54
    return h, m


def crear_matriz_invisible(h):
    matriz: list = crear_matriz(h[0], h[0], 0)
    matriz = apply_mines(h[1], matriz)
    matriz = number_mines_in_area(matriz)
    return matriz


def crear_matriz_visible(h):
    matriz: list = crear_matriz(h[0], h[0], "□")
    return matriz


def game_layout(matriz_vis: list, mode: str, b: int):
    print_matriz(matriz_vis)
    n = 0
    for i in matriz_vis:
        for e in i:
            if e == "f":
                b -= 1
            elif e == "□":
                n += 1
    print("Modo actual =", mode, "   |   ", "Cuadros Faltantes",
          n, "   |   ", "Banderas colocadas", b)


def game_over_layout(matriz):
    print_matriz(matriz)
    game_over()


def main():
    menu_dificultades()
    h = []
    difficultad = checker_options(
        ("1", "2", "3", "h"), "str", "Type 1, 2, 3 or h -> ")

    if difficultad == "h":
        help_menu()

    else:
        h = dificultad_datos(int(difficultad))

        matriz_invisible = crear_matriz_invisible(h)
        matriz_visible = crear_matriz_visible(h)

        breaker = False
        game_mode = "Bandera"

        while True:
            game_mode = switch_game_mode(game_mode, "Bandera", "Cavar")
            while True:
                game_layout(matriz_visible, game_mode, h[1])
                x = tuple_mode_checker()
                if x == "m":
                    break
                else:
                    y = int(x[-1]) - 1
                    x = int(x[0]) - 1

                if game_mode == "Bandera":
                    matriz_visible = flag_visible_map(x, y, matriz_visible)
                else:

                    if matriz_invisible[y][x] == "¤":
                        matriz_invisible[y][x] = "X"

                        game_over_layout(matriz_invisible)

                        breaker = True
                        break

                    else:
                        matriz_visible[y][x] = str(matriz_invisible[y][x])

            if breaker == True:
                break


# ___________________________________________________________________________________

buscaminas_menu()

while True:
    main()
    print("Quieres volver al menú principal? [y/n]")
    breaker = checker_options(("y", "n"), "str", ">")
    if breaker == "n":
        break

good_bye()
