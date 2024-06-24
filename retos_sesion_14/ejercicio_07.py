# Simular un tres en raya con funciones donde reciba las jugadas 
# y devuelva el ganador hasta que alguien ingrese salir

def jugar_tres_en_raya(turno1, turno2):
    pass

print("Tres en raya")
while True:
    jugador1 = input("Posición Jugador 1: ")
    if jugador1 == "salir":
        break
    jugador2 = input("Posición Jugador 2: ")
    if jugador2 == "salir":
        break
    resultado = jugar_tres_en_raya(jugador1, jugador2)
    print (resultado)
