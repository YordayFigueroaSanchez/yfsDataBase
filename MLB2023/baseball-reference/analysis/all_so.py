import os
import json
import csv
import pandas as pd
from datetime import datetime
from itertools import cycle

def dateInYYYYMMDD_MMSS():
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    # Formatear la fecha en AAAAMMDD
    fecha_formateada = fecha_actual.strftime("%Y%m%d")
    # Formatear la hora en HHMM
    hora_formateada = fecha_actual.strftime("%H%M")
    # Combinar la fecha y la hora con _
    fecha_resultante = fecha_formateada + "_" + hora_formateada
    return fecha_resultante

# Obtener la ruta absoluta del directorio actual
directorio_actual = os.path.abspath(os.path.dirname(__file__))
directory = 'games_month_all'
directory_to_save = os.path.join(directorio_actual, 'all_so')
extension = '.json'
file_out = 'all_so_' + dateInYYYYMMDD_MMSS()

if not os.path.exists(directory_to_save):
    try:
        # Crear un directorio
        os.mkdir(directory_to_save)
        print(f"Directorio {directory_to_save} creado con éxito.")
    except Exception as e:
        print(f"Se produjo un error al intentar crear el directorio: {e}")
else:
    print(f"El directorio {directory_to_save} ya existe.")

# Crear la ruta completa del directorio
ruta = os.path.join(directorio_actual, directory)
ruta_csv = os.path.join(directory_to_save, file_out + '.csv')
archivos_json = [archivo for archivo in os.listdir(ruta) if archivo.endswith(extension)]

# Datos que deseas guardar en el archivo CSV
data_csv = []
data_csv.append(["Date", "Name", "SO"])
data_date   = []
data_name   = []
data_feature     = []
table       = {}
for archivo in archivos_json:
    print(archivo)
    ruta_completa = os.path.join(ruta, archivo)  # Obtiene la ruta completa del archivo
    with open(ruta_completa, 'r', encoding="utf-8") as archivo_json:
        datos = json.load(archivo_json)  # Carga los datos JSON del archivo en un diccionario

    # Aquí puedes trabajar con los datos como lo harías con un diccionario de Python
    for pitchers in datos["home_team"]["pitchers"]:
        if pitchers['SO'] != "":
            data_csv.append([datos["date"], pitchers['name'], pitchers['SO']])
            data_date.append(datos["date"])
            data_name.append(pitchers["name"])
            data_feature.append(pitchers["SO"])
            # Verificar si la clave '20230401' existe en el diccionario table
            fecha = datos["date"]
            nombre_jugador = pitchers["name"]
            feature = pitchers["SO"]
            if fecha in table:
                # Verificar si la clave 'nombre_bateador' existe en el diccionario anidado
                if nombre_jugador in table[fecha]:
                    # La clave 'nombre_bateador' existe, actualiza el valor
                    table[fecha][nombre_jugador] = str(int(table[fecha][nombre_jugador]) + int(feature))
                else:
                    # La clave 'nombre_bateador' no existe, crea una nueva entrada
                    table[fecha][nombre_jugador] = feature
            else:
                # La clave 'fecha' no existe, crea una nueva entrada con el diccionario anidado
                table[fecha] = {nombre_jugador: feature}

    for pitchers in datos["away_team"]["pitchers"]:
        if pitchers['SO'] != "":
            data_csv.append([datos["date"], pitchers['name'], pitchers['SO']])
            data_date.append(datos["date"])
            data_name.append(pitchers["name"])
            data_feature.append(pitchers["SO"])
            fecha = datos["date"]
            nombre_jugador = pitchers["name"]
            feature = pitchers["SO"]
            if fecha in table:
                # Verificar si la clave 'nombre_bateador' existe en el diccionario anidado
                if nombre_jugador in table[fecha]:
                    # La clave 'nombre_bateador' existe, actualiza el valor
                    table[fecha][nombre_jugador] = str(int(table[fecha][nombre_jugador]) + int(feature))
                else:
                    # La clave 'nombre_bateador' no existe, crea una nueva entrada
                    table[fecha][nombre_jugador] = feature
            else:
                # La clave 'fecha' no existe, crea una nueva entrada con el diccionario anidado
                table[fecha] = {nombre_jugador: feature}


# Abre el archivo CSV en modo escritura
with open(ruta_csv, mode='w', newline='', encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Escribe los datos en el archivo CSV
    for fila in data_csv:
        escritor_csv.writerow(fila)

# Acumulador para estadísticas
table_acumulador = {}

# print(table)
# construir una lista con todos los nombre de jugador como key y valor 0
player_list = {}

for date in table:
    for player in table[date]:
        if player not in player_list:
            player_list[player] = 0

# print(player_list)


for date in table:
    for player, value in table[date].items():
        player_list[player] += int(value)
    # Convertir la cadena a un objeto datetime
    date_object = datetime.strptime(date, '%Y%m%d')
    # Formatear la fecha en el formato deseado (YYYY-MM-DD)
    formatted_date = date_object.strftime('%Y-%m-%d')
    table_acumulador[formatted_date] = player_list.copy()

print(table_acumulador)

colors_select = ['#0086F9','#FF4131','#FEBD00','#c71cda','#15004b']

ruta_csv = os.path.join(directory_to_save, file_out + '_pivot.csv')
nombres_bateadores = set()
for datos_bateadores in table_acumulador.values():
    nombres_bateadores.update(datos_bateadores.keys())
with open(ruta_csv, 'w', newline='', encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    encabezados = ['Date / Title'] + list(nombres_bateadores)
    csv_writer.writerow(encabezados)
    imagen_row = ['Image'] + [''] * (len(nombres_bateadores)+1)
    csv_writer.writerow(imagen_row)
    list_color = [x for x, _ in zip(cycle(colors_select), range(len(nombres_bateadores)))]
    bar_color_row = ['Bar Color'] + list_color
    csv_writer.writerow(bar_color_row)
    # diccionario_jugadores = {jugador: 0 for jugador in nombres_bateadores}
    for fecha, datos_bateadores in table_acumulador.items():
        fila = [fecha]
        for bateador in nombres_bateadores:
            fila.append(datos_bateadores.get(bateador, 0))
        csv_writer.writerow(fila)

