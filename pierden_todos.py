def pierden_todos(dicc_jugadores, config):
    
    """pierden_todos resta el puntaje por derrota a todos los jugadores. Esto
    se da cuando gana el programa, es decir que ninguno adivino la palabra.
    Ademas imprime un mensaje indicando que los jugadores perdieron y que gano
    el programa."""
    
    PUNTAJE = 4
        
    for jugador in dicc_jugadores:
        dicc_jugadores[jugador][PUNTAJE] -= config["PUNTOS_RESTA_GANA_PROGRAMA"][0]
    
    print("\n\nTodos los jugadores perdieron contra la maquina.")
    
    return dicc_jugadores