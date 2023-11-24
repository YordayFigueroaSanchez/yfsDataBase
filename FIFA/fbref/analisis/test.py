import os
import json

# print('test')
# extension = '.json'
# # Obtén la ruta al directorio 'data' desde el directorio 'code'
# ruta = os.path.join(os.path.dirname(__file__), '..', '1938', 'game', '20231120_1207', 'json')
# # Ahora puedes acceder a los archivos en el directorio 'data'
# archivos_json = [archivo for archivo in os.listdir(ruta) if archivo.endswith(extension)]
# # archivo_datos = os.path.join(ruta_data, 'archivo_de_datos.txt')
# for archivo in archivos_json:
#     print(archivo)

# def arreglo_y_conjunto():
#     arreglo = [1, 2, 3, 4, 5]
#     conjunto = set(arreglo)
#     return arreglo, conjunto
# mi_arreglo, mi_conjunto = arreglo_y_conjunto()
# print("Arreglo:", mi_arreglo)
# print("Conjunto:", mi_conjunto)

# para inizializar el tema de colores y asociar nombres, se inicializa  con cinco colores que son los que se usan hasta el momento
print("data color used")
class MiClase:
    def __init__(self, color_id):
        self.contador = 0
        self.lista_nombres = []
        self.color_id = color_id

    def agregar_nombre(self, nombre):
        self.lista_nombres.append(nombre)
        self.contador += 1

    def obtener_contador(self):
        return self.contador

    def obtener_nombres(self):
        return self.lista_nombres

    def obtener_color_id(self):
        return self.color_id
import pickle

class OtraClase:
    def __init__(self):
        self.lista_mi_clase = []

    def agregar_mi_clase(self, mi_clase_obj):
        self.lista_mi_clase.append(mi_clase_obj)

    def obtener_lista_mi_clase(self):
        return self.lista_mi_clase
    
    def obtener_id_menor_contador(self, nombre):
        if not self.lista_mi_clase:
            return None  # Retorna None si la lista está vacía
        # Encuentra el objeto MiClase con el menor contador
        menor_contador_obj = min(self.lista_mi_clase, key=lambda x: x.obtener_contador())
        # Retorna el índice de ese objeto en la lista
        menor_contador_obj.agregar_nombre(nombre)
        return menor_contador_obj.obtener_color_id()

    def obtener_color_id_por_nombre(self, nombre):
        for mi_clase_obj in self.lista_mi_clase:
            if nombre in mi_clase_obj.obtener_nombres():
                return mi_clase_obj.obtener_color_id()
        return self.obtener_id_menor_contador(nombre)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(self, archivo)

    @classmethod
    def cargar_desde_archivo(cls, nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            return pickle.load(archivo)

# Uso de las clases
# mi_objeto_1 = MiClase(color_id='#0086F9')
# mi_objeto_1.agregar_nombre('A')
# mi_objeto_1.agregar_nombre('B')
# mi_objeto_2 = MiClase(color_id='#00FF00')
# mi_objeto_2.agregar_nombre('X')
otro_objeto = OtraClase()
# otro_objeto.agregar_mi_clase(mi_objeto_1)
# otro_objeto.agregar_mi_clase(mi_objeto_2)

otro_objeto.agregar_mi_clase(MiClase(color_id='#0086F9'))
otro_objeto.agregar_mi_clase(MiClase(color_id='#FF4131'))
otro_objeto.agregar_mi_clase(MiClase(color_id='#FEBD00'))
otro_objeto.agregar_mi_clase(MiClase(color_id='#c71cda'))
otro_objeto.agregar_mi_clase(MiClase(color_id='#15004b'))
# Guardar en archivo
otro_objeto.guardar_en_archivo('estado_otra_clase.pkl')
# Cargar desde archivo
otra_clase_recuperada = OtraClase.cargar_desde_archivo('estado_otra_clase.pkl')

print("Lista de MiClase en OtraClase:", otra_clase_recuperada.obtener_lista_mi_clase())

# print("Menor id :", otra_clase_recuperada.obtener_color_id_por_nombre('D'))


