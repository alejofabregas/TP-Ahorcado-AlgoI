def actualizar_incognita(adivinar, palabra, letra):
    
    """actualizar_incognita modifica la palabra incognita (con los signos de  
    interrogacion) reemplazando los caracteres acertados por el usuario."""
    
    for i in range(0, len(adivinar)):
        if palabra[i] == letra:
            adivinar[i] = letra
    
    return adivinar