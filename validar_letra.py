def validar_letra(letra, letras_correctas, letras_erroneas):
    
    """validar_letra recibe la letra ingresada por el usuario y la valida.
    Si no es una letra imprime 'Ingreso invalido', y si ya se ingreso
    anteriormente imprime 'Letra ya ingresada'. Si es correcta devolvera un
    booleano True"""
    
    letra_es_correcta = False

    if len(letra) != 1 or letra.isalpha() == False:
        print("\nIngreso invalido")  
    elif letra.lower() in letras_correctas or letra.lower() in letras_erroneas:
        print("\nLetra ya ingresada")
    else:
        letra_es_correcta = True
        
    return letra_es_correcta