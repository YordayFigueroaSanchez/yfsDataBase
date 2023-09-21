import requests
import os
import json
import time

day = "20230709"
url = "https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBBoxScore"

headers = {
	"X-RapidAPI-Key": "f7c8fc8c64msh5fe2cb8870ad258p1c59eejsn8daa1f794366",
	"X-RapidAPI-Host": "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
}

directory = 'getMLBBoxScore'

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_getMLBGamesForDate = os.path.join(directorio_actual, "getMLBGamesForDate")
ruta_json = os.path.join(ruta_getMLBGamesForDate, day + ".json")

ruta = os.path.join(directorio_actual, directory)
if not os.path.exists(ruta):
    os.makedirs(ruta)


with open(ruta_json, "r") as file:
    datos = json.load(file)

games = datos["body"]

for game in games:
    time.sleep(5)
    gameID = game["gameID"]
    away = game["away"]
    home = game["home"]
    
    print("gameID:", gameID)
    print("away:", away)
    print("home:", home)
    print()  # Agregamos una línea en blanco para separar las personas

    querystring = {"gameID":gameID}
    response = requests.get(url, headers=headers, params=querystring)
    nombre_archivo = gameID.replace("@", "_") +'.json'
    ruta_complete = os.path.join(ruta, nombre_archivo)
    with open(ruta_complete, 'w') as archivo:
        json.dump(response.json(), archivo)

