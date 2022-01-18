
def buscaminas_menu():
    print("""
    $$$$$$$\                                                       $$\                                            @@.    
    $$  __$$\                                                      \__|                                   (@).%@@@@@@@@%.(@)
    $$ |  $$ |$$\   $$\  $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$\$$$$\  $$\ $$$$$$$\   $$$$$$\   $$$$$$$\       .#@@@@@@@@@@@@(.
    $$$$$$$\ |$$ |  $$ |$$  _____|$$  _____|\____$$\ $$  _$$  _$$\ $$ |$$  __$$\  \____$$\ $$  _____|     (@@@,   @@@@@@@@@(
    $$  __$$\ $$ |  $$ |\$$$$$$\  $$ /      $$$$$$$ |$$ / $$ / $$ |$$ |$$ |  $$ | $$$$$$$ |\$$$$$$\    @@@@@@@@@@@@@@@@@@@@@@@@
    $$ |  $$ |$$ |  $$ | \____$$\ $$ |     $$  __$$ |$$ | $$ | $$ |$$ |$$ |  $$ |$$  __$$ | \____$$\      (@@@@@@@@@@@@@@@@/.
    $$$$$$$  |\$$$$$$  |$$$$$$$  |\$$$$$$$_\$$$$$$$ |$$ | $$ | $$ |$$ |$$ |  $$ |\$$$$$$$ |$$$$$$$  |     /%&@@@@@@@@@@@@&%/
    \_______/  \______/ \_______/  \_______|\_______|\__| \__| \__|\__|\__|  \__| \_______|\_______/      (@/ %@@@@@@@@% (@)
                                                V. 1.2                                                            @@
    """)


def menu_dificultades():
    print("""
                                              <<< Selecciona una dificulad: >>>

                    |         [1] Fácil         |         [2] Normal         |         [3] Difícil         |
                    |                           |                            |                             |
                    |          · 5x5            |          · 10x10           |           · 15x15           |
                    |        · 6 minas          |        · 24 minas          |         · 54 minas          |


                                    --->  Escribe 'h' si necesitas ayuda/instucciones  <---
    """)


def help_menu():
    print("""
    
                
                                   _             __  _____           _                       _                       
              /\                  | |           / / |_   _|         | |                     (_)                      
             /  \  _   _ _   _  __| | __ _     / /    | |  _ __  ___| |_ _ __ _   _  ___ ___ _  ___  _ __   ___  ___ 
            / /\ \| | | | | | |/ _` |/ _` |   / /     | | | '_ \/ __| __| '__| | | |/ __/ __| |/ _ \| '_ \ / _ \/ __|
           / ____ \ |_| | |_| | (_| | (_| |  / /     _| |_| | | \__ \ |_| |  | |_| | (_| (__| | (_) | | | |  __/\__  |
          /_/    \_\__, |\__,_|\__,_|\__,_| /_/     |_____|_| |_|___/\__|_|   \__,_|\___\___|_|\___/|_| |_|\___||___/
                    __/ |                                                                                            
                    |___/                                                                                             

                                                        <<< Como Jugar >>>

                        1   2   3 ->x
                       -------------      Este es el tablero de juego, está enumerado en el eje horizontal 
                    1 | □ | □ | □ |       y en eje vertica por numeros que determinan las coordenadas de
                       -------------      cada uno de los cuadros.
                    2 | □ | □ | □ |
                       -------------      Al entrar al juego puedes escribir una coordenada de manera x, y 
               y <- 3 | □ | □ | □ |       para realizar una accion en el cuadro correspondiente, ya sea 
                       -------------      "cavar" o "colocar una bandera" que se representa con la letra 'f'.


                        1   2   3 
                       -------------      
                    1 | f | 2 | 1 |       
                       -------------      Para ganar hay que despejar todo el tablero colocando las banderas
                    2 | 2 | f | 1 |       correspondientes a cada bomba
                       -------------      
                    3 | 1 | 1 | 1 |       
                       -------------      

                                                       <<< Creditos >>>

                
                              <Autor 2>               Ana Isabella Gasca                     <Autor 3>
                            Datos Extra...      Estudiante Ingenieria Electronica          Datos Extra...
                            Datos extra...        https://github.com/ZBNomek               Datos Extra...
            


    """)


def game_over():
    print("""
      _____                         ____                 
     / ____|                       / __ \                
    | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
    | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
    | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
     \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                        
    """)


def good_bye():
    print("gracias por juagar!!!")
