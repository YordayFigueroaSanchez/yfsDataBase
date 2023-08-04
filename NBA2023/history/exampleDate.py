import datetime

# Obtener la fecha actual
fecha_actual = datetime.date.today()

# Formatear la fecha en AAAAMMDD
fecha_formateada = fecha_actual.strftime("%Y%m%d")

print("Fecha actual en formato AAAAMMDD:", fecha_formateada)
