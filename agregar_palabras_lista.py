def agregar_palabras_lista(lista_palabras, diccionario):
    
    """agregar_palabras_lista suma las palabras de cada diccionario a una lista
    que se va a utilizar para generar el archivo con todas las palabras y sus
    apariciones en los distintos textos."""
    
    lista_palabras.extend(list(diccionario.keys()))
    
    return lista_palabras