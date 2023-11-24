import os

# print('test')
# extension = '.json'
# # Obtén la ruta al directorio 'data' desde el directorio 'code'
# ruta = os.path.join(os.path.dirname(__file__), '..', '1938', 'game', '20231120_1207', 'json')
# # Ahora puedes acceder a los archivos en el directorio 'data'
# archivos_json = [archivo for archivo in os.listdir(ruta) if archivo.endswith(extension)]
# # archivo_datos = os.path.join(ruta_data, 'archivo_de_datos.txt')
# for archivo in archivos_json:
#     print(archivo)

def arreglo_y_conjunto():
    # Crear un arreglo (lista)
    arreglo = [1, 2, 3, 4, 5]
    # Crear un conjunto a partir del arreglo
    conjunto = set(arreglo)
    # Retornar tanto el arreglo como el conjunto
    return arreglo, conjunto
# Llamamos a la función
mi_arreglo, mi_conjunto = arreglo_y_conjunto()
# Mostramos los resultados
print("Arreglo:", mi_arreglo)
print("Conjunto:", mi_conjunto)
