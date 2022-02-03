from libreria_minesweeper.matrices import *
from libreria_minesweeper.minas_banderas import *
from libreria_minesweeper.verificadores import *
from libreria_minesweeper.ascii import *
from libreria_minesweeper.datos_niveles import *


# Creación del los mapas

def crear_matriz_invisible(datos_dificultad: tuple) -> list:
    matriz: list = crear_matriz(datos_dificultad[0], datos_dificultad[0], 0)
    matriz = colocar_minas(datos_dificultad[1], matriz)
    matriz = cant_minas(matriz)
    return matriz


def crear_matriz_visible(datos_dificultad: tuple) -> list:
    matriz: list = crear_matriz(datos_dificultad[0], datos_dificultad[0], "□")
    return matriz


# Menús que dependen del juego

def menu_dentro_del_juego(matriz_vis: list, modo: str, banderas_sin_colocar: int) -> None:
    print_matriz(matriz_vis)
    cuadrados = 0
    for i in matriz_vis:
        for e in i:
            if e == "f":
                banderas_sin_colocar -= 1
            elif e == "□":
                cuadrados += 1
    print('\t' * 3 + "   Modo actual =", modo, "   |   ", "Cuadros Faltantes",
          cuadrados, "   |   ", "Banderas sin colocar", banderas_sin_colocar)


def menu_game_over(matriz) -> None:
    print_matriz(matriz)
    game_over()


# Organización del juego
def main(key) -> None:

    datos_juego: tuple  # lista en donde se almacenan los datos de la dificultad

# ----------------------------------------Menu Principal----------------------------------------

    menu_dificultades()
    print(('\t'*6)+"      Type 1, 2, 3 or h")
    difficultad: str = verificador(
        "str", ("1", "2", "3", "h", "2534803"), '\t'*7 + "     >")

    if difficultad == "h":  # Si el el input es 'h', redirecciona al usuario a un menu de ayuda/instrucciones
        help_menu()

    else:  # En otro caso, se obtienen los datos necesarios de la dificultad seleccionada por medio de la siguiente funcion.
        datos_juego = datos_dificultad(int(difficultad))

# -----------------------------------Creación del mapa de juego-----------------------------------

        # Se crean dos matrices para el juego -> Una visible con la que el usuario interactuará, y otra invisible que contiene los datos del juego (minas y demás)
        matriz_invisible: list = crear_matriz_invisible(datos_juego)
        matriz_visible: list = crear_matriz_visible(datos_juego)

        breaker: bool = False  # Variable que controla el loop del juego

        # Modo de juego con el que se empieza el juego (Devido a la estructura del codigo se invierte esta al empezar, por lo que comenzaria con el modo de cavar.)
        modo_de_juego: str = "Bandera"


# <<>><<>><<>><<>><<>><<>><<>><<>><<>|Inicio Loop de la partida|<<>><<>><<>><<>><<>><<>><<>><<>><<>

        while True:  # loop del juego
            modo_de_juego = switch_game_mode(modo_de_juego, "Bandera", "Cavar")

            while True:  # Loop de "modo de juego"

                # -----------------------------------Imprimir juego en terminal-----------------------------------

                if key == True:
                    print_matriz(matriz_invisible)

                # Imprime el juego en el terminal con informacion para el jugador.
                menu_dentro_del_juego(
                    matriz_visible, modo_de_juego, datos_juego[1])

# --------------------------------------Input del usuario--------------------------------------

                # Input de usuario para coodenadas / cambio de modo de juego
                modo = tupla_o_modo('\t'*7 + "     >")

                if modo == "m":  # Si el input es 'm', rompe el loop del "modo de juego" y cambia el modo de cavar a bandera
                    break

                else:  # En caso de ser una tupla, toma la coordenada en x y en y en donde se realizara una accion dentro del juego.
                    y = int(modo[-1]) - 1
                    x = int(modo[0]) - 1

# -------------------------------------Acciones en el tablero-------------------------------------

                # Si el modo de juego está en bandera, pone una bandera en la coordenada dada.
                if modo_de_juego == "Bandera":
                    matriz_visible = flag_visible_map(y, x, matriz_visible)

                else:  # Si el modo de juego es cavar ...

                    # Si en el tablero invisible NO hay una bomba en la coordenada dada...
                    if matriz_invisible[y][x] != "¤":

                        # En el tablero visible se remblaza con los datos correspondientes del tablero invisible en la coordenada dada.
                        matriz_visible[y][x] = str(matriz_invisible[y][x])

# ------------------------------Verificar Bomba Detonada (GAME OVER)------------------------------

                    else:  # Si en el tablero invisible hay una bomba en la coordenada dada...

                        # Coloca una X en el tablero invisible para marcar donde se equivocó el jugador
                        matriz_invisible[y][x] = "X"

                        # Imprime el tablro invisible para visualizar todas las minas y el menu de Game Over.
                        menu_game_over(matriz_invisible)

                        breaker = True  # Variable que indica roper con el loop del juego
                        break  # Rome el loop de "modo de juego"

# --------------------------Verificar si el tablero ya está limpio (U WON!!!)-------------------------------

                flag = False
                for i in matriz_visible:

                    for e in i:
                        if e != "□":
                            pass
                        else:
                            flag = True
                            break
                    if flag == True:
                        break
                if flag == False:
                    win()
                    breaker = True
                    break

            if breaker == True:  # Breaker para acabar con el loop del juego
                break
