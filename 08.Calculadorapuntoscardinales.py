print("Bienvenido")

print("Opciones: norte, sur, este, oeste")

origin = input("Ingresa la primera dirección (origen): ")
destiny = input("Ingresa la segunda dirección (destino): ")

if origin == destiny:
    print("Ya estás en la dirección")
else:
    course = ""

    if origin == "norte" and destiny == "sur":
        course = "recto hacia el sur"
    elif origin == "sur" and destiny == "norte":
        course = "recto hacia el norte"
    elif origin == "este" and destiny == "oeste":
        course = "recto hacia el oeste"
    elif origin == "oeste" and destiny == "este":
        course = "recto hacia el este"

    elif (origin == "norte" and destiny == "sur") or (origin == "este" and destiny == "oeste"):
        course = "noreste"
    elif (origin == "sur" and destiny == "norte") or (origin == "oeste" and destiny == "norte"):
        course = "noroeste"
    elif (origin == "sur" and destiny == "este") or (origin == "este" and destiny == "sur"):
        course = "sureste"
    elif (origin == "sur" and destiny == "oeste") or (origin == "oeste" and destiny == "sur"):
        course = "suroeste"

    if course == "":
        course = ("Dirección no reconocida")

    print(f"Debe moverse a: ", course)

