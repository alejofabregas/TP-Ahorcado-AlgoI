def lista_de_palabras_por_linea(linea):
    
    """lista_de_palabras_por_linea toma una linea pasada como parametro y la
    procesa para devolver una lista con las palabras que hay en esa linea."""
    
    lista_de_palabras = []
    palabra = ""
    for caracter in linea:
        if caracter == ",":
            palabra = palabra.replace("\n", "")
            lista_de_palabras.append(palabra)
            palabra = ""
        else:
            palabra += caracter
    palabra = palabra.replace("\n", "")
    lista_de_palabras.append(palabra)
    
    return lista_de_palabras