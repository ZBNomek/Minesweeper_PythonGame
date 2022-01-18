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
    print('\t' * 3 + "Modo actual =", mode, "   |   ", "Cuadros Faltantes",
          n, "   |   ", "Banderas colocadas", b)


def game_over_layout(matriz):
    print_matriz(matriz)
    game_over()


def main(key):
    menu_dificultades()  # imprime menu de dificultades
    h: tuple  # lista en donde se almacenan los datos de la dificultad

    # Imput del usurio en para seleccionar la dificultad
    print(('\t'*6)+"      Type 1, 2, 3 or h")
    difficultad = checker_options(
        ("1", "2", "3", "h"), "str", ('\t'*7)+"       ")

    if difficultad == "h":  # Si el el input es 'h', redirecciona al usuario a un menu de ayuda/instrucciones
        help_menu()

    else:  # En otro caso, se obtienen los datos necesarios de la dificultad seleccionada por medio de la siguiente funcion.
        h = dificultad_datos(int(difficultad))

        # Se crean dos matrices para el juego -> Una visible con la que el usuario interactuará, y otra invisible que contiene los datos del juego (minas y demás)
        matriz_invisible = crear_matriz_invisible(h)
        matriz_visible = crear_matriz_visible(h)

        breaker = False  # Variable que controla el loop del juego
        # Modo de juego con el que se empieza el juego (Devido a la estructura del codigo se invierte esta al empezar, por lo que comenzaria con el modo de cavar)
        game_mode = "Bandera"

        while True:  # loop del juego
            game_mode = switch_game_mode(game_mode, "Bandera", "Cavar")

            while True:  # Loop de "modo de juego"

                # Inprime el juego en el terminal con informacion para el jugador.
                if key == True:
                    print_matriz(matriz_invisible)
                game_layout(matriz_visible, game_mode, h[1])

                # Input de usuario para coodenadas / cambio de modo de juego
                modo = tuple_mode_checker()

                if modo == "m":  # Si el input es 'm', rompe el loop del "modo de juego" y cambia el modo de cavar a bandera
                    break

                else:  # En caso de ser una tupla, toma la coordenada en x y en y en donde se realizara una accion dentro del juego.
                    y = int(modo[-1]) - 1
                    x = int(modo[0]) - 1

                # Si el modo de juego está en bandera, pone una bandera en la coordenada dada.
                if game_mode == "Bandera":

                    matriz_visible = flag_visible_map(x, y, matriz_visible)

                else:  # Si el modo de juego es cavar ...

                    # Si en el tablero invisible hay una bomba en la coordenada dada...
                    if matriz_invisible[y][x] == "¤":

                        # Coloca una X en el tablero invisible para marcar donde se equivocó el jugador
                        matriz_invisible[y][x] = "X"

                        # Imprime el tablro invisible para visualizar todas las minas y el menu de Game Over.
                        game_over_layout(matriz_invisible)

                        breaker = True  # Variable que indica roper con el loop del juego
                        break  # Rome el loop de "modo de juego"

                    else:  # Si en el tablero invisible NO hay una bomba en la coordenada dada...

                        # En el tablero visible se remblaza con los datos correspondientes del tablero invisible en la coordenada dada.
                        matriz_visible[y][x] = str(matriz_invisible[y][x])

                fleg = False
                for i in matriz_visible:

                    for e in i:
                        if e != "□":
                            pass
                        else:
                            fleg = True
                            break
                    if fleg == True:
                        break
                if fleg == False:
                    print("u won :D")
                    breaker = True
                    break

            if breaker == True:  # Breaker para acabar con el loop del juego
                break


# ___________________________________________________________________________________

admin_key = False

buscaminas_menu()

while True:
    main(admin_key)
    print("Quieres volver al menú principal? [y/n]")
    breaker = checker_options(("y", "n"), "str", ">")
    if breaker == "n":
        break

good_bye()
