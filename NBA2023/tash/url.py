from urllib.parse import urlparse
from team import Team
from game import Game
from player import Player
from stats import Stats
import json

url = "https://www.nba.com/game/phx-vs-den-0042200225/box-score#box-score"

# Parsear la URL
parsed_url = urlparse(url)

# Obtener la ruta
path = parsed_url.path

# Dividir la ruta por "/"
segments = path.split("/")

# Eliminar segmentos vacíos
segments = [segment for segment in segments if segment]
# print("Segmentos de la ruta:", segments)

#folder
folder = segments[1]
print(folder)

# Dividir la folder por "-"
segments_folder = folder.split("-")
# Eliminar segmentos vacíos
segments_folder = [segment_folder for segment_folder in segments_folder if segment_folder]
print(segments_folder)
segments_folder_team_away = segments_folder[0]
print(segments_folder_team_away)
segments_folder_team_home = segments_folder[2]
print(segments_folder_team_home)

#crear team away and home
home_team = Team(segments_folder_team_home)
away_team = Team(segments_folder_team_away)

# Create a game and assign teams
game = Game(home_team, away_team)

# Convert game structure to dictionary
game_data = game.to_dict()

# Save game structure to JSON file
with open(folder +'.json', 'w') as file:
  json.dump(game_data, file, indent=4)


