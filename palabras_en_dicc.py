def palabras_en_dicc(dicc_jugadores, lista_de_palabras):
    
    """palabras_en_dicc: dentro del diccionario de los jugadores, coloca la
    palabra a adivinar y la palabra incognita con los signos de interrogacion,
    para la lista de datos de cada jugador."""
    
    contador = 0
    PALABRA_A_ADIVINAR = 0
    PALABRA_INCOGNITA = 1
    
    for jugador in dicc_jugadores:
        dicc_jugadores[jugador][PALABRA_A_ADIVINAR] = lista_de_palabras[contador]
        dicc_jugadores[jugador][PALABRA_INCOGNITA] = ["?"] * len(lista_de_palabras[contador])
        contador += 1
        
    return dicc_jugadores