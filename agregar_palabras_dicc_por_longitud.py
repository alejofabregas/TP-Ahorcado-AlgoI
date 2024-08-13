def agregar_palabras_dicc_por_longitud(linea, dicc):
    
    """agregar_palabras_dicc_por_longitud toma las líneas procesadas de cada
    archivo y va sumando las palabras al diccionario. Este diccionario tiene
    como clave al largo de las palabras y como valor a una lista que contiene
    a todas las palabras de dicho valor."""
    
    for palabra in linea:
        if len(palabra) in dicc:
            if palabra not in dicc[len(palabra)]:
                dicc[len(palabra)] += [palabra]
        else:
            dicc[len(palabra)] = [palabra]
            
    return dicc