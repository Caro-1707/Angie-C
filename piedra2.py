import random

opciones = ["piedra", "papel", "tijera"]
jugador = 0 
computadora = 0
rondas = int(input("cuantas rondas quiere jugar?: "))

for ronda in range(1, rondas+1):
    print(f"\n Ronda {ronda} de {rondas}")
    eleccionJ = input(" Elija piedra, papel o tijera: ").lower()
    while eleccionJ not in opciones:
        eleccionJ= input("Opción inválida. Elija piedra, papel o tijera: ").lower()
    
    eleccionC = random.choice(opciones)
    print(f"jugador: {eleccionJ.capitalize()}")
    print(f" computadora: {eleccionC.capitalize()}")

    if eleccionJ == eleccionC:
        print("Empate ")
        
    elif (eleccionJ == "piedra" and eleccionC == "tijera") or \
         (eleccionJ == "papel" and eleccionC == "piedra") or \
         (eleccionJ == "tijera" and eleccionC == "papel"):
        print("Ganaste ")
        jugador += 1
    else:
        print("Perdiste ")
        computadora += 1
    
    print(f"Puntaje: {jugador} - {computadora}")
    print(f"Rondas restantes: {rondas - ronda}")

print("Juego terminado ")
print(f"Puntaje final: \njugador:{jugador} \ncomputadora: {computadora}")

