data_csv = [["date", "name", "value"],
            ["2023-10-16", "Ejemplo1", 100],
            ["2023-10-16", "Ejemplo2", 90],
            ["2023-10-17", "Ejemplo2", 150],
            ["2023-10-18", "Ejemplo1", 200],
            ["2023-10-19", "Ejemplo3", 120]]

# Crear un diccionario para almacenar los valores de las columnas
data_dict = {}
for row in data_csv[1:]:
    date, name, value = row
    if date not in data_dict:
        data_dict[date] = {name : value}
    else :
        data_dict[date][name] = value

# Imprimir el diccionario resultante
print(data_dict)
