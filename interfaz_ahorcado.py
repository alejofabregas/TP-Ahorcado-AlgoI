from validar_letra import validar_letra

from actualizar_incognita import actualizar_incognita

def interfaz_ahorcado(lista_jugador, finalizar_turno, finalizar_partida, config):
    
    """interfaz_ahorcado recibe todos los datos del jugador en una lista. Se
    encarga de la interacción con el usuario dentro de su turno en el ahorcado.
    Devuelve los datos actualizados del jugador de acuerdo al turno jugado.
    Ademas, modifica el booleano finalizar_turno si el jugador tuvo un desacierto
    o si adivino la palabra, en este caso tambien se modifica finalizar_partida."""
    
    PALABRA = 0
    ADIVINAR = 1
    ACIERTOS = 2
    DESACIERTOS = 3
    PUNTAJE = 4
    LETRAS_C = 5
    LETRAS_I = 6
    GANADOR = 11
    
    letra = input("Ingrese Letra: ")
    if letra == "FIN" or letra == "0":
        finalizar_turno = True
        finalizar_partida = True
    elif validar_letra(letra, lista_jugador[LETRAS_C], lista_jugador[LETRAS_I]):
        letra = letra.lower()
        lista_jugador[ADIVINAR] = actualizar_incognita(lista_jugador[ADIVINAR], lista_jugador[PALABRA], letra)
        if lista_jugador[PALABRA].find(letra) >= 0:
            lista_jugador[PUNTAJE] += config["PUNTOS_ACIERTOS"][0]
            lista_jugador[ACIERTOS] += 1
            lista_jugador[LETRAS_C].append(letra)
            if "".join(lista_jugador[ADIVINAR]) != lista_jugador[PALABRA]:
                print("\nMuy bien!!! --->", "".join(lista_jugador[ADIVINAR]), "\t", "Aciertos:", lista_jugador[ACIERTOS], "Desaciertos:", lista_jugador[DESACIERTOS], "-", *lista_jugador[LETRAS_I])
            else:
                lista_jugador[GANADOR] = True
                finalizar_turno = True
                finalizar_partida = True
        else:
            lista_jugador[PUNTAJE] -= config["PUNTOS_DESACIERTOS"][0]
            lista_jugador[DESACIERTOS] += 1
            finalizar_turno = True
            lista_jugador[LETRAS_I].append(letra)
            print("\nLo siento!!! --->", "".join(lista_jugador[ADIVINAR]), "\t", "Aciertos:", lista_jugador[ACIERTOS], "Desaciertos:", lista_jugador[DESACIERTOS],"-",*lista_jugador[LETRAS_I])
            
    return lista_jugador, finalizar_turno, finalizar_partida