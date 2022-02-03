from recursos_juego import *

admin_key = False
buscaminas_menu()

while True:
    main(admin_key)
    menu_volver_inicio()
    breaker = verificador("str", ("y", "n"), '\t'*7 + "     >")
    if breaker == "n":
        break
despedida()
