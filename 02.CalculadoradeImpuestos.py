print("Bienvenido a la Calculadora de impuestos")

annualincome = float(input("Ingresa tus ingresos anuales: "))
dependentnumber = int(input("Ingresa tu número de dependentes: "))

deduction = dependentnumber * 1000
deducted_income = annualincome - deduction

if annualincome < 40000 and dependentnumber > 2:
    tax = 0
    print("\n¡Exonerado de impuestos por ingreso menor a Q40,000 y más de 2 dependientes!")
else:
    tax = 0

    if deduction <= 30000:
        tax = deducted_income * 0.05
    elif deduction <= 60000:
        tax = (30000 * 0.05) + ((deducted_income - 30000) * 0.10)
    elif deduction <= 100000:
        tax = (30000 * 0.05) + (30000 * 0.10) + ((deducted_income - 60000) * 0.15)
    else:
        tax = (30000 * 0.05) + (30000 * 0.10 ) +(40000 * 0.15) + ((deducted_income - 10000) * 0.20)


print(f"\nIngreso bruto:  Q{annualincome:,.2f}")
print(f"Deducción por dependientes ({dependentnumber}): Q{deduction:,.2f}")
print(f"Ingreso después de deducción: Q{deducted_income:,.2f}")
print(f"Impuesto a pagar: Q{tax:,.2f}")