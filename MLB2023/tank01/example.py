import os

# Obtener el directorio del archivo actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Nombre del archivo que deseas guardar (puedes cambiar el nombre y extensión)
nombre_archivo = "archivo_guardado.txt"

# Combinar el directorio actual con el nombre del archivo para obtener la ruta completa
ruta_archivo_guardado = os.path.join(directorio_actual, nombre_archivo)

# Aquí puedes realizar las operaciones para guardar el archivo en la ruta especificada
# Por ejemplo, si deseas guardar un archivo de texto, podrías hacer lo siguiente:
with open(ruta_archivo_guardado, 'w') as archivo:
    archivo.write("Contenido del archivo que deseas guardar")

print(f"El archivo ha sido guardado en: {ruta_archivo_guardado}")
