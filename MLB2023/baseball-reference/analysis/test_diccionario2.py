import csv

# Tu diccionario de datos
table = {
    '20230401': {
        'Bateador1': 3,
        'Bateador2': 1,
        'Bateador3': 2
    },
    '20230402': {
        'Bateador1': 2,
        'Bateador4': 0,
        'Bateador5': 1
    }
}

# Nombre del archivo CSV en el que deseas guardar los datos
archivo_csv = 'datos_bateadores.csv'

# Obtener la lista de nombres de bateadores únicos
nombres_bateadores = set()
for datos_bateadores in table.values():
    nombres_bateadores.update(datos_bateadores.keys())

# Abrir el archivo CSV en modo de escritura
with open(archivo_csv, 'w', newline='') as csvfile:
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

print(f"Los datos se han guardado en '{archivo_csv}'.")
