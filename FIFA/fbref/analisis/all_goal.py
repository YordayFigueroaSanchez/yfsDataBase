import os
import json
import csv
import pandas as pd
from datetime import datetime
from itertools import cycle
from utils import dateInYYYYMMDD_MMSS
from utils import listar_archivos_json

directorio_actual = os.path.abspath(os.path.dirname(__file__))
extension = '.json'
file_out = 'all_goal_' + dateInYYYYMMDD_MMSS()
rutas_especificas = [
    os.path.join(directorio_actual, '..', "1930", 'game', '20231113_2135', 'json'), 
    os.path.join(directorio_actual, '..', "1934", 'game', '20231119_2123', 'json'), 
    os.path.join(directorio_actual, '..', "1938", 'game', '20231120_1207', 'json'), 
    ]
archivos_json = listar_archivos_json(rutas_especificas)

# Imprimir la lista de archivos JSON encontrados en ambas rutas
# print("Archivos JSON en las rutas {}: {}".format(rutas_especificas, archivos_json))

# Crear la ruta completa del directorio
ruta_csv = os.path.join(directorio_actual, file_out + '.csv')

data_csv = []
data_csv.append(["Date", "Name", "Goal"])
table       = {}
for archivo in archivos_json:
    print(archivo)
    with open(archivo, 'r', encoding="utf-8") as archivo_json:
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
with open(ruta_csv, mode='w', newline='', encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for fila in data_csv:
        escritor_csv.writerow(fila)
table_acumulador = {}
player_list = {}
for date in table:
    for player in table[date]:
        if player not in player_list:
            player_list[player] = 0
for date in table:
    for player, value in table[date].items():
        player_list[player] += int(value)
    date_object = datetime.strptime(date, '%Y%m%d')
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