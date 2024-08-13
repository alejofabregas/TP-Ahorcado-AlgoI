def abrir_archivos():
    
    """abrir_archivos abre los tres archivos de texto con las palabras a
    utilizar, los coloca en una lista de archivos, y ademas abre en modo write
    al archivo palabras que se llenará posteriormente."""
    
    
    archivo_1 = open('Cuentos.txt', 'r')
    archivo_2 = open('La araña negra - tomo 1.txt', 'r')
    archivo_3 = open('Las 1000 Noches y 1 Noche.txt', 'r')
    archivos = [archivo_1, archivo_2, archivo_3]
    palabras = open('palabras.csv', 'w')
    
    return archivos, palabras