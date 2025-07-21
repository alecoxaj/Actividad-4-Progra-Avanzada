students = []

for i in range(5):
    name = input(f"Ingresa el nombre del Estudiante {i + 1}: ")
    notes = []
    for j in range(1, 4):
        note = float(input(f"Ingresa la nota {j} de {name}: "))
        notes.append(note)
    average = sum(notes) / 3
    students.append([name, notes, average])

    every_less_than_70 = True
    for est in students:
        if est[2] >= 70:
            every_less_than_70 = False
            break
    if every_less_than_70:
        print(f"\nAplicando curva de +5 puntos (máximo 100)... \n")
        for est in students:
            new_notes = []
            for note in est[1]:
                new = note + 5
                if new > 100:
                    new = 100
                new_notes.append(new)
            est[1] = new_notes
            est[2] = sum(new_notes)

    print("Nombre\t\tPromedio")
    print("-" * 25)
    for est in students:
        print(f"{est[0]:<15} {est[2]:.2f}")