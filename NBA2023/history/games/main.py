from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date
import time
import json
import os
import datetime
from urllib.parse import urlparse
import csv

from history_traditional import traditional_row
from history_traditional import advanced_row
from history_traditional import misc_row
from history_traditional import scoring_row
from history_traditional import usage_row
from history_data import history_data
from entity_table import EntityTable
from entity_element import EntityElement


def saveFile(data):
    # Parsear la URL
    # parsed_url = urlparse(url)
    # Obtener la ruta
    # path = parsed_url.path
    # Dividir la ruta por "/"
    # segments = path.split("/")
    # Eliminar segmentos vacíos
    # segments = [segment for segment in segments if segment]
    #id player
    idPlayer = data.id
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
    nombre_archivo = 'player_' + idPlayer + '.json'
    # Combinar la ruta del directorio actual con el nombre del archivo
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    # Save game structure to JSON file
    with open(ruta_archivo, 'w') as file:
        json.dump(data.to_dict(), file, indent=4)
    return 0

def saveFileCsv(data):
    #id player
    idPlayer = data.id
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
    nombre_archivo = 'player_' + idPlayer + '.csv'
    # dataCsv
    # dataCsv = [["NAME","YEAR","PTS"]]
    # for element in data.traditional_data:
    #     dataCsv.append([data.name,element.YEAR,element.PTS])
    # Combinar la ruta del directorio actual con el nombre del archivo
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    # Guardar los datos en el archivo CSV
    with open(ruta_archivo, mode='w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(data.to_csv())
    return 0

def saveFileCsvGeneric(data,file_name):
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
    nombre_archivo = file_name
    # Combinar la ruta del directorio actual con el nombre del archivo
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    # Guardar los datos en el archivo CSV
    with open(ruta_archivo, mode='w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(data.to_csv())
    return 0


# url de la data
all_player_link = "https://www.nba.com/stats/alltime-leaders?SeasonType=Regular+Season"
tableAllPlayers = extractAllPlayers(all_player_link)
# tableAllPlayers.print()
saveFileCsvGeneric(tableAllPlayers,'all_players.csv')
# url de la data
# home_link = "https://www.nba.com/stats/player/2544"
home_link = "https://www.nba.com/stats/player/2544?PerMode=Totals"
home_link_part_01 = "https://www.nba.com"
home_link_part_03 = "?PerMode=Totals"

for player in tableAllPlayers.body:
    print(player.array[2])
    home_link_part_02 = player.array[2]
    home_link_part_02 = home_link_part_02[:-1]
    home_link_player = home_link_part_01 + home_link_part_02 + home_link_part_03
    print(home_link_player)
    home_link = home_link_player
# data all players



# Save file in json url,history_data
# saveFile(data)
# Save file in csv url,history_data



