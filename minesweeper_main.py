from random import choice


h = 10 ,10
m = 10


def print_matriz(matriz: list) -> None:
    print('\n'.join([' '.join([str(cell) for cell in row])
          for row in matriz]))

def crear_matriz(x:int,y:int,symbol) -> list:
    matriz = []
    for e in range(y):
        a = []
        for i in range(x):
            a.append(symbol)
        matriz.append(a)
    return matriz

def apply_mines(number_of_mines: int, array: list) -> list:
    n = 0
    while number_of_mines > n:
        coordenada = choice([[i, j]for i, x in enumerate(array[:-1])
                         for j, y in enumerate(x[:-1])if not y])
        array[coordenada[0]][coordenada[1]] = "m"
        n += 1
    return array

def number_mines_in_area(array: list):
    coordinates_for_numbers = []
    mine_coordinates = [(y, x)for y, i in enumerate(
        array)for x, e in enumerate(i) if e == "m"]
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
            array[y][x] = "🏳"
        elif array[y][x] == "🏳":
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

matriz_invisible = crear_matriz(h[0],h[1],0)
matriz_invisible = apply_mines(10,matriz_invisible)
matriz_invisible = number_mines_in_area(matriz_invisible)

matriz_visible = crear_matriz(h[0],h[1],"□")

breaker = False
game_mode = "flag"

while True:
    game_mode = switch_game_mode(game_mode, "flag", "dig")
    while True:
        print_matriz(matriz_visible)
        print("current mode = ",game_mode)
        
        x = input("x ->")
        if x == "mode":
            break
        else:
            x = int(x)
            x -= 1
        y = input("y ->")
        if y == "mode":
            break
        else:
            y = int(y)
            y -= 1
        
        if game_mode == "flag":
            matriz_visible = flag_visible_map(x, y, matriz_visible)
        else:

            if matriz_invisible[y][x] == "m":

                matriz_invisible[y][x]= "X"
                print_matriz(matriz_invisible)
                print("game over")
                breaker = True
                break

            else:
                matriz_visible[y][x]= matriz_invisible[y][x]

    if breaker == True:
        break