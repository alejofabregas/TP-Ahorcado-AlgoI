def agregar_palabras_archivo(palabras, diccionarios, lista_de_palabras):
    
    """agregar_palabras_archivo toma la lista de palabras y los diccionarios que
    tienen la cantidad de apariciones de cada palabra y escribe en el archivo csv
    llamado palabras a todas las palabras de los tres textos ordenadas
    alfabeticamente y el número de apariciones de dichas palabras en los tres
    archivos."""
        
    for palabra in lista_de_palabras:
        linea = palabra + ","
        for indice in range(len(diccionarios)):
            if diccionarios[indice].__contains__(palabra):
                cantidad = str(diccionarios[indice][palabra])
                linea += cantidad + ","
            else:
                cantidad = 0
                linea += str(cantidad) + ","
        linea = linea[:-1]
        palabras.write(linea +"\n")
    
    return