"""
Esta parte son funciones que sirven para filtrar informacion de los 
inputs para que desta manera no hayan errores y muestren el el terminar
al usuario el error de su input, repitiendo esto hata que el usuario
ingrese un input valido y sirve con datos tipo str y  int, pero pueden
ser ampliados a más.
"""


# Verificar si el input es una tupla con elementos int, o en su defecto str = "m"
from time import process_time_ns


def tupla_o_modo(pre_text: int = ">") -> object:

    while True:
        flag: bool = True
        print()
        user_input: str = input(pre_text)
        print()
        user_input.lower()

        if user_input == "m":
            pass
        else:
            user_input: list = user_input.split(",")

            if len(user_input) == 2:
                for i in user_input:
                    try:
                        i = int(i)
                    except ValueError:
                        print("ValueError: Tipo de dato ingresado no valido.")
                        flag = False
                        break

                if flag == True:
                    for i in user_input:
                        if int(i) <= 0:
                            print("RangeError: Input fuera del rango")
                            flag = False
                            break
            else:
                flag = False
                print(
                    "ValueError: El input debe ser 'm' o dos numeros separados por una coma -> #,#")

            if flag == True:
                user_input: tuple = user_input[0], user_input[1]

        if flag == True:
            break

    return user_input

# Verifica si el input cumple con ciertos condicionales


def verificador(data_type: str, options: tuple = None, pre_text: str = ">") -> str:

    while True:
        flag_datatype: bool = True
        flag_option: bool = True
        print()
        user_input: str = input(pre_text)
        print()

        if data_type == 'int':
            try:
                user_input: int = int(user_input)
                if options:
                    for i in options:
                        if user_input == i:
                            flag_option = True
                            break
                        else:
                            flag_option = False

            except ValueError:
                flag_datatype = False

        elif data_type == 'str':
            user_input = user_input.lower()
            if options:
                for i in options:
                    if user_input == i:
                        flag_option = True
                        break
                    else:
                        flag_option = False

        if not flag_datatype:
            print("ValueError: Tipo de dato ingresado no valido.")
        elif not flag_option:
            print(
                "InputError:  El dato ingrasado no se encuentra dentro de las opciones.")
        else:
            break

    return str(user_input)
