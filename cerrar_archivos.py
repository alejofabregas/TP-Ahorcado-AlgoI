def cerrar_archivos(archivos, palabras):
    
    """cerrar_archivos simplemente cierra los archivos que fueron abiertos
    previamente"""
    
    archivos[0].close()
    archivos[1].close()
    archivos[2].close()
    palabras.close()
    
    return