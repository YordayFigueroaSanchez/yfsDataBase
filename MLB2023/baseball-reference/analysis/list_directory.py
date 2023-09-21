import os
import json
import csv
import pandas as pd

# Obtener la ruta absoluta del directorio actual
directorio_actual = os.path.abspath(os.path.dirname(__file__))
directory = 'games_month_all'
extension = '.json'
# Crear la ruta completa del directorio
ruta = os.path.join(directorio_actual, directory)
ruta_csv = os.path.join(directorio_actual, directory + '.csv')
archivos_json = [archivo for archivo in os.listdir(ruta) if archivo.endswith(extension)]

# Datos que deseas guardar en el archivo CSV
data_csv = []
data_csv.append(["Date", "Name", "HR"])
data_date   = []
data_name   = []
data_hr     = []
table       = {}
for archivo in archivos_json:
    print(archivo)
    ruta_completa = os.path.join(ruta, archivo)  # Obtiene la ruta completa del archivo
    with open(ruta_completa, 'r', encoding="utf-8") as archivo_json:
        datos = json.load(archivo_json)  # Carga los datos JSON del archivo en un diccionario

    # Aquí puedes trabajar con los datos como lo harías con un diccionario de Python
    # print(datos["home_team"]["name"])
    for batter in datos["home_team"]["batters"]:
        if batter['HR'] != "":
            # print(datos["date"])
            # print(batter['name'])
            # print(batter['HR'])
            data_csv.append([datos["date"], batter['name'], batter['HR']])
            data_date.append(datos["date"])
            data_name.append(batter["name"])
            data_hr.append(batter["HR"])
            # Verificar si la clave '20230401' existe en el diccionario table
            fecha = datos["date"]
            nombre_bateador = batter["name"]
            hr = batter["HR"]
            if fecha in table:
                # Verificar si la clave 'nombre_bateador' existe en el diccionario anidado
                if nombre_bateador in table[fecha]:
                    # La clave 'nombre_bateador' existe, actualiza el valor
                    table[fecha][nombre_bateador] = str(int(table[fecha][nombre_bateador]) + int(hr))
                else:
                    # La clave 'nombre_bateador' no existe, crea una nueva entrada
                    table[fecha][nombre_bateador] = hr
            else:
                # La clave 'fecha' no existe, crea una nueva entrada con el diccionario anidado
                table[fecha] = {nombre_bateador: hr}

    # print(datos["away_team"]["name"])
    for batter in datos["away_team"]["batters"]:
        if batter['HR'] != "":
            # print(datos["date"])
            # print(batter['name'])
            # print(batter['HR'])
            data_csv.append([datos["date"], batter['name'], batter['HR']])
            data_date.append(datos["date"])
            data_name.append(batter["name"])
            data_hr.append(batter["HR"])
            fecha = datos["date"]
            nombre_bateador = batter["name"]
            hr = batter["HR"]
            if fecha in table:
                # Verificar si la clave 'nombre_bateador' existe en el diccionario anidado
                if nombre_bateador in table[fecha]:
                    # La clave 'nombre_bateador' existe, actualiza el valor
                    table[fecha][nombre_bateador] = str(int(table[fecha][nombre_bateador]) + int(hr))
                else:
                    # La clave 'nombre_bateador' no existe, crea una nueva entrada
                    table[fecha][nombre_bateador] = hr
            else:
                # La clave 'fecha' no existe, crea una nueva entrada con el diccionario anidado
                table[fecha] = {nombre_bateador: hr}


# Abre el archivo CSV en modo escritura
with open(ruta_csv, mode='w', newline='', encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Escribe los datos en el archivo CSV
    for fila in data_csv:
        escritor_csv.writerow(fila)

# Crear un DataFrame desde los datos CSV originales
data = {
    "Date": data_date,
    "Name": data_name,
    "HR": data_hr
}
# print(data_hr)

# TEST 01
# df = pd.DataFrame(data)
# # Realizar un pivot para obtener un DataFrame con una columna para cada jugador
# # pivot_df = df.pivot(index="Date", columns="Name", values="HR")
# pivot_df = df.pivot_table(index="Date", columns="Name", values="HR", aggfunc='sum', fill_value=0)
# # Rellenar los valores NaN con 0 (si un jugador no tiene HR en una fecha, se establecerá como 0)
# pivot_df.fillna(0, inplace=True)
# # Guardar el DataFrame pivot en un nuevo archivo CSV
# ruta_csv = os.path.join(directorio_actual, directory + '_pivot.csv')
# pivot_df.to_csv(ruta_csv)

# TEST 02
print(table)
# Obtener la lista de nombres de bateadores únicos
ruta_csv = os.path.join(directorio_actual, directory + '_pivot.csv')
nombres_bateadores = set()
for datos_bateadores in table.values():
    nombres_bateadores.update(datos_bateadores.keys())

# Abrir el archivo CSV en modo de escritura
with open(ruta_csv, 'w', newline='', encoding="utf-8") as csvfile:
    # Crear un objeto escritor CSV
    csv_writer = csv.writer(csvfile)
    
    # Escribir la primera fila con los encabezados (nombre de bateadores)
    encabezados = ['Fecha'] + list(nombres_bateadores)
    csv_writer.writerow(encabezados)
    
    # Iterar a través del diccionario y escribir los datos en el archivo CSV
    for fecha, datos_bateadores in table.items():
        fila = [fecha]
        for bateador in nombres_bateadores:
            fila.append(datos_bateadores.get(bateador, 0))
        csv_writer.writerow(fila)

# TEST 03
# df = pd.DataFrame(data)
# # Agrupar los datos por fecha y nombre, y sumar los valores de 'HR'
# df = df.groupby(['Date', 'Name'])['HR'].sum().reset_index()
# # Realizar un pivot después de eliminar los duplicados
# pivot_df = df.pivot(index="Date", columns="Name", values="HR")
# pivot_df.fillna(0, inplace=True)
# ruta_csv = os.path.join(directorio_actual, directory + '_pivot.csv')
# pivot_df.to_csv(ruta_csv)

