"""
Comisiones de un vendedor.
"""

# Entradas
ventas = 0
for dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
    ventas += float(input(f"Ventas {dia}: "))

# Proceso
if ventas > 20_000:
    porcentaje = 6
else:
    porcentaje = 5
comision = ventas * porcentaje / 100

# Salidas
print()
print("Ventas totales:", ventas)
print(f"Comisión ({porcentaje}%): {comision}")
