def limpia_tildes(palabra):
    
    """limpia_tildes es una funcion que por cada palabra que ingresa como parametro
    devuelve la misma palabra reemplazando las vocales con tilde por las mismas
    sin tilde."""
    
    tildes = "ÁÉÍÓÚáéíóú"
    vocales = "AEIOUaeiou"
    dicc_tildes_vocales = palabra.maketrans(tildes, vocales)
    palabra_sin_tildes = palabra.translate(dicc_tildes_vocales)
    
    return palabra_sin_tildes