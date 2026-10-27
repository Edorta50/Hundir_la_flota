import funciones as f

# 1. Creamos todos los tableros del juego
t_barcos_rival = f.crear_tableros()
t_disparos_rival = f.crear_tableros()
t_barcos_jugador = f.crear_tableros()
t_disparos_jugador = f.crear_tableros()

# 2. Colocamos toda la flota de forma AUTOMÁTICA y ALEATORIA en el tablero del jugador:
# - 1 barco de eslora 4
f.colocar_barco_aleatorio(t_barcos_jugador, 4)

# - 2 barcos de eslora 3
f.colocar_barco_aleatorio(t_barcos_jugador, 3)
f.colocar_barco_aleatorio(t_barcos_jugador, 3)

# - 3 barcos de eslora 2
f.colocar_barco_aleatorio(t_barcos_jugador, 2)
f.colocar_barco_aleatorio(t_barcos_jugador, 2)
f.colocar_barco_aleatorio(t_barcos_jugador, 2)

# 3. Imprimimos la información en la consola de forma limpia
print("******************** TABLERO DE BARCOS (ALEATORIO) ********************")
print(t_barcos_jugador)

print("\n******************** TABLERO DE DISPAROS ********************")
print(t_disparos_jugador)