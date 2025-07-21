day = int(input("Ingresa el día: "))
month = int(input("Ingresa el mes (en números): "))
year = int(input("Ingresa el año: "))

valid = True

if month in [1, 3, 5, 7, 8, 10, 12]:
    if day < 1 or day > 31:
        valid = False

elif month in [4, 6, 9, 11]:
    if day < 1 or day > 30:
        valido = False

elif month == 2:
    leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if leap:
        if day < 1 or day > 29:
            valido = False
    else:
        if day < 1 or day > 28:
            valid= False
else:
    valid = False

if not valid:
    print("¡Fecha inválida!")
else:
    m = month
    y = year
    if m < 3:
        m += 12
        y -= 1

    K = y % 100
    J = y // 100

    h = (day + (13*(m + 1)) // 5 + K + (K // 4) + (J // 4) + 5*J) % 7

    weekdays = ["sábado", "domingo", "lunes", "martes", "miércoles", "jueves", "viernes"]

    print(f"La fecha {day:02d}/{month:02d}/{year} fue un {weekdays[h]}")
