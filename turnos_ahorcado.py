from jugador_ganador import jugador_ganador

from pierden_todos import pierden_todos

from interfaz_ahorcado import interfaz_ahorcado

def turnos_ahorcado(dicc_jugadores, lista_de_nombres,config):
    
    """turnos_ahorcado es la encargada de gestionar los turnos de cada jugador
    y de finalizar la partida actual. Llama a la interfaz del ahorcado las veces
    que sea necesaria, si el jugador no desacerto o si la partida no ha finalizado.
    Actualiza los datos de cada jugador al finalizar su turno en el diccionario
    que contiene los datos de todos los jugadores. Al finalizar la partida devuelve
    este diccionario con todos los datos actualizados."""
      
    ADIVINAR = 1
    ACIERTOS = 2
    DESACIERTOS = 3
    LETRAS_I = 6
    GANADOR = 11
    finalizar_turno = False
    finalizar_partida = False
    nro_jugador = 0
    
    while not finalizar_partida:
    
        lista_jugador = dicc_jugadores[lista_de_nombres[nro_jugador]]
        
        while not finalizar_turno:
            print("\n\nJugador:",lista_de_nombres[nro_jugador],"\n")
            print("Palabra a adivinar:", "".join(lista_jugador[ADIVINAR]),"\t", "Aciertos:", lista_jugador[ACIERTOS], "Desaciertos:", lista_jugador[DESACIERTOS], "-", *lista_jugador[LETRAS_I])
            lista_jugador, finalizar_turno, finalizar_partida = interfaz_ahorcado(lista_jugador, finalizar_turno, finalizar_partida, config)
        finalizar_turno = False
        if lista_jugador[GANADOR]:
            lista_jugador = jugador_ganador(lista_jugador, lista_de_nombres[nro_jugador], config)
        dicc_jugadores[lista_de_nombres[nro_jugador]] = lista_jugador
                
        if nro_jugador == len(lista_de_nombres) - 1:
            if lista_jugador[DESACIERTOS] != config["MAX_DESACIERTOS"][0]:
                nro_jugador = 0
            else:   
                dicc_jugadores = pierden_todos(dicc_jugadores,config)
                finalizar_partida = True  
        else:
            nro_jugador += 1
    
    return dicc_jugadores