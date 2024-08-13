import random

def elige_palabras_random(dicc, longitud, cant_participantes):

    """elige_palabra va a devolver una palabra lista de palabras aleatorias del
    diccionario de palabras que fue pasado como parametro. El largo de esta
    lista es la cantidad de palabras, y depende de la cantidad de participantes.
    Si tiene como parametro una longitud buscara en el diccionario una palabra
    de dicha longitud. Si no, elige una al azar dentro del diccionario."""  
    
    lista_palabras_random = []

    if longitud != 0:   
        if longitud in dicc and len(dicc[longitud]) >= cant_participantes:
            lista_dicc = dicc[longitud]
            for participante in range(cant_participantes):
                palabra_random = random.choice(lista_dicc)
                lista_palabras_random.append(palabra_random)
                lista_dicc.remove(palabra_random)
        else:
            lista_palabras_random = []
    else:
        dicc_keys = random.choice(list(dicc))
        lista_dicc = dicc[dicc_keys]
        for participante in range(cant_participantes):
            palabra_random = random.choice(lista_dicc)
            lista_palabras_random.append(palabra_random)
            lista_dicc.remove(palabra_random)
        
    return lista_palabras_random