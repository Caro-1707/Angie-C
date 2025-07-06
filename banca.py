ganadas = 0
perdidas = 0
empate = 0

import random

while True:
    banca = random.randint(1, 13)
    cartaJugador = random.randint(1,13)
    jugador = input(f"La carta es {cartaJugador}, desea jugarla?")
    print("el numero que eligio banca es:", banca)

    if jugador.lower() == "si":
        if banca > cartaJugador:
            print("perdido")
            perdidas += 1
        elif cartaJugador > banca:
            print("gano")
            ganadas += 1
        else:
            print("empate")
            empate += 1

    elif jugador == "no":
        print("gracias por jugar")
        print("cuantas gano", ganadas)
        print("cuantas perdio", perdidas)
        print("cuantas empate", empate)
        break 

    else:
        print("Digite una opcion valida")
        continue   

    if ganadas == 3:
        print("haz ganado")
        break
    elif perdidas == 3:
        print("haz perdido")
        break

    print("las rondas ganadas son:", ganadas)
    print("las rondas perdidas son:", perdidas)
    print("las rondas empatadas son:", empate)


    


