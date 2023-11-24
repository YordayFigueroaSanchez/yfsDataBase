import pickle

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

class OtraClase:
    def __init__(self):
        self.lista_mi_clase = []

    def agregar_mi_clase(self, mi_clase_obj):
        self.lista_mi_clase.append(mi_clase_obj)

    def obtener_lista_mi_clase(self):
        return self.lista_mi_clase
    
    def obtener_id_menor_contador(self, nombre):
        if not self.lista_mi_clase:
            return None
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