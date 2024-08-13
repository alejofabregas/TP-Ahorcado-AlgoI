from leer_archivo_configuracion import leer_archivo_configuracion

from abrir_archivos import abrir_archivos

from generar_diccionarios_palabras import generar_diccionarios_palabras

from agregar_palabras_archivo import agregar_palabras_archivo

from cerrar_archivos import cerrar_archivos

from menu_principal import menu_principal

from finalizar_juego import finalizar_juego


def main():
    
    """El main se encarga de realizar las llamadas a las distintas funciones.
    No realiza ninguna operacion."""
    
    config = leer_archivo_configuracion()
   
    archivos, palabras = abrir_archivos()

    dicc, diccionarios, lista_total_palabras = generar_diccionarios_palabras(archivos, palabras, config)

    agregar_palabras_archivo(palabras, diccionarios, lista_total_palabras)

    cerrar_archivos(archivos, palabras)
       
    seguir = menu_principal(config)
    
    finalizar_juego(seguir, dicc, config)
    
    return


main()