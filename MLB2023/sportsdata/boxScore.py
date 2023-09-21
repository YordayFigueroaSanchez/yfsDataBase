import requests
import os
import json

parameterGame = "69795"
url = "https://api.sportsdata.io/v3/mlb/stats/json/BoxScore/"+ parameterGame +"?key=87172a8552914404994259782b1d8551"

response = requests.get(url)

print(response.json())

directorio_actual = os.path.abspath(os.path.dirname(__file__))
directory = 'boxScore'
ruta = os.path.join(directorio_actual, directory)
if not os.path.exists(ruta):
    os.makedirs(ruta)
nombre_archivo = parameterGame +'.json'
ruta_complete = os.path.join(ruta, nombre_archivo)

with open(ruta_complete, 'w') as archivo:
        json.dump(response.json(), archivo)