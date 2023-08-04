from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date
import time
import json


from team import Team
from game import Game
from player import Player
from stats import Stats

def extractNameFull( element):
  #url player id,  
  div_a_span_element_names = element.select('div > a > span > span', class_=lambda c: c and c.startswith("GameBoxscoreTablePlayer_gbpNameFull"))
  # print(div_a_span_element_names)
  # div_a_span_element_shortname = element.select('div > a > span > span', class_=lambda c: c and c.startswith("GameBoxscoreTablePlayer_gbpNameShort"))
  div_a_figure_image = element.select('div > a > figure > img')
  src_value = div_a_figure_image[0]['src']

  div_a = element.select('div > a')
  href_value = div_a[0]['href']

  div_span = element.select('div > span')
  status_value = div_span[0].text

  return {  'full_name': div_a_span_element_names[0].text,
            'short_name': div_a_span_element_names[1].text, 
            'image_url': src_value,
            'url': href_value,
            'status': status_value}

def extractDescripcionNoPlay(element):
  span = element[1].select('span')
  return span[0].text

def extractStatsPlayer( element):
  minutes                   = element[1].text   # MIN (Minutes played)
  field_goals_made          = element[2].text   # FGM (Field Goals Made)
  field_goals_attempted     = element[3].text   # FGA (Field Goals Attempted)
  field_goal_percentage     = element[4].text   # FG% (Field Goal Percentage)
  three_pointers_made       = element[5].text   # 3PM (Three-Pointers Made)
  three_pointers_attempted  = element[6].text   # 3PA (Three-Pointers Attempted)
  three_point_percentage    = element[7].text   # 3P% (Three-Point Percentage)
  free_throws_made          = element[8].text   # FTM (Free Throws Made)
  free_throws_attempted     = element[9].text   # FTA (Free Throws Attempted)
  free_throw_percentage     = element[10].text  # FT% (Free Throw Percentage)
  offensive_rebounds        = element[11].text  # OREB (Offensive Rebounds)
  defensive_rebounds        = element[12].text  # DREB (Defensive Rebounds)
  total_rebounds            = element[13].text  # REB (Total Rebounds)
  assists                   = element[14].text  # AST (Assists)
  steals                    = element[15].text  # STL (Steals)
  blocks                    = element[16].text  # BLK (Blocks)
  turnovers                 = element[17].text  # TO (Turnovers)
  personal_fouls            = element[18].text  # PF (Personal Fouls)
  points                    = element[19].text  # PTS (Points)
  plus_minus                = element[20].text  # +/- (Plus/Minus)
  # print('paso...')
  return minutes,  field_goals_made, field_goals_attempted, field_goal_percentage, three_pointers_made, three_pointers_attempted, three_point_percentage, free_throws_made, free_throws_attempted, free_throw_percentage, offensive_rebounds, defensive_rebounds, total_rebounds, assists,  steals, blocks, turnovers,  personal_fouls, points, plus_minus


 #Ruta del driver

ubicacion = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver"
driver = webdriver.Chrome(ubicacion)

#url de la data
home_link = "https://www.nba.com/game/phx-vs-den-0042200225/box-score#box-score"

driver.get(home_link)

page = BeautifulSoup(driver.page_source,'html.parser')

#crear team away and home
home_team = Team("Home Team")
away_team = Team("Away Team")

elemntsTBODY = page.findAll("tbody", class_=lambda c: c and c.startswith("StatsTableBody_tbody"))
type_team = 0
for elemntTBODY in elemntsTBODY:
  elementsTR = elemntTBODY.find_all("tr")
  count = 0
  try:
    # Bloque de código que podría generar una excepción
    for elemenTR in elementsTR:
      print(type_team)
      # print('count')
      # print(count)
      count = count + 1
      elementsTD = elemenTR.find_all("td")
      if count < len(elementsTR):
        #
        print(len(elementsTD))
        #extraer nombre del jugador
        player_data = extractNameFull(elementsTD[0])
        # print(player_data)

        #extraer stats puede tener data o solo descripcion por la que no participo en el juego
        if len(elementsTD) > 2:
          (minutes,  field_goals_made, field_goals_attempted, 
           field_goal_percentage, three_pointers_made, three_pointers_attempted, 
           three_point_percentage, free_throws_made, free_throws_attempted, 
           free_throw_percentage, offensive_rebounds, defensive_rebounds, 
           total_rebounds, assists,  steals, blocks, turnovers,  
           personal_fouls, points, plus_minus) = extractStatsPlayer(elementsTD)
          stats_player = Stats()  
          stats_player.minutes = minutes
          stats_player.field_goals_made = field_goals_made
          stats_player.field_goals_attempted = field_goals_attempted
          stats_player.field_goal_percentage = field_goal_percentage
          stats_player.three_pointers_made = three_pointers_made
          stats_player.three_pointers_attempted = three_pointers_attempted
          stats_player.three_point_percentage = three_point_percentage
          stats_player.free_throws_made = free_throws_made
          stats_player.free_throws_attempted =free_throws_attempted
          stats_player.free_throw_percentage = free_throw_percentage
          stats_player.offensive_rebounds = offensive_rebounds
          stats_player.defensive_rebounds = defensive_rebounds
          stats_player.total_rebounds = total_rebounds
          stats_player.assists = assists
          stats_player.steals = steals
          stats_player.blocks = blocks
          stats_player.turnovers = turnovers
          stats_player.personal_fouls = personal_fouls
          stats_player.points = points
          stats_player.plus_minus = plus_minus

          # print('player')
        else:
          player_data['status'] = extractDescripcionNoPlay(elementsTD)
          # print(player_data)
        player = Player(player_data['full_name'], player_data['short_name'], player_data['image_url'], player_data['url'], player_data['status'])
        # player = Player('abc', 'abc', 'abc', 'abc', 'abc')
        player.stats = stats_player
        print(type_team)
        if type_team < 50:
          print('away')
          away_team.add_player(player)
        else:
          print('home')
          home_team.add_player(player)
      else:
        print("data of team")
        (minutes,  field_goals_made, field_goals_attempted, 
           field_goal_percentage, three_pointers_made, three_pointers_attempted, 
           three_point_percentage, free_throws_made, free_throws_attempted, 
           free_throw_percentage, offensive_rebounds, defensive_rebounds, 
           total_rebounds, assists,  steals, blocks, turnovers,  
           personal_fouls, points, plus_minus) = extractStatsPlayer(elementsTD)
        stats_team = Stats()
        #stats_team.minutes = minutes
        stats_team.field_goals_made = field_goals_made
        stats_team.field_goals_attempted = field_goals_attempted
        stats_team.field_goal_percentage = field_goal_percentage
        stats_team.three_pointers_made = three_pointers_made
        stats_team.three_pointers_attempted = three_pointers_attempted
        stats_team.three_point_percentage = three_point_percentage
        stats_team.free_throws_made = free_throws_made
        stats_team.free_throws_attempted =free_throws_attempted
        stats_team.free_throw_percentage = free_throw_percentage
        stats_team.offensive_rebounds = offensive_rebounds
        stats_team.defensive_rebounds = defensive_rebounds
        stats_team.total_rebounds = total_rebounds
        stats_team.assists = assists
        stats_team.steals = steals
        stats_team.blocks = blocks
        stats_team.turnovers = turnovers
        stats_team.personal_fouls = personal_fouls
        stats_team.points = points
        stats_team.plus_minus = plus_minus  
        print(type_team)
        if type_team < 50:
          away_team.stats = stats_team
        else:
          home_team.stats = stats_team
  except Exception as e:
    print("Ha ocurrido un error:", str(e))

  finally:
    type_team = 100
    print("Este bloque de código siempre se ejecuta.")
    print(type_team)
  
# Create a game and assign teams
game = Game(home_team, away_team)

# Convert game structure to dictionary
game_data = game.to_dict()

# Save game structure to JSON file
with open('game_data.json', 'w') as file:
  json.dump(game_data, file, indent=4)


