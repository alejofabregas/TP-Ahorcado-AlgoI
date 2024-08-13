def resultados_partida(dicc_jugadores):
    
    """resultados_partida imprime los datos de la partida recien terminada para
    cada jugador, indicando su nombre, la palabra a adivinar, aciertos,
    desaciertos y puntaje."""
    
    PALABRA = 0
    ACIERTOS = 2
    DESACIERTOS = 3
    PUNTAJE = 4
       
    print("\nResultados de la partida:\n")
    for jugador in dicc_jugadores:
        print("Jugador:", jugador, "\tPalabra:", dicc_jugadores[jugador][PALABRA])
        print("Aciertos:", dicc_jugadores[jugador][ACIERTOS], "\tDesaciertos:", dicc_jugadores[jugador][DESACIERTOS], "Puntaje:",dicc_jugadores[jugador][PUNTAJE])
        
    return