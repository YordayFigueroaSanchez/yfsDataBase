import os
import json
from datetime import datetime

def dateInYYYYMMDD_MMSS():
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    # Formatear la fecha en AAAAMMDD
    fecha_formateada = fecha_actual.strftime("%Y%m%d")
    # Formatear la hora en HHMM
    hora_formateada = fecha_actual.strftime("%H%M")
    # Combinar la fecha y la hora con _
    fecha_resultante = fecha_formateada + "_" + hora_formateada
    return fecha_resultante
def listar_archivos_json(rutas):
    archivos_json = []
    for ruta in rutas:
        print(ruta)
        # archivos_json.extend([archivo for archivo in os.listdir(ruta) if archivo.endswith(".json")])
        archivos_json.extend([os.path.join(ruta, archivo) for archivo in os.listdir(ruta) if archivo.endswith(".json")])
    return archivos_json
def data_extract(archivos_json):
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
    return data_csv, table