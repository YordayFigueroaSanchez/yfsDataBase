from datetime import date, timedelta

def obtener_dias_mes(anio, mes):
    # Determinar el primer día del mes
    primer_dia_mes = date(anio, mes, 1)
    
    # Calcular el último día del mes sumando un mes al primer día y restando un día
    ultimo_dia_mes = date(anio, mes % 12 + 1, 1) - timedelta(days=1)
    
    # Crear la lista con todos los días del mes
    dias_mes = [primer_dia_mes + timedelta(days=dia) for dia in range((ultimo_dia_mes - primer_dia_mes).days + 1)]
    
    return [str(dia) for dia in dias_mes]

# Ejemplo de uso
anio = 2023
mes = 8
dias_mes = obtener_dias_mes(anio, mes)
print(dias_mes)
