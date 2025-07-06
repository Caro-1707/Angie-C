notas = ["matematicas", "fisica", "quimica", "historia", "lengua"]

reprobadas = []
aprobadas = []

for nota in notas:
    materia = int(input(f"Ingrese la nota de {nota}: "))
    if materia >= 6:
        aprobadas.append(nota)
    else:
        reprobadas.append(nota)

print("Materias aprobadas: ", aprobadas)
print("Materias reprobadas: ", reprobadas)