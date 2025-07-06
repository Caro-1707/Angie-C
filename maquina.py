valor = 0
while True:
    bebidas = int(input("Seleccione una bebida: "))

    match bebidas:
        case 1:
            print("Cafe : $3000")
            valor += 3000
        case 2:
            print("Te : $2500")
            valor += 2500
        case 3:
            print("Jugo : $3500")
            valor += 3500
        case 0:
            print(f"El total a pagar es: ${valor}")
            break
        case _:
            print("Opcion no valida, intente de nuevo")
            
print("el total es: ", valor)