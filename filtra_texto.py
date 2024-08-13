from limpia_tildes import limpia_tildes

def filtra_texto(texto, config):
    
    """filtra_texto es una funcion que recibe un texto (tipo string) y devuelve una
    lista ordenada alfabeticamente con las palabras que contiene el mismo."""
    
    for car in texto:
        if not car.isalpha() and car != ' ':
            texto = texto.replace(car,(' '))
    lista_aux_palabras = texto.split()
    lista_palabras = []
    for palabra in lista_aux_palabras:
        if len(palabra) >= config["LONG_PALABRA_MIN"][0]:
            lista_palabras.append(limpia_tildes(palabra).lower())
    
    return sorted(lista_palabras)