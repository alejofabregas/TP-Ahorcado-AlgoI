from agregar_palabras_dicc_por_longitud import agregar_palabras_dicc_por_longitud

from agregar_palabras_dicc_por_apariciones import agregar_palabras_dicc_por_apariciones

from filtra_texto import filtra_texto

def leer_linea(archivo, dicc, diccionarios, palabras, config):
    
    """leer_linea hace la lectura línea por línea del archivo pasado como
    parámetro hasta el end of file. Cada línea se filtra y se envía a los
    correspondientes diccionarios."""
    
    linea = archivo.readline()
    while linea != '':
        dicc = agregar_palabras_dicc_por_longitud(filtra_texto(linea, config), dicc)
        diccionarios = agregar_palabras_dicc_por_apariciones(filtra_texto(linea, config), diccionarios)
        linea = archivo.readline()
        
    return dicc, diccionarios