from obtener_nombres_de_jugadores import obtener_nombres_de_jugadores

from genera_dicc_jugadores import genera_dicc_jugadores

from imprimir_asignacion_de_turnos import imprimir_asignacion_de_turnos

from seleccion_longitud_palabras import seleccion_longitud_palabras

from palabras_en_dicc import palabras_en_dicc

from turnos_ahorcado import turnos_ahorcado

from resultados_partida import resultados_partida

from guardar_datos import guardar_datos

from resultados_generales import resultados_generales

def finalizar_juego(seguir,dicc,config):
    
    """finalizar_juego es la encargada de empezar cada partida y le pregunta al
    usuario al finalizar si quiere iniciar otra partida. En caso negativo, se
    imprime un mensaje informando que se esta saliendo del juego. Con la ayuda
    de otras funciones obtiene los datos de los jugadores y los va actualizando
    con cada partida jugada."""
    
    if seguir:
        lista_de_nombres = obtener_nombres_de_jugadores(config)
        dicc_jugadores = genera_dicc_jugadores(lista_de_nombres)    
    
    cant_partidas = 0
    
    ganador = ""  

    
    while seguir:
        
        lista_de_nombres = imprimir_asignacion_de_turnos(lista_de_nombres, ganador)
        
        lista_palabras = seleccion_longitud_palabras(dicc, len(lista_de_nombres))
        
        dicc_jugadores = palabras_en_dicc(dicc_jugadores, lista_palabras) 
        
        dicc_jugadores = turnos_ahorcado(dicc_jugadores, lista_de_nombres,config)
        
        resultados_partida(dicc_jugadores)
        
        dicc_jugadores = guardar_datos(dicc_jugadores)
        
        if cant_partidas != 0: 
            resultados_generales(dicc_jugadores)
        
        cant_partidas += 1 
        
        if input("\n¿Desea seguir jugando? (s/n): ") == "n":
            seguir = False
            print("\n\nSaliendo del juego...")
            
    return