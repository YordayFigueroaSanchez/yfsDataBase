import os
import json
import csv
import pandas as pd
from datetime import datetime

# Obtener la ruta absoluta del directorio actual
directorio_actual = os.path.abspath(os.path.dirname(__file__))
directory = 'games_month_all'
directory_output = 'list_winner_table'
extension = '.json'
# Crear la ruta completa del directorio
ruta = os.path.join(directorio_actual, directory)
ruta_csv = os.path.join(directorio_actual, directory_output + '.csv')
archivos_json = [archivo for archivo in os.listdir(ruta) if archivo.endswith(extension)]

# Datos que deseas guardar en el archivo CSV
data_csv = []
data_csv.append(["date", "name", "category", "value"])
data_date   = []
data_name   = []
data_hr     = []
table       = {}
teams       = {
    'Boston Red Sox'            : {'wins': 0, 'group': 'ALEast'}, 
    'Baltimore Orioles'         : {'wins': 0, 'group': 'ALEast'}, 
    'Chicago Cubs'              : {'wins': 0, 'group': 'NLCentral'}, 
    'Milwaukee Brewers'         : {'wins': 0, 'group': 'NLCentral'}, 
    'Cincinnati Reds'           : {'wins': 0, 'group': 'NLCentral'}, 
    'Pittsburgh Pirates'        : {'wins': 0, 'group': 'NLCentral'}, 
    'Houston Astros'            : {'wins': 0, 'group': 'ALEast'}, 
    'Chicago White Sox'         : {'wins': 0, 'group': 'ALCentral'}, 
    'Kansas City Royals'        : {'wins': 0, 'group': 'ALCentral'}, 
    'Minnesota Twins'           : {'wins': 0, 'group': 'ALCentral'}, 
    'Los Angeles Dodgers'       : {'wins': 0, 'group': 'NLWest'}, 
    'Arizona Diamondbacks'      : {'wins': 0, 'group': 'NLWest'}, 
    'Miami Marlins'             : {'wins': 0, 'group': 'NLEast'}, 
    'New York Mets'             : {'wins': 0, 'group': 'NLEast'}, 
    'New York Yankees'          : {'wins': 0, 'group': 'ALEast'}, 
    'San Francisco Giants'      : {'wins': 0, 'group': 'NLWest'}, 
    'Oakland Athletics'         : {'wins': 0, 'group': 'ALEast'}, 
    'Los Angeles Angels'        : {'wins': 0, 'group': 'ALEast'}, 
    'San Diego Padres'          : {'wins': 0, 'group': 'NLWest'}, 
    'Colorado Rockies'          : {'wins': 0, 'group': 'NLWest'}, 
    'Seattle Mariners'          : {'wins': 0, 'group': 'ALEast'}, 
    'Cleveland Guardians'       : {'wins': 0, 'group': 'ALCentral'}, 
    'St. Louis Cardinals'       : {'wins': 0, 'group': 'NLCentral'}, 
    'Toronto Blue Jays'         : {'wins': 0, 'group': 'ALEast'}, 
    'Tampa Bay Rays'            : {'wins': 0, 'group': 'ALEast'}, 
    'Detroit Tigers'            : {'wins': 0, 'group': 'ALCentral'}, 
    'Texas Rangers'             : {'wins': 0, 'group': 'ALEast'}, 
    'Philadelphia Phillies'     : {'wins': 0, 'group': 'NLEast'}, 
    'Washington Nationals'      : {'wins': 0, 'group': 'NLEast'}, 
    'Atlanta Braves'            : {'wins': 0, 'group': 'NLEast'},
    }

teams_check       = {
    'Boston Red Sox'            : 0, 
    'Baltimore Orioles'         : 0, 
    'Chicago Cubs'              : 0, 
    'Milwaukee Brewers'         : 0, 
    'Cincinnati Reds'           : 0, 
    'Pittsburgh Pirates'        : 0, 
    'Houston Astros'            : 0, 
    'Chicago White Sox'         : 0, 
    'Kansas City Royals'        : 0, 
    'Minnesota Twins'           : 0, 
    'Los Angeles Dodgers'       : 0, 
    'Arizona Diamondbacks'      : 0, 
    'Miami Marlins'             : 0, 
    'New York Mets'             : 0, 
    'New York Yankees'          : 0, 
    'San Francisco Giants'      : 0, 
    'Oakland Athletics'         : 0, 
    'Los Angeles Angels'        : 0, 
    'San Diego Padres'          : 0, 
    'Colorado Rockies'          : 0, 
    'Seattle Mariners'          : 0, 
    'Cleveland Guardians'       : 0, 
    'St. Louis Cardinals'       : 0, 
    'Toronto Blue Jays'         : 0, 
    'Tampa Bay Rays'            : 0, 
    'Detroit Tigers'            : 0, 
    'Texas Rangers'             : 0, 
    'Philadelphia Phillies'     : 0, 
    'Washington Nationals'      : 0, 
    'Atlanta Braves'            : 0,
    }

# TODO
# eliminar los repetidos de teams en dias como el 18/04
# (OK) agregar los groups de la mlb 

def remove_duplicates_with_min_value(data_csv):
    duplicates = {}
    for row in data_csv[1:]:
        key = (row[0], row[1])
        if key in duplicates:
            if row[3] > duplicates[key][3]:
                duplicates[key] = row
        else:
            duplicates[key] = row

    return [data_csv[0]] + list(duplicates.values())

date_current = '20230330'
# {'Boston Red Sox': 0, 'Baltimore Orioles': 0, 'Chicago Cubs': 0, 'Milwaukee Brewers': 0, 'Cincinnati Reds': 0, 'Pittsburgh Pirates': 0, 'Houston Astros': 0, 'Chicago White Sox': 0, 'Kansas City Royals': 0, 'Minnesota Twins': 0, 'Los Angeles Dodgers': 0, 'Arizona Diamondbacks': 0, 'Miami Marlins': 0, 'New York Mets': 0, 'New York Yankees': 0, 'San Francisco Giants': 0, 'Oakland Athletics': 0, 'Los Angeles Angels': 0, 'San Diego Padres': 0, 'Colorado Rockies': 0, 'Seattle Mariners': 0, 'Cleveland Guardians': 0, 'St. Louis Cardinals': 0, 'Toronto Blue Jays': 0, 'Tampa Bay Rays': 0, 'Detroit Tigers': 0, 'Texas Rangers': 0, 'Philadelphia Phillies': 0, 'Washington Nationals': 0, 'Atlanta Braves': 0}
# {'Boston Red Sox': {'wins': 0, 'group': 'a'}, 'Baltimore Orioles': {'wins': 0, 'group': 'a'}, 'Chicago Cubs': {'wins': 0, 'group': 'a'}, 'Milwaukee Brewers': {'wins': 0, 'group': 'a'}, 'Cincinnati Reds': {'wins': 0, 'group': 'a'}, 'Pittsburgh Pirates': {'wins': 0, 'group': 'a'}, 'Houston Astros': {'wins': 0, 'group': 'a'}, 'Chicago White Sox': {'wins': 0, 'group': 'a'}, 'Kansas City Royals': {'wins': 0, 'group': 'a'}, 'Minnesota Twins': {'wins': 0, 'group': 'a'}, 'Los Angeles Dodgers': {'wins': 0, 'group': 'a'}, 'Arizona Diamondbacks': {'wins': 0, 'group': 'a'}, 'Miami Marlins': {'wins': 0, 'group': 'a'}, 'New York Mets': {'wins': 0, 'group': 'a'}, 'New York Yankees': {'wins': 0, 'group': 'a'}, 'San Francisco Giants': {'wins': 0, 'group': 'a'}, 'Oakland Athletics': {'wins': 0, 'group': 'a'}, 'Los Angeles Angels': {'wins': 0, 'group': 'a'}, 'San Diego Padres': {'wins': 0, 'group': 'a'}, 'Colorado Rockies': {'wins': 0, 'group': 'a'}, 'Seattle Mariners': {'wins': 0, 'group': 'a'}, 'Cleveland Guardians': {'wins': 0, 'group': 'a'}, 'St. Louis Cardinals': {'wins': 0, 'group': 'a'}, 'Toronto Blue Jays': {'wins': 0, 'group': 'a'}, 'Tampa Bay Rays': {'wins': 0, 'group': 'a'}, 'Detroit Tigers': {'wins': 0, 'group': 'a'}, 'Texas Rangers': {'wins': 0, 'group': 'a'}, 'Philadelphia Phillies': {'wins': 0, 'group': 'a'}, 'Washington Nationals': {'wins': 0, 'group': 'a'}, 'Atlanta Braves': {'wins': 0, 'group': 'a'}}
for archivo in archivos_json:
    print(archivo)
    ruta_completa = os.path.join(ruta, archivo)  # Obtiene la ruta completa del archivo
    with open(ruta_completa, 'r', encoding="utf-8") as archivo_json:
        datos = json.load(archivo_json)  # Carga los datos JSON del archivo en un diccionario
    # si la fecha es diferente a la date_current, completar los team que no tengan registro para el dia
    if date_current != datos["date"] :
        # recorrer los teams y determinar cual no tiene registro
        # llenar el dia con data para todos los team
        for team, info in teams_check.items():
            print(f"Equipo: {team}, Info: {info}")
            if info == 0 :
                print(f"Equipo: {team}, faltante")
                data_csv.append([datetime.strptime(date_current, '%Y%m%d').strftime('%d/%m/%Y'), team, teams[team]['group'], str(teams[team]['wins'])])
            teams_check[team] = 0
        # limpiar el registro de teams para procesar la proxima fecha
        # actualizar la date_current
        date_current = datos["date"]

    fecha = datetime.strptime(datos["date"], '%Y%m%d')
    game_date = fecha.strftime('%d/%m/%Y')
    home_team_name = datos["home_team"]["name"]
    if teams.get(home_team_name) is None:
        teams[home_team_name]= {'wins':0, 'group':'a'}
    teams_check[home_team_name] = 1
    home_team_category = "a"
    home_team_value = "0"
    home_team_runs = int(datos["home_team"]["runs"])

    away_team_name = datos["away_team"]["name"]
    if teams.get(away_team_name) is None:
        teams[away_team_name] = {'wins':0, 'group':'a'}
    teams_check[away_team_name] = 1
    away_team_category = "b"
    away_team_value = "0"
    away_team_runs = int(datos["away_team"]["runs"])

    if home_team_runs > away_team_runs :
        home_team_value = "1"
        teams[home_team_name]['wins'] += 1
    else :
        away_team_value = "1"
        teams[away_team_name]['wins'] += 1

    data_csv.append([game_date, home_team_name, teams[home_team_name]['group'], str(teams[home_team_name]['wins'])])
    data_csv.append([game_date, away_team_name, teams[away_team_name]['group'], str(teams[away_team_name]['wins'])])

# Eliminar duplicados con el menor valor de 'value'
data_csv_without_duplicates = remove_duplicates_with_min_value(data_csv)    

# Abre el archivo CSV en modo escritura
with open(ruta_csv, mode='w', newline='', encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Escribe los datos en el archivo CSV
    for fila in data_csv_without_duplicates:
        escritor_csv.writerow(fila)

# Crear un DataFrame desde los datos CSV originales
# data = {
#     "Date": data_date,
#     "Name": data_name,
#     "HR": data_hr
# }
# print(data_hr)


# TEST 02
print(teams)
# Obtener la lista de nombres de bateadores únicos
# ruta_csv = os.path.join(directorio_actual, directory_output + '_pivot.csv')
# nombres_bateadores = set()
# for datos_bateadores in table.values():
#     nombres_bateadores.update(datos_bateadores.keys())

# Abrir el archivo CSV en modo de escritura
# with open(ruta_csv, 'w', newline='', encoding="utf-8") as csvfile:
#     csv_writer = csv.writer(csvfile)
    
#     encabezados = ['Fecha'] + list(nombres_bateadores)
#     csv_writer.writerow(encabezados)
    
#     for fecha, datos_bateadores in table.items():
#         fila = [fecha]
#         for bateador in nombres_bateadores:
#             fila.append(datos_bateadores.get(bateador, 0))
#         csv_writer.writerow(fila)
