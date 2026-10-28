import numpy as np

def crear_tableros():

# Crea y devuelve un tablero vacío de 10x10 relleno de espacios en blanco.
    tablero = np.full((10, 10), " ")
    return tablero

# Tablero: La matriz o cuadrícula en la que se va a trabajar. posiciones:  
# Las coordenadas (en forma de filas y columnas) que va a ocupar el barco.
def colocar_barco(tablero, posiciones): 

###################################################################################################

# Recibe un tablero y una lista de coordenadas (fila, columna) y coloca una marca ("O") en cada una de esas casillas.
    for fila, col in posiciones:
        tablero[fila, col] = "O"  
    return tablero

def colocar_barco_aleatorio(tablero, eslora):
    """
    # Coloca un barco de forma aleatoria (horizontal o vertical) controlando que quepa dentro del tablero de 10x10.
    """
    colocado = False
    while not colocado:
        # Elegimos al azar si el barco se coloca en horizontal (0) o vertical (1)
        orientacion = np.random.randint(0, 2)
        
        if orientacion == 0:  # Horizontal
            fila = np.random.randint(0, 10)
            columna = np.random.randint(0, 11 - eslora)
            
            # Creamos la lista de coordenadas consecutivas
            posiciones = [(fila, columna + i) for i in range(eslora)]
        else:  # Vertical
            fila = np.random.randint(0, 11 - eslora)
            columna = np.random.randint(0, 10)
            
            # Creamos la lista de coordenadas consecutivas
            posiciones = [(fila + i, columna) for i in range(eslora)]
        
        # Verificamos si las casillas están libres (aquí comprobamos que tengan un espacio " ")
        espacios_libres = True
        for f, c in posiciones:
            if tablero[f, c] != " ":
                espacios_libres = False
                break
        
        # Si están libres, colocamos el barco y salimos del bucle
        if espacios_libres:
            colocar_barco(tablero, posiciones)
            colocado = True
            
    return tablero