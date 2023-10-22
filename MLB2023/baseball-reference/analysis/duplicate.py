data_csv = [["date", "name", "category", "value"],
            ["2023-10-16", "John Doe", "Groceries", 50],
            ["2023-10-15", "Jane Doe", "Entertainment", 30],
            ["2023-10-15", "Jane Doe", "Entertainment", 10],
            ["2023-10-16", "John Doe", "Groceries", 40],
            ["2023-10-15", "Jane Doe", "Entertainment", 20]]

def remove_duplicates_with_min_value(data_csv):
    duplicates = {}
    for row in data_csv[1:]:
        key = (row[0], row[1])
        if key in duplicates:
            if row[3] > duplicates[key][3]:
                duplicates[key] = row
        else:
            duplicates[key] = row

    return [data_csv[0]] + list(duplicates.values())

# Eliminar duplicados con el menor valor de 'value'
data_csv_without_duplicates = remove_duplicates_with_min_value(data_csv)

# Mostrar el resultado
for row in data_csv_without_duplicates:
    print(row)
