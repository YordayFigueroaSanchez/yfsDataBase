from datetime import datetime

def transform_date(date_str):
    # Definimos los formatos de entrada y salida de la fecha
    input_format = "%a, %b %d, %Y"
    output_format = "%d/%m/%Y"

    try:
        # Convertimos la cadena a un objeto datetime
        date_obj = datetime.strptime(date_str, input_format)
        # Formateamos la fecha como una cadena en el formato deseado
        transformed_date = date_obj.strftime(output_format)
        return transformed_date
    except ValueError:
        return date_str

# Ejemplo de uso
date_str = "Wed, Oct 26, 2022"
transformed_date = transform_date(date_str)
print(transformed_date)
