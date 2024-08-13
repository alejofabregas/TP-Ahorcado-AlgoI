def resultados_generales(dicc_jugadores):
    
    """resultados_generales imprime los datos acumulados de todas las partidas
    que se han jugado hasta el momento, para cada jugador. En estos se incluyen
    el nombre del jugador, su puntaje total, aciertos totales, desaciertos totales,
    y la cantidad de victorias."""
    
    ACIERTOS_TOTALES = 7
    DESACIERTOS_TOTALES = 8
    VICTORIAS = 9 
    PUNTAJE_TOTAL = 10    
    
    lista_jugadores = sorted(dicc_jugadores.items(), key = lambda x : x[1][PUNTAJE_TOTAL], reverse = True)
    
    print("\nResultados Generales:\n")
    for jugador in lista_jugadores:
        print("Jugador:", jugador[0], "\tPuntaje total:", jugador[1][PUNTAJE_TOTAL])
        print("Aciertos:", jugador[1][ACIERTOS_TOTALES], "\tDesaciertos:", jugador[1][DESACIERTOS_TOTALES], "\tVictorias:", jugador[1][VICTORIAS])
    
    return