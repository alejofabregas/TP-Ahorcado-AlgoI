from random import shuffle

def imprimir_asignacion_de_turnos(lista_de_nombres,ganador):
     
    """imprimir_asignacion_de_turnos ordena aleatoriamente la lista de jugadores
    para asignar el orden de los turnos al azar. El ganador de la partida anterior
    siempre va primero. Finalmente imprime el orden de los turnos."""
    
    if ganador != "":
        lista_de_nombres.remove(ganador)
        shuffle(lista_de_nombres)
        lista_de_nombres.insert(0, ganador)
    else:
        shuffle(lista_de_nombres)
    for i in range(len(lista_de_nombres)):
        nro_turno = i + 1
        nombre_jugador = lista_de_nombres[i]
        print("El", nro_turno, "° turno es de ", nombre_jugador)
        
    return lista_de_nombres