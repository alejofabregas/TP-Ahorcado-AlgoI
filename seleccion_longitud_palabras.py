from elige_palabras_random import elige_palabras_random

def seleccion_longitud_palabras(dicc, cant_participantes):
    
    """seleccion_longitud_palabra le da la opcion al usuario de elegir la longitud
    de la palabra a adivinar. Luego llama a elige_palabra para elegir una palabra
    aleatoria del largo deseado. Si no se especifica la longitud, se elige una al
    azar."""
    
    lista_palabras_random = []
    suficientes_palabras = False
    
    while not suficientes_palabras:
        if input("\n¿Desea ingresar la longitud de la palabra? (s/n): ") == "s":
            longitud = input("\nIngrese la longitud de la palabra mayor a 5 caracteres: ")    
            while not longitud.isnumeric():
                print("\nIngreso invalido, debe ser un valor numerico. ")
                longitud = input("\nIngrese la longitud de la palabra mayor a 5 caracteres: ")
        else:
            longitud = 0
        
        lista_palabras_random = elige_palabras_random(dicc, int(longitud), cant_participantes)
        
        if lista_palabras_random == []:
            print("\nNo hay suficientes palabras de esa longitud.")
        else:
            suficientes_palabras = True

    return lista_palabras_random