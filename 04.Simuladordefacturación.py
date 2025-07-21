print("Bienvenido al simulador de facturación ")

prices = []

price = -1
while price != 0:
    entry = input("Ingresa el precio del producto (0 para terminar): Q")

    if entry.replace(".","").isdigit():
        price = float(entry)

        if price == 0:
            break
        elif price < 0:
            print("El precio no puede ser negativo")
        else:
            prices.append(price)
    else:
        print("¡Entrada inválida! Ingresa sólo números positivos")

subtotal = sum(prices)
print(f"\nSubtotal: Q{subtotal:,.2f}")

tip = 0
res_trip = input("¿Deseas dejer propina? (si/no)")
if res_trip == "si" or res_trip == "SI":
    porcentage_text = input("¿Cuánto porcentaje de propina deseas dejar?: ")
    if porcentage_text.replace(".","").isdigit():
        porcentage = float(porcentage_text)
        if porcentage >= 0:
            total_tip = subtotal * (porcentage / 100)
        else:
            print("La propina no puede ser negativa")
    else:
        print("¡Entrada Inválida!. No se aplicará propina")

discount = 0
card = input("¿Tienes tarjeta cliente frecuente? (si/no): ")
if card == "si" or card == "SI":
    discount = subtotal * 0.10

iva = subtotal * 0.12
total = subtotal + iva + tip - discount

print(f"\nFACTURA FINAL")
print(f"Subtotal: Q{subtotal:,.2f}")
print(f"IVA (12%): Q{iva:,.2f}")
print(f"Propina: Q{tip:,.2f}")
print(f"Descuento: Q{discount:,.2f}")
print(f"TOTAL A PAGAR: Q{total:,.2f}")



