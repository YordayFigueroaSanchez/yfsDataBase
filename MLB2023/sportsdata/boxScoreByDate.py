import requests
import os
import json
import time
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
mes = 5
dias_mes = obtener_dias_mes(anio, mes)

listOfDate = dias_mes

directorio_actual = os.path.abspath(os.path.dirname(__file__))
directory = 'boxScore'
ruta = os.path.join(directorio_actual, directory)
if not os.path.exists(ruta):
    os.makedirs(ruta)

ruta_getMLBGamesForDate = os.path.join(directorio_actual, "gamesByDate")

for elementDate in listOfDate:
    print(elementDate)
    day = elementDate

    ruta_json = os.path.join(ruta_getMLBGamesForDate, day + ".json")

    with open(ruta_json, "r") as file:
        datos = json.load(file)

    games = datos

    for game in games:
        time.sleep(5)
        gameID = str(game["GameID"])
        away = game["AwayTeam"]
        home = game["HomeTeam"]
        
        print("gameID:", gameID)
        print("away:", away)
        print("home:", home)
        print()  # Agregamos una línea en blanco para separar las personas

        url = "https://api.sportsdata.io/v3/mlb/stats/json/BoxScore/"+ gameID +"?key=87172a8552914404994259782b1d8551"
        response = requests.get(url)
        print(response.json())

        nombre_archivo = day + "_" + gameID +'.json'
        ruta_complete = os.path.join(ruta, nombre_archivo)

        with open(ruta_complete, 'w') as archivo:
                json.dump(response.json(), archivo)