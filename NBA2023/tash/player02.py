import requests
from bs4 import BeautifulSoup

# Realizar la solicitud GET a la página web
url = "https://www.nba.com/game/phi-vs-bos-0042200215/box-score#box-score"  # Reemplaza con la URL de la página web que deseas analizar
response = requests.get(url)

# Parsear el contenido HTML de la página web
soup = BeautifulSoup(response.content, "html.parser")

# Seleccionar todos los elementos 'tr'
trs = soup.find_all()
print(len(trs))
# Iterar sobre los elementos 'tr' encontrados
with open("resultado.txt", "w") as archivo:
    for tr in trs:
        # Aquí puedes realizar operaciones o acceder a los datos dentro de cada elemento 'tr'
        # Por ejemplo, para obtener el texto dentro de cada celda 'td' dentro del elemento 'tr':
        #tds = tr.find_all()
        #for td in tds:
        print(tr)
        #archivo.write(tr + "\n")

# Resto de tu código

