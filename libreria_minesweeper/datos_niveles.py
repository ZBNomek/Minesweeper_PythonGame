def datos_dificultad(nivel: int):
    dimension_cuadrada: tuple
    minas: int
    if nivel == 1:
        dimension_cuadrada = 5
        minas = 6
    elif nivel == 2:
        dimension_cuadrada = 10
        minas = 24
    elif nivel == 3:
        dimension_cuadrada = 15
        minas = 54
    elif nivel == 2534803:
        dimension_cuadrada = 3
        minas = 2

    return dimension_cuadrada, minas
