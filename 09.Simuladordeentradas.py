print("Bienvenido al Simulador de entradas de Cine con validación Múltiple")

age = int(input("Ingresa la edad: "))
weekday = input("Ingresa el día de la Semana: ")
Istudent = input("¿Es estudiante? (si/no): ")

if age <= 13:
    print("¡Acceso denegado! No puedes ingresar a películas para mayores de 15")
else:
    if Istudent == "si":
        price = 35
    else:
        price = 50

    if weekday == "miércoles":
        print("\n¡Promoción 2x1 activada!")
        print(f"Pagas Q{price:.2f} por 2 personas (Q{price:.2f} c/u)")
    else:
        print(f"\nPrecio de entrada: Q{price:.2f}")

