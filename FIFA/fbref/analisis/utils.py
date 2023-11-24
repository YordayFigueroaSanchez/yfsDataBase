import os
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