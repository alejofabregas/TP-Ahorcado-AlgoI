from agregar_palabras_lista import agregar_palabras_lista

from leer_linea import leer_linea

def generar_diccionarios_palabras(archivos, palabras, config):
    
    """generar_diccionarios_palabras se encarga de llenar los diccionarios de
    palabras segun los archivos de texto que contienen estas palabras. Ademas,
    se va llenando la lista total de palabras sin repeticiones y ordenada que
    se utiliza par crear el archivo palabras.csv junto a los diccionarios 1, 2
    y 3."""
    
    dicc = {}
    dicc_1 = {}
    dicc_2 = {}
    dicc_3 = {}
    diccionarios = [dicc_1, dicc_2, dicc_3]

    lista_total_palabras = []

    for indice in range(len(archivos)):
        dicc, diccionarios[indice] = leer_linea(archivos[indice], dicc, diccionarios[indice], palabras, config)
        lista_total_palabras = agregar_palabras_lista(lista_total_palabras, diccionarios[indice])
    lista_total_palabras = list(set(lista_total_palabras))
    lista_total_palabras.sort()
    
    return dicc, diccionarios, lista_total_palabras