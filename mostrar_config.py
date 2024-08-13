def mostrar_config(config):
    
    """mostrar_config imprime los parametros con los que está configurado el
    juego, diferenciando aquellos que han sido modificados de aquellos que
    estan por defecto."""
    
    print()
    for parametro in config:
        if config[parametro][1] == 0:
            print(parametro,": ",config[parametro][0]," (por defecto).",sep="")
        else:
            print(parametro,": ",config[parametro][0],sep="")
    print()
    
    return