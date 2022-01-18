"""
Esta parte son funciones que sirven para filtrar informacion de los 
inputs para que desta manera no hayan errores y muestren el el terminar
al usuario el error de su input, repitiendo esto hata que el usuario
ingrese un input valido y sirve con datos tipo str y  int, pero pueden
ser ampliados a más.
"""


# verifica que el input sea una de las opciones (filtro de dos opciones ej: a o b | si o no) ---> options = opciones posibles | datatype = el tipo de dato de las opciones y del input que se busca


from tkinter import TRUE


def tuple_mode_checker():
    while True:
        flag = True
        input_user = str(input(">>>"))
        print()
        input_user.lower()
        if input_user == "m":
            pass
        else:
            input_user = input_user.split(",")
            if len(input_user) == 2:
                for i in input_user:
                    try:
                        i = int(i)
                    except:
                        ValueError
                        flag = False
                        break
            else:
                flag = False
            if flag == True:
                input_user = input_user[0], input_user[-1]

        if flag == True:
            break

    return input_user


def checker_options(options: tuple, data_type: str, pre_text: str = ">>> "):
    while True:
        validation_datatype: bool
        validation_option: bool

        input_user = input(pre_text)
        print()

        if data_type == "int":
            try:
                input_user = int(input_user)
                validation_datatype = True
                for i in options:
                    if input_user == i:
                        validation_option = True
                        break
                    else:
                        validation_option = False
            except:
                ValueError
                validation_datatype = False
        elif data_type == "str":
            input_user = input_user.lower()
            validation_datatype = True
            for i in options:
                if input_user == i:
                    validation_option = True
                    break
                else:
                    validation_option = False
        if validation_datatype == False:
            print("Not a valid datatype for input.")
        elif validation_option == False:
            print("Not a valid option.")
            print()
        else:
            break

    return input_user


# verifica que el input sea el tipo de dato bucado ---> data_type = tipo de dato que se necesita | taxt = dato a analizar (sirve para ins, str y se puede adaptar a máss)
def checker(data_type: str, text: str):
    breaker: bool
    while True:
        breaker = False
        input_user = input(text)

        if data_type == "int":
            try:
                input_user = int(input_user)
                breaker = True
                break
            except:
                ValueError
                print("Not a valid input (not int)")
        elif data_type == "str":
            input_user.lower()
            breaker = True
            break

        if breaker == True:
            break
    return input_user


def various_checker(options: tuple, text: str = ">"):
    breaker: bool
    while True:
        breaker = False
        input_user = (str(input(text))).lower()
        if "int" in options:
            try:
                input_user = int(input_user)
                breaker = True
            except:
                ValueError
        elif "float" in options:
            try:
                input_user = float(input_user)
                breaker = True
            except:
                ValueError
        elif "str" in options:
            try:
                input_user = str(input_user)
                breaker = True
            except:
                ValueError
        if breaker == True:
            break
        else:
            for i in options:
                if input_user == i:
                    breaker = True
        if breaker == True:
            break
        else:
            print("!!! Not valid input !!!")
    return input_user
