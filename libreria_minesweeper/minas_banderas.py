from enum import Flag
from random import choice


def colocar_minas(numero_de_minas: int, matriz: list) -> list:
    n = 0

    while numero_de_minas > n:
        coordenada = choice([[i, j] for i, x in enumerate(matriz[:-1])
                            for j, y in enumerate(x[:-1])if not y])
        matriz[coordenada[0]][coordenada[1]] = "¤"
        n += 1

    return matriz


def cant_minas(matriz: list) -> list:
    coordenadas_numeros: list = []

    coordenadas_minas: list = [(y, x)for y, i in enumerate(matriz)
                               for x, e in enumerate(i) if e == "¤"]

    for i in coordenadas_minas:
        set_coordenadas: list = []

        indices_y: tuple = (-1, 0, 1)
        indices_x: tuple = (-1, 0, 1)

        mina_y: int = i[0]
        mina_x: int = i[1]

        for i in indices_y:
            for e in indices_x:
                flag = False
                y = mina_y + i
                x = mina_x + e
                if i == 0:
                    if i == e:
                        flag = True
                if not flag:
                    if y >= 0 and x >= 0:
                        set_coordenadas.append((y, x))
        coordenadas_numeros.append(set_coordenadas)

    for i in coordenadas_numeros:
        for e in i:
            try:
                matriz[e[0]][e[1]] += 1
            except TypeError:
                pass

    return matriz


def flag_visible_map(y, x, matriz) -> list:
    try:
        if matriz[y][x] == "□":
            matriz[y][x] = "f"
        elif matriz[y][x] == "f":
            matriz[y][x] = "□"
        else:
            print("RangeError: Input fuera del rango")

    except IndexError:
        print("RangeError: Input fuera del rango")

    return matriz


def switch_game_mode(current_mode: str, mode_1: str, mode_2: str) -> str:
    if current_mode == mode_1:
        current_mode = mode_2
    else:
        current_mode = mode_1
    return current_mode
