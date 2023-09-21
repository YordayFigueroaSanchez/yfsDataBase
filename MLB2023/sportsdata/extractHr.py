import requests
import os
import json
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
mes = 7
dias_mes = obtener_dias_mes(anio, mes)

day = "2023-07-01"
parameterGame = "69416"


directorio_actual = os.path.abspath(os.path.dirname(__file__))

directoryBoxScore = 'boxScore'
rutaBoxScore = os.path.join(directorio_actual, directoryBoxScore)

nombre_archivo = day + "_" + parameterGame +'.json'
rutaBoxScoreComplete = os.path.join(rutaBoxScore, nombre_archivo)

with open(rutaBoxScoreComplete, "r") as file:
        datos = json.load(file)
        players = datos["PlayerGames"]
        for player in players:
            if player["HomeRuns"] != 0.0 :
                print(player["PlayerID"])
                print(player["Name"])
                print(player["Position"])
                print(player["HomeRuns"])
