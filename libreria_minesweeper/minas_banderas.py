from random import choice


def apply_mines(number_of_mines: int, array: list) -> list:
    n = 0
    while number_of_mines > n:
        coordenada = choice([[i, j]for i, x in enumerate(array[:-1])
                             for j, y in enumerate(x[:-1])if not y])
        array[coordenada[0]][coordenada[1]] = "¤"
        n += 1
    return array


def number_mines_in_area(array: list):
    coordinates_for_numbers = []
    mine_coordinates = [(y, x)for y, i in enumerate(
        array)for x, e in enumerate(i) if e == "¤"]
    for i in mine_coordinates:
        set_of_coordinates = []
        # Arriba
        y = i[0]+1
        x = i[1]
        if y >= 0 and x >= 0:
            if (y, x) not in mine_coordinates:
                set_of_coordinates.append((y, x))
        y = i[0]+1
        x = i[1]+1
        if y >= 0 and x >= 0:
            if (y, x) not in mine_coordinates:
                set_of_coordinates.append((y, x))
        y = i[0]+1
        x = i[1]-1
        if y >= 0 and x >= 0:
            if (y, x) not in mine_coordinates:
                set_of_coordinates.append((y, x))
        # Abajo
        y = i[0]-1
        x = i[1]
        if y >= 0 and x >= 0:
            if (y, x) not in mine_coordinates:
                set_of_coordinates.append((y, x))
        y = i[0]-1
        x = i[1]+1
        if y >= 0 and x >= 0:
            if (y, x) not in mine_coordinates:
                set_of_coordinates.append((y, x))
        y = i[0]-1
        x = i[1]-1
        if y >= 0 and x >= 0:
            if (y, x) not in mine_coordinates:
                set_of_coordinates.append((y, x))
        # Derecha
        y = i[0]
        x = i[1]+1
        if y >= 0 and x >= 0:
            if (y, x) not in mine_coordinates:
                set_of_coordinates.append((y, x))
        # Izquerda
        y = i[0]
        x = i[1]-1
        if y >= 0 and x >= 0:
            if (y, x) not in mine_coordinates:
                set_of_coordinates.append((y, x))

        coordinates_for_numbers.append(set_of_coordinates)
    for i in coordinates_for_numbers:
        for e in i:
            try:
                array[e[0]][e[1]] += 1
            except:
                TypeError
    return array


def flag_visible_map(x, y, array):
    try:
        if array[y][x] == "□":
            array[y][x] = "f"
        elif array[y][x] == "f":
            array[y][x] = "□"
        elif array[y][x] == " ":
            print("coordinate out of range")
        else:
            print("not valid")
    except:
        IndexError
        print("coordinate out of range")

    return array


def switch_game_mode(current_mode, mode_1, mode_2):
    if current_mode == mode_1:
        current_mode = mode_2
    else:
        current_mode = mode_1
    return current_mode
