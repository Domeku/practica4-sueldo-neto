# ============================================================
# Práctica 4: Cálculo de Sueldo Neto
# Curso: Programación en Python
# Descripción: Calcula el sueldo neto de un empleado aplicando
#              descuentos de TSS, ISR, bonificación y otros.
#
# Valores investigados según normativa dominicana (DGII / TSS):
#   - TSS (Seguridad Social empleado): 3.04% del sueldo bruto
#   - ISR: Escala progresiva DGII 2024 (exento hasta RD$34,685.67/mes)
#   - Bonificación: 8.33% del sueldo (equivale a un sueldo extra / 12)
# ============================================================

# --- CONSTANTES (valores oficiales RD) ---
TSS_PORCENTAJE      = 0.0304   # 3.04% descuento seguridad social (empleado)
BONIFICACION_PORCENTAJE = 0.0833  # 8.33% bonificación mensual (1 mes / 12)

# Tramos ISR mensual 2024 según DGII (en pesos dominicanos)
ISR_TRAMO_1_LIMITE  = 34685.67   # Exento hasta este monto
ISR_TRAMO_2_LIMITE  = 52027.50
ISR_TRAMO_3_LIMITE  = 69370.00
ISR_TRAMO_4_LIMITE  = float('inf')  # Todo lo que supere el tramo 3

ISR_TRAMO_2_TASA    = 0.15   # 15% sobre el excedente del tramo 1
ISR_TRAMO_3_TASA    = 0.20   # 20% sobre el excedente del tramo 2
ISR_TRAMO_4_TASA    = 0.25   # 25% sobre el excedente del tramo 3

# ============================================================
# FUNCIÓN: Calcula el ISR según los tramos de la DGII
# ============================================================
def calcular_isr(sueldo_bruto):
    """Calcula la retención del ISR mensual según tramos DGII."""
    if sueldo_bruto <= ISR_TRAMO_1_LIMITE:
        # Exento: no paga ISR
        return 0.0
    elif sueldo_bruto <= ISR_TRAMO_2_LIMITE:
        # 15% sobre el excedente del primer límite
        return (sueldo_bruto - ISR_TRAMO_1_LIMITE) * ISR_TRAMO_2_TASA
    elif sueldo_bruto <= ISR_TRAMO_3_LIMITE:
        # 15% del tramo 2 completo + 20% sobre el excedente
        isr  = (ISR_TRAMO_2_LIMITE - ISR_TRAMO_1_LIMITE) * ISR_TRAMO_2_TASA
        isr += (sueldo_bruto - ISR_TRAMO_2_LIMITE) * ISR_TRAMO_3_TASA
        return isr
    else:
        # 15% + 20% completos + 25% sobre el excedente del tramo 3
        isr  = (ISR_TRAMO_2_LIMITE - ISR_TRAMO_1_LIMITE) * ISR_TRAMO_2_TASA
        isr += (ISR_TRAMO_3_LIMITE - ISR_TRAMO_2_LIMITE) * ISR_TRAMO_3_TASA
        isr += (sueldo_bruto - ISR_TRAMO_3_LIMITE) * ISR_TRAMO_4_TASA
        return isr

# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 50)
print("   CALCULADORA DE SUELDO NETO - REPÚBLICA DOMINICANA")
print("=" * 50)

# --- Entrada del sueldo bruto con validación ---
while True:
    try:
        sueldo_bruto = float(input("\nIngrese el sueldo bruto mensual (RD$): "))
        if sueldo_bruto <= 0:
            print("⚠  El sueldo bruto debe ser un valor positivo. Intente de nuevo.")
        else:
            break  # Valor válido, salir del bucle
    except ValueError:
        print("⚠  Entrada inválida. Ingrese un número válido.")

# --- Entrada de otros descuentos con validación ---
while True:
    try:
        otros_descuentos = float(input("Ingrese otros descuentos (RD$) [0 si no aplica]: "))
        if otros_descuentos < 0:
            print("⚠  Los descuentos no pueden ser negativos. Intente de nuevo.")
        else:
            break
    except ValueError:
        print("⚠  Entrada inválida. Ingrese un número válido.")

# --- ¿Aplica bonificación? ---
aplica_bonificacion = input("¿El empleado recibe bonificación? (s/n): ").strip().lower()

# ============================================================
# CÁLCULOS
# ============================================================

# Descuento por Seguridad Social (TSS)
descuento_tss = sueldo_bruto * TSS_PORCENTAJE

# Retención ISR (usando función con tramos DGII)
retencion_isr = calcular_isr(sueldo_bruto)

# Bonificación (solo si aplica)
if aplica_bonificacion == 's':
    bonificacion = sueldo_bruto * BONIFICACION_PORCENTAJE
else:
    bonificacion = 0.0

# Total de descuentos
total_descuentos = descuento_tss + retencion_isr + otros_descuentos

# Sueldo Neto = Sueldo Bruto - Descuentos + Bonificación
sueldo_neto = sueldo_bruto - total_descuentos + bonificacion

# ============================================================
# MOSTRAR RESULTADOS
# ============================================================

print("\n" + "=" * 50)
print("           RESUMEN DE NÓMINA")
print("=" * 50)
print(f"  Sueldo Bruto:                  RD$ {sueldo_bruto:>12,.2f}")
print("-" * 50)
print(f"  Descuento TSS (3.04%):         RD$ {descuento_tss:>12,.2f}")
print(f"  Retención ISR:                 RD$ {retencion_isr:>12,.2f}")
print(f"  Otros Descuentos:              RD$ {otros_descuentos:>12,.2f}")
print(f"  Total Descuentos:              RD$ {total_descuentos:>12,.2f}")
print("-" * 50)

if aplica_bonificacion == 's':
    print(f"  Bonificación (8.33%):          RD$ {bonificacion:>12,.2f}")
    print("-" * 50)

print(f"  SUELDO NETO:                   RD$ {sueldo_neto:>12,.2f}")
print("=" * 50)