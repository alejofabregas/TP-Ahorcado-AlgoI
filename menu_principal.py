from mostrar_config import mostrar_config

def menu_principal(config):
    
    """menu_principal es una funcion que interactua con el usuario y le da la 
    bienvenida al juego. Tiene 4 opciones: Inciar juego, Leer instrucciones,
    Configuracion y Salir del juego."""
    
    opcion = "0"
    
    seguir = True
    
    print("---- Bienvenido al ahorcado ----")
        
    while opcion != "1" and opcion != "4":
    
        opcion = input("1- Iniciar el juego.\n2- Instrucciones.\n3- Configuracion.\n4- Salir del juego.\n>>> ")
        if opcion == "2":
            print('''\n\tEl juego consiste en adivinar una palabra al azar. 
\tSi quiere podra elegir la longitud de la palabra.
\tTendra hasta 8 desaciertos para adivinar la palabra antes de perder.
\tPara salir de la partida actual debera ingresar "FIN" o "0".
\tPor cada letra acertada se le suma 10 puntos al jugador.
\tPor cada desacierto se le resta 5 puntos al jugador.
\tAl final de la partida se informara el puntaje parcial.
\tAl salir del juego se informara el puntaje final.
                  ''')
        elif opcion == "3":
            mostrar_config(config)
        elif opcion == "4":
            seguir = False
             
        elif opcion != "1":
            print("Ingreso invalido.")
            
    return seguir