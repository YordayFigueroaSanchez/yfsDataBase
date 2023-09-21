import requests
import os
import datetime
import json

parameter = "20230712"

url = "https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBGamesForDate"

querystring = {"gameDate":parameter}

headers = {
	"X-RapidAPI-Key": "f7c8fc8c64msh5fe2cb8870ad258p1c59eejsn8daa1f794366",
	"X-RapidAPI-Host": "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

directorio_actual = os.path.abspath(os.path.dirname(__file__))
directory = 'getMLBGamesForDate'
ruta = os.path.join(directorio_actual, directory)
if not os.path.exists(ruta):
    os.makedirs(ruta)
nombre_archivo = parameter +'.json'
ruta_complete = os.path.join(ruta, nombre_archivo)

with open(ruta_complete, 'w') as archivo:
        json.dump(response.json(), archivo)