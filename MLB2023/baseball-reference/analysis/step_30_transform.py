import pandas as pd

# Crear un DataFrame desde los datos CSV originales
data = {
    "Date": ["20230330"] * 12,
    "Name": [
        "Adley Rutschman", "Ramón Urías", "Spencer Steer", "Oneil Cruz",
        "Yordan Alvarez", "Yasmani Grandal", "James Outman", "Garrett Cooper",
        "Aaron Judge", "Gleyber Torres", "C.J. Cron", "Elehuris Montero"
    ],
    "HR": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
}

df = pd.DataFrame(data)

# Realizar un pivot para obtener un DataFrame con una columna para cada jugador
pivot_df = df.pivot(index="Date", columns="Name", values="HR")

# Rellenar los valores NaN con 0 (si un jugador no tiene HR en una fecha, se establecerá como 0)
pivot_df.fillna(0, inplace=True)

# Guardar el DataFrame pivot en un nuevo archivo CSV
pivot_df.to_csv("datos_pivot.csv")

print(pivot_df)
