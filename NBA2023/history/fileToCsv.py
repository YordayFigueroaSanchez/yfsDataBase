import csv
import os
import datetime



# Datos a guardar en el archivo CSV
datos = [
    ['Nombre', 'Apellido', 'Edad'],
    ['John', 'Doe', 30],
    ['Jane', 'Smith', 25],
    ['Bob', 'Johnson', 35]
]

# Obtener la fecha actual
fecha_actual = datetime.date.today()
# Formatear la fecha en AAAAMMDD
fecha_formateada = fecha_actual.strftime("%Y%m%d")
# Obtener la ruta absoluta del directorio actual
directorio_actual = os.path.abspath(os.path.dirname(__file__))
# Nombre del directorio donde deseas guardar el archivo
nombre_directorio = fecha_formateada
# Crear la ruta completa del directorio
ruta_directorio = os.path.join(directorio_actual, nombre_directorio)
# Comprobar si el directorio existe, si no, crearlo
if not os.path.exists(ruta_directorio):
    os.makedirs(ruta_directorio)
# Nombre del archivo que deseas guardar
nombre_archivo = 'player_' + '123456' + '.csv'
# Combinar la ruta del directorio actual con el nombre del archivo
ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)

# Ruta del archivo CSV
archivo_csv = 'datos.csv'

# Guardar los datos en el archivo CSV
with open(ruta_archivo, mode='w', newline='') as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerows(datos)

print(f"Los datos se han guardado correctamente en {ruta_archivo}.")
