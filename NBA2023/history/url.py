from urllib.parse import urlparse
from team import Team
from game import Game
from player import Player
from stats import Stats
import json

url = "https://www.nba.com/stats/player/2544"

# Parsear la URL
parsed_url = urlparse(url)

# Obtener la ruta
path = parsed_url.path

# Dividir la ruta por "/"
segments = path.split("/")

# Eliminar segmentos vacíos
segments = [segment for segment in segments if segment]
# print("Segmentos de la ruta:", segments)

#id player
idPlayer = segments[2]
print(idPlayer)
