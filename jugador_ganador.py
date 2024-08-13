def jugador_ganador(lista_jugador, nombre_ganador,config):
    
    """jugador_ganador suma el puntaje y la victoria en los datos del jugador
    que gano la partida. Ademas imprime un mensaje indicando que este jugador
    fue el ganador."""
    
    PUNTAJE = 4
    VICTORIAS = 9
     
    lista_jugador[PUNTAJE] += config["PUNTOS_ADIVINA_PALABRA"][0]
    lista_jugador[VICTORIAS] += 1
    print("\n\nEl jugador", nombre_ganador, "ha ganado la partida!!")
    
    return lista_jugador