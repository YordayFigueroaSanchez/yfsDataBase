class Auto:
    def __init__(self, color, modelo):
        self.color = color
        self.modelo = modelo

    def __repr__(self):
        return f"Auto(color={self.color}, modelo={self.modelo})"

# Definimos una lista de objetos Auto
autos = [
    Auto("Rojo", "A"),
    Auto("Azul", "B"),
    Auto("Verde", "C"),
    Auto("Rojo", "D"),
    Auto("Azul", "E"),
]

# Definimos la función de comparación
def comparar_autos(auto):
    return (auto.color)

# Ordenamos la lista de autos usando la función de comparación
autos_ordenados = sorted(autos, key=comparar_autos)

# Imprimimos la lista ordenada
for auto in autos_ordenados:
    print(auto)
