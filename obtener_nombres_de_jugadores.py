def obtener_nombres_de_jugadores(config):
    
    """obtener_nombres_de_jugadores solicita que se ingrese los nombres de los
    jugadores, y los guarda en una lista. Se indica que para finalizar la carga
    hay que presionar ENTER."""
    
    nombres_de_jugadores = []
    cantidad_de_ingresos = 0
    termino_ingreso = False
    while cantidad_de_ingresos < config["MAX_USUARIOS"][0] and not termino_ingreso:
        nombre_ingresado = input("Ingrese el nombre de un jugador o presione ENTER para finalizar el ingreso: ")
        if nombre_ingresado == "":
            termino_ingreso = True
        else:
            nombres_de_jugadores.append(nombre_ingresado)
        cantidad_de_ingresos = len(nombres_de_jugadores)
        
    return nombres_de_jugadores