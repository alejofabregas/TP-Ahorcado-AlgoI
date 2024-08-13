from lista_de_palabras_por_linea import lista_de_palabras_por_linea

def leer_archivo_configuracion():
    
    """leer_archivo_configuracion abre el archivo csv de configuracion, lee linea
    por linea y modifica los datos del archivo en el diccionario de datos por
    defecto, indicando con un 0 si es el valor por defecto (no se modifico) y con
    un 1 si el valor fue modificado por el archivo."""
    
    archivo = open("configuracion.csv", "r")
    datos = {"MAX_USUARIOS":[5,0], "LONG_PALABRA_MIN":[5,0], "MAX_DESACIERTOS":[8,0],"PUNTOS_ACIERTOS":[2,0], 
             "PUNTOS_DESACIERTOS":[1,0], "PUNTOS_ADIVINA_PALABRA":[10,0], "PUNTOS_RESTA_GANA_PROGRAMA":[5,0]}
    linea = " "
    while linea:
        linea = archivo.readline()
        lista_de_palabras = lista_de_palabras_por_linea(linea)
        if len(lista_de_palabras) == 2:
            clave = lista_de_palabras[0]
            valor = lista_de_palabras[1]
            datos[clave][0] = int(valor)
            datos[clave][1] = 1
    archivo.close()
    
    return datos