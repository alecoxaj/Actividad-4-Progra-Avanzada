print("¡Bienvenido al Simulador! ")
name = input("Ingresa tu Nombre Completo: ")

if len(name.strip()) < 5:
    print("¡Nombre inválido! Debe tener al menos 5 letras")
elif True:
    DPI = input("Ingresa el No. de DPI (13 dígitos): ").strip()
    if not DPI.isdigit() or len(DPI) != 13:
        print("¡DPI Inválido! Debe tener al menos 13 dígitos")
    elif True:
        dep = input("Ingresa el Departamento: ").strip()
        birthdate = int(input("Ingresa tu año de nacimiento:  "))

        currentyear = 2025
        age = currentyear - birthdate

        if (dep == "Petén" or dep == "Alta Verapaz") and age >= 17:
            print("¡Bienvenido", name +"!","tu centro de votación está en", dep + ".")
        elif age >= 18:
            print("¡Bienvenido", name +"!","tu centro de votación está en", dep + ".")
        else:
            print("No cumples con la edad mínima para votar.")

