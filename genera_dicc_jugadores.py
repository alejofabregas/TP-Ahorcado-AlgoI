def genera_dicc_jugadores(lista_de_nombres):
    
    """genera_dicc_jugadores crea el diccionario que tiene como claves a los
    nombres de los jugadores y como valores a las listas vacías que van a contener
    a sus datos."""
    
    dicc_jugadores = {}
    for jugador in lista_de_nombres:
        dicc_jugadores[jugador] = ["",[],0,0,0,[],[],0,0,0,0,False]
        
    return dicc_jugadores