import os
import json
import csv
import pandas as pd
from datetime import datetime
from itertools import cycle
from utils import dateInYYYYMMDD_MMSS

# Obtener la ruta absoluta del directorio actual
directorio_actual = os.path.abspath(os.path.dirname(__file__))
directory = '1930'
extension = '.json'
file_out = 'all_goal_1930_' + dateInYYYYMMDD_MMSS()
# Crear la ruta completa del directorio
ruta = os.path.join(directorio_actual, directory)
ruta_json = os.path.join(directorio_actual,  '..', directory, 'game', '20231113_2135', 'json')
ruta_csv = os.path.join(directorio_actual, file_out + '.csv')
archivos_json = [archivo for archivo in os.listdir(ruta_json) if archivo.endswith(extension)]
# Datos que deseas guardar en el archivo CSV
data_csv = []
data_csv.append(["Date", "Name", "Goal"])
table       = {}
for archivo in archivos_json:
    print(archivo)
    ruta_completa = os.path.join(ruta_json, archivo)
    with open(ruta_completa, 'r', encoding="utf-8") as archivo_json:
        datos = json.load(archivo_json)
    for batter in datos["home_team"]["players"]:
        if batter['goals'] != "":
            fecha = datos["date"]
            nombre_bateador = batter["name"] + ' (' + datos["home_team"]["name"] + ')'
            feature = batter["goals"]
            data_csv.append([fecha, nombre_bateador, feature])
            if fecha in table:
                if nombre_bateador in table[fecha]:
                    table[fecha][nombre_bateador] = str(int(table[fecha][nombre_bateador]) + int(feature))
                else:
                    table[fecha][nombre_bateador] = feature
            else:
                table[fecha] = {nombre_bateador: feature}
    for batter in datos["away_team"]["players"]:
        if batter['goals'] != "":
            fecha = datos["date"]
            nombre_bateador = batter["name"] + ' (' + datos["away_team"]["name"] + ')'
            feature = batter["goals"]
            data_csv.append([fecha, nombre_bateador, feature])
            if fecha in table:
                if nombre_bateador in table[fecha]:
                    table[fecha][nombre_bateador] = str(int(table[fecha][nombre_bateador]) + int(feature))
                else:
                    table[fecha][nombre_bateador] = feature
            else:
                table[fecha] = {nombre_bateador: feature}
# Abre el archivo CSV en modo escritura
with open(ruta_csv, mode='w', newline='', encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for fila in data_csv:
        escritor_csv.writerow(fila)
# Acumulador para estadísticas
table_acumulador = {}
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
# print(table_acumulador)
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
    for fecha, datos_bateadores in table_acumulador.items():
        fila = [fecha]
        for bateador in nombres_bateadores:
            fila.append(datos_bateadores.get(bateador, 0))
        csv_writer.writerow(fila)

