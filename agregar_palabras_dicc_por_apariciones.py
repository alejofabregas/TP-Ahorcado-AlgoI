def agregar_palabras_dicc_por_apariciones(linea, diccionarios):
    
    """agregar_palabras_dicc_por_apariciones toma las líneas procesadas de cada
    archivo y va sumando las palabras al diccionario. Este diccionario tiene
    como clave a cada palabra y como valor a la cantidad de apariciones de dicha
    palabra en el texto."""
    
    for palabra in linea:
        if palabra in diccionarios:
            diccionarios[palabra] += 1
        else:
            diccionarios[palabra] = 1
            
    return diccionarios