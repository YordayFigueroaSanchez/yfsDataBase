import requests
import os
import datetime
import json

param = "717189"; 

url = "https://baseball4.p.rapidapi.com/game-boxscore"

querystring = {"gamePk":param}

headers = {
	"X-RapidAPI-Key": "f7c8fc8c64msh5fe2cb8870ad258p1c59eejsn8daa1f794366",
	"X-RapidAPI-Host": "baseball4.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# Obtener la fecha actual
fecha_actual = datetime.datetime.now()
# Formatear la fecha en AAAAMMDD
fecha_formateada = fecha_actual.strftime("%Y%m%d")
# Formatear la hora en HHMM
hora_formateada = fecha_actual.strftime("%H%M")
# Combinar la fecha y la hora con _
fecha_resultante = fecha_formateada + "_" + hora_formateada
# fecha_resultante = '20230723_2026'
# Obtener la ruta absoluta del directorio actual
directorio_actual = os.path.abspath(os.path.dirname(__file__))
directory = 'game-boxscore'
ruta = os.path.join(directorio_actual, directory)
# Comprobar si el directorio existe, si no, crearlo
if not os.path.exists(ruta):
    os.makedirs(ruta)
# Nombre del archivo que deseas guardar
nombre_archivo = param +'.json'
ruta_complete = os.path.join(ruta, nombre_archivo)

with open(ruta_complete, 'w') as archivo:
        json.dump(response.json(), archivo)