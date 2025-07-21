print("Bienvenido ")

weight = float(input("Ingresa el peso del paquete en kg: "))
distance = float(input("Ingresa la distancia en km: "))
urgent = input("¿Es urgente? (si/no): ")
size = input("Tamaño del paquete (pequeño/mediano/grande): ").lower()

base_cost = (weight * 10) + (distance * 0.5)


total = base_cost

print("\nDesglose de envío")
print(f"Costo base (peso y distancia): Q{base_cost:.2f}")

if urgent == "si":
    total += 50
    print("Recargo por urgencia: +Q50")

if size == "grannde":
    total += 30
    print("Recargo por tamaño grande: +Q30")

if urgent == "no" and weight < 5:
    total -= 20
    print("Descuento por peso < 5kg y no urgente: -Q20")

print(f"Total a pagar: {total:,.2f}")