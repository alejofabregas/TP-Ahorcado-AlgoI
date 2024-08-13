def guardar_datos(dicc_jugadores):
    
    """guardar_datos almacena los datos de la partida recién jugada en los datos
    totales, para cada jugador. Estos luego se informan en los resultados generales."""
    
    ACIERTOS = 2
    DESACIERTOS = 3
    PUNTAJE = 4
    LETRAS_CORRECTAS = 5
    LETRAS_ERRONEAS = 6
    ACIERTOS_TOTALES = 7
    DESACIERTOS_TOTALES = 8
    PUNTAJE_TOTAL = 10
    GANADOR = 11
    
    for jugador in dicc_jugadores:
        
        dicc_jugadores[jugador][PUNTAJE_TOTAL] += dicc_jugadores[jugador][PUNTAJE]
        dicc_jugadores[jugador][ACIERTOS_TOTALES] += dicc_jugadores[jugador][ACIERTOS]
        dicc_jugadores[jugador][DESACIERTOS_TOTALES] += dicc_jugadores[jugador][DESACIERTOS]
        dicc_jugadores[jugador][LETRAS_CORRECTAS] = []
        dicc_jugadores[jugador][LETRAS_ERRONEAS] = []
        dicc_jugadores[jugador][ACIERTOS] = 0
        dicc_jugadores[jugador][DESACIERTOS] = 0
        dicc_jugadores[jugador][PUNTAJE] = 0
        dicc_jugadores[jugador][GANADOR] = False
        
    return dicc_jugadores