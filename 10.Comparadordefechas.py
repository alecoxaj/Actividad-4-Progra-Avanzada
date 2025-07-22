print("Bienvenido")
print("\nPrimera fecha:")
day1 = int(input("Día: "))
month1 = int(input("Mes (en números): "))
year1 = int(input("Año: "))

print("\nSegunda fecha: ")
day2 = int(input("Día: "))
month2 = int(input("Mes (en números): "))
year2 = int(input("Año: "))

if year1 > year2:
    print("\nLa primera fecha es mayor")
elif year1 < year2:
    print("\nLa segunda fecha es mayor")
else:
    if month1 > month2:
        print("La primera fecha es mayor")
    elif month1 < month2:
        print("La segunda fecha es mayor")
    else:
        if day1 > day2:
            print("\nLa primera fecha es mayor")
        elif day2 < day1:
            print("\nLa segunda fecha es mayor")
        else:
            print("\nAmbas fechas son iguales")

if month1 == month2 and year1 == year2:
    print("Ambas fechas están en el mismo mes y año.")
else:
    print("Las fechas están en meses o años distintos.")

total1 = year1 * 365 + month1 * 30 + day1
total2 = year2 * 365 + month2 * 30 + day2
diference= total1 - total2

if diference < 0:
    diference = diference * -1

print("Días transcurridos entre ambas fechas:", diference, "días.")

