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
directory = '1934'
extension = '.json'
file_out = 'all_goal_1934_' + dateInYYYYMMDD_MMSS()
# Crear la ruta completa del directorio
ruta = os.path.join(directorio_actual, directory)
ruta_json = os.path.join(directorio_actual,  '..', directory, 'game', '20231119_2123', 'json')
ruta_csv = os.path.join(directorio_actual, file_out + '.csv')
archivos_json = [archivo for archivo in os.listdir(ruta) if archivo.endswith(extension)]

# Datos que deseas guardar en el archivo CSV
data_csv = []
data_csv.append(["Date", "Name", "Goal"])
data_date   = []
data_name   = []
data_feature     = []
table       = {}
for archivo in archivos_json:
    print(archivo)
    ruta_completa = os.path.join(ruta_json, archivo)  # Obtiene la ruta completa del archivo
    with open(ruta_completa, 'r', encoding="utf-8") as archivo_json:
        datos = json.load(archivo_json)  # Carga los datos JSON del archivo en un diccionario

    # Aquí puedes trabajar con los datos como lo harías con un diccionario de Python
    for batter in datos["home_team"]["players"]:
        if batter['goals'] != "":
            fecha = datos["date"]
            nombre_bateador = batter["name"] + ' (' + datos["home_team"]["name"] + ')'
            feature = batter["goals"]
            data_csv.append([fecha, nombre_bateador, feature])
            # data_date.append(datos["date"])
            # data_name.append(batter["name"])
            # data_feature.append(batter["goals"])
            # Verificar si la clave '20230401' existe en el diccionario table
            if fecha in table:
                # Verificar si la clave 'nombre_bateador' existe en el diccionario anidado
                if nombre_bateador in table[fecha]:
                    # La clave 'nombre_bateador' existe, actualiza el valor
                    table[fecha][nombre_bateador] = str(int(table[fecha][nombre_bateador]) + int(feature))
                else:
                    # La clave 'nombre_bateador' no existe, crea una nueva entrada
                    table[fecha][nombre_bateador] = feature
            else:
                # La clave 'fecha' no existe, crea una nueva entrada con el diccionario anidado
                table[fecha] = {nombre_bateador: feature}

    for batter in datos["away_team"]["players"]:
        if batter['goals'] != "":
            fecha = datos["date"]
            nombre_bateador = batter["name"] + ' (' + datos["away_team"]["name"] + ')'
            feature = batter["goals"]
            data_csv.append([fecha, nombre_bateador, feature])
            # data_date.append(datos["date"])
            # data_name.append(batter["name"])
            # data_feature.append(batter["goals"])
            if fecha in table:
                # Verificar si la clave 'nombre_bateador' existe en el diccionario anidado
                if nombre_bateador in table[fecha]:
                    # La clave 'nombre_bateador' existe, actualiza el valor
                    table[fecha][nombre_bateador] = str(int(table[fecha][nombre_bateador]) + int(feature))
                else:
                    # La clave 'nombre_bateador' no existe, crea una nueva entrada
                    table[fecha][nombre_bateador] = feature
            else:
                # La clave 'fecha' no existe, crea una nueva entrada con el diccionario anidado
                table[fecha] = {nombre_bateador: feature}


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

ruta_csv = os.path.join(directorio_actual, file_out + '_pivot.csv')
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

