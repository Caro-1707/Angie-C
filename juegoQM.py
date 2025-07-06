import random
preguntas = {
    1:[ 
        {
            "pregunta": "¿Cuál es la capital de Francia?",
            "opciones": ["a. Madrid", "b. París", "c. Berlín", "d. Roma"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Cuántos días tiene una semana?",
            "opciones": ["a. 5", "b. 6", "c. 7", "d. 8"],
            "respuesta_correcta": "c"
        }
    ],
    2:[
        {
            "pregunta": "¿Cuál es el océano más grande del mundo?",
            "opciones": ["a. Atlántico", "b. Índico", "c. Ártico", "d. Pacífico"],
            "respuesta_correcta": "d"
        },
        {
            "pregunta": "¿Qué gas respiramos principalmente?",
            "opciones": ["a. Oxígeno", "b. Hidrógeno", "c. Nitrógeno", "d. Dióxido de carbono"],
            "respuesta_correcta": "c"
        }
    ],
    3:[
        {
            "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
            "opciones": ["a. Lope de Vega", "b. Gabriel García Márquez", "c. Miguel de Cervantes", "d. Pablo Neruda"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Cuál es el resultado de 3 x 4?",
            "opciones": ["a. 7", "b. 12", "c. 9", "d. 14"],
            "respuesta_correcta": "b"
        }
    ],  
    4:[
        {
            "pregunta": "¿Cuál es el planeta más cercano al Sol?",
            "opciones": ["a. Venus", "b. Tierra", "c. Marte", "d. Mercurio"],
            "respuesta_correcta": "d"
        },
        {
            "pregunta": "¿En qué continente se encuentra Egipto?",
            "opciones": ["a. Asia", "b. África", "c. Europa", "d. América"],
            "respuesta_correcta": "b"
        }
    ],
    5:[ 
         {
      
            "pregunta": "¿Quién pintó la Mona Lisa?",
            "opciones": ["a. Miguel Ángel", "b. Leonardo da Vinci", "c. Picasso", "d. Goya"],
            "respuesta_correcta": "b"
        },
        {
       
            "pregunta": "¿Qué instrumento mide la temperatura?",
            "opciones": ["a. Barómetro", "b. Higrómetro", "c. Termómetro", "d. Altímetro"],
            "respuesta_correcta": "c"
        },
    ],
    6:[ 
        {
       
            "pregunta": "¿Cuál es la raíz cuadrada de 144?",
            "opciones": ["a. 10", "b. 11", "c. 12", "d. 13"],
            "respuesta_correcta": "c"
        },
        {
       
            "pregunta": "¿Qué elemento químico tiene el símbolo 'Na'?",
            "opciones": ["a. Nitrógeno", "b. Sodio", "c. Neón", "d. Níquel"],
            "respuesta_correcta": "b"
        },
     
    ],
    7:[
        {
      
            "pregunta": "¿Qué país tiene forma de bota?",
            "opciones": ["a. España", "b. Italia", "c. Grecia", "d. Francia"],
            "respuesta_correcta": "b"
        },
        {
     
            "pregunta": "¿Quién fue el primer presidente de Estados Unidos?",
            "opciones": ["a. George Washington", "b. Abraham Lincoln", "c. Thomas Jefferson", "d. John Adams"],
            "respuesta_correcta": "a"
        },
    ],
    8:[
        {
      
            "pregunta": "¿Qué órgano produce la insulina?",
            "opciones": ["a. Hígado", "b. Páncreas", "c. Riñón", "d. Estómago"],
            "respuesta_correcta": "b"
        },
        {
       
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["a. 1914", "b. 1939", "c. 1945", "d. 1929"],
            "respuesta_correcta": "b"
        },
     
     ],
    9:[
        {
      
            "pregunta": "¿Qué filósofo escribió 'La República'?",
            "opciones": ["a. Aristóteles", "b. Sócrates", "c. Platón", "d. Descartes"],
            "respuesta_correcta": "c"
        },
        {
       
            "pregunta": "¿Cuál es el idioma más hablado del mundo?",
            "opciones": ["a. Inglés", "b. Español", "c. Hindi", "d. Chino mandarín"],
            "respuesta_correcta": "d"
        },
     
    ],
    10:[ 
        {
     
            "pregunta": "¿Cuál es la fórmula del área de un círculo?",
            "opciones": ["a. πr²", "b. 2πr", "c. πd", "d. r²"],
            "respuesta_correcta": "a"
        },
        {
       
            "pregunta": "¿Quién desarrolló la teoría de la relatividad?",
            "opciones": ["a. Isaac Newton", "b. Albert Einstein", "c. Nikola Tesla", "d. Stephen Hawking"],
            "respuesta_correcta": "b"
        },
     
    ]
}

premio = 0
print("BIENVENIDO A QUIEN QUIERE SER MILLONARIO")
jugador = input("Hola jugador por favor dime tu nombre? ")

print(f"Listo {jugador } vamos a jugar Quien Quiere ser Millonario!")
print("APLAUSOS!!!")

comodines = {"1": "Llamada a un amigo",
             "2": "Cambio de pregunta",
             "3": "50/50",
             "4": "No utilizar comodin\n"}

comodines_usados = {
    "1": False,
    "2": False,
    "3": False
}

for nivel in preguntas:
    pregunta = preguntas[nivel][0]["pregunta"]
    opciones = preguntas[nivel][0]["opciones"]
    respuesta = preguntas[nivel][0]["respuesta_correcta"]

    print(f"{jugador} Nivel{nivel}:")
    print("Pregunta!")
    print(pregunta)
    for op in opciones:
        print(op)


    while True:
        disponibles = [clave for clave in comodines if clave == "4" or not comodines_usados.get(clave, False)]

        if not disponibles or disponibles == ["4"]:
            print("Ya no tienes más comodines disponibles.\n")
            break

        print("\n---Comodines disponibles---")
        for clave in disponibles:
            print(f"{clave}. {comodines[clave]}")

        opcion = input("Selecciona una opcion: ")

        if opcion not in comodines:
            print("Opción inválida.")
            continue

        if opcion != "4" and comodines_usados.get(opcion, False):
            print(" Ese comodín ya fue usado.")
            continue
        match opcion:
            case "1":
                print(f"Has elegido el comodin de llamar un amigo")
                print(f"Creo que la respuesta es:  {random.choice(opciones)}")
                comodines_usados["1"] = True
            case "2":
                print(f"Has elegido el comodin de cambio de pregunta")
                pregunta = preguntas[nivel][1]["pregunta"]
                opciones = preguntas[nivel][1]["opciones"]
                respuesta = preguntas[nivel][1]["respuesta_correcta"]
                print(f"{jugador} Nivel{nivel}:")
                print(pregunta)
                for op in opciones:
                    print(op)
                comodines_usados["2"] = True
            case "3":
                print(f"Has elegido el comodin de 50/50")
                opcion_correcta = [op for op in opciones if op.lower().startswith(respuesta)]
                opciones_incorrectas = [op for op in opciones if not op.lower().startswith(respuesta)]
                opcion_incorrecta = random.choice(opciones_incorrectas)
                opciones_mostradas = [opcion_correcta[0], opcion_incorrecta]
                random.shuffle(opciones_mostradas) # sirve para mezclar aleatoriamente el orden de los elementos de una lista
                print(f"\nOpciones después de aplicar 50/50:")
                for op in opciones_mostradas:
                    print(op)
                comodines_usados["3"] = True
            case "4":
                print("No eligiste ningun comodin")
                break
            case _:
                    print("Opción inválida. No se aplicó ningún comodín.")

    respJugador = input("dime la respuesta correcta: ")
    print(f"\nTu repuesta fue: {respJugador}")
    print(f"\nLa respuesta correcta es: {respuesta}")

    if respuesta == respJugador:
        print(f"dinero obtenido hasta el momento")
        premio = premio+1000
        print(premio)
        print(f"-"*200)
    
        retirar = input(f"\n¿Deseas retirarte del juego? (si/no): ").lower()
        if retirar == "si":
            print(f"\nTU DINERO GANADO FUE ${premio}, GRACIAS POR JUGAR.")
            exit()
    else:
        print("la respuesta es incorrecta salio del juego el dinero obtenido es",premio)
        break