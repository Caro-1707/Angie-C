vocales = input("Ingresa una palabra: ")

vocal = ['a', 'e', 'i', 'o', 'u']
contador = 0

for letra in vocales:
    if letra.lower() in vocal:
        contador += 1

print("El número de vocales es:", contador)