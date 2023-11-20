from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import os
from urllib.parse import urlparse
from funciones import lastStrInUrlBeforeDot
from funciones import dateInYYYYMMDD_MMSS
from funciones import dateInYYYYMMDD
from funciones import dateInHHMM
from funciones import createDirectory
from funciones import createDirectoryAndSubdirectory
from funciones import createDirectoryInPath
from funciones import extract_scorebox_meta
from funciones import extract_players
from funciones import extract_goals
from funciones import saveInfoComplete
from classes import FifaWorldCupGame
from classes import FifaWorldCupTeam
from classes import FifaWorldCupTeamGoalkeeper
from classes import InfoComplete


# Especifica la ruta al ejecutable de ChromeDriver
ruta_chrome_driver = 'C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/chromedriver.exe'  # Sustituye por tu ruta real
# Crea un objeto Service con la ruta del ejecutable
servicio_chrome = Service(ruta_chrome_driver)
# Crea una instancia de Chrome WebDriver utilizando el objeto Service
driver = webdriver.Chrome(service=servicio_chrome)
# Ahora puedes utilizar 'driver' para tus operaciones de Selenium como antes

# ubicacion           = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver"
# driver              = webdriver.Chrome(ubicacion)
link_base           = "https://fbref.com"
list_game           = [
'/en/matches/89e6fe61/Switzerland-Germany-June-4-1938-FIFA-World-Cup',
'/en/matches/7aa6e624/Cuba-Romania-June-5-1938-FIFA-World-Cup',
'/en/matches/9942f6ed/Hungary-Dutch-East-Indies-June-5-1938-FIFA-World-Cup',
'/en/matches/b33c6206/France-Belgium-June-5-1938-FIFA-World-Cup',
'/en/matches/542933dd/Italy-Norway-June-5-1938-FIFA-World-Cup',
'/en/matches/f41dea83/Brazil-Poland-June-5-1938-FIFA-World-Cup',
'/en/matches/97e2cad4/Czechoslovakia-Netherlands-June-5-1938-FIFA-World-Cup',
'/en/matches/68015527/Switzerland-Germany-June-9-1938-FIFA-World-Cup',
'/en/matches/cbea1ca5/Cuba-Romania-June-9-1938-FIFA-World-Cup',
'/en/matches/10c7d3fe/Italy-France-June-12-1938-FIFA-World-Cup',
'/en/matches/f9b42643/Sweden-Cuba-June-12-1938-FIFA-World-Cup',
'/en/matches/bb19998e/Brazil-Czechoslovakia-June-12-1938-FIFA-World-Cup',
'/en/matches/790141f6/Hungary-Switzerland-June-12-1938-FIFA-World-Cup',
'/en/matches/b9e80723/Brazil-Czechoslovakia-June-14-1938-FIFA-World-Cup',
'/en/matches/9a8bfc05/Hungary-Sweden-June-16-1938-FIFA-World-Cup',
'/en/matches/d6c5c22e/Italy-Brazil-June-16-1938-FIFA-World-Cup',
'/en/matches/8bf431de/Brazil-Sweden-June-19-1938-FIFA-World-Cup',
'/en/matches/0f66a5be/Italy-Hungary-June-19-1938-FIFA-World-Cup',
]
day                 = dateInYYYYMMDD()

fecha_resultante    = dateInYYYYMMDD_MMSS()
fecha_hhmm          =  dateInHHMM()                                               
ruta_game           = createDirectoryAndSubdirectory('game',fecha_resultante)
ruta_game_txt       = createDirectoryInPath(ruta_game,'txt')
ruta_game_json      = createDirectoryInPath(ruta_game,'json')

for current_game in list_game:
    print('-->' + current_game)
    allInfo = []

    link_game = current_game

    game_name = lastStrInUrlBeforeDot(link_game)
    ruta_game = createDirectory('game')

    link_complete = link_base + link_game
    driver.get(link_complete)
    page = BeautifulSoup(driver.page_source,'html.parser')

    # div = page.find('div', class_='site_announcement')
    # print(div)

    # fifaWorldCupGoal = FifaWorldCupGoal()
    # fifaWorldCupGoal.minute = "22"
    # fifaWorldCupGoal.result = "2-2"

    fifaWorldCupGame = FifaWorldCupGame()
    fifaWorldCupGame.game_number = game_name
    # fifaWorldCupGame.date = "20231103"
    # fifaWorldCupGame.attendance = "1234"
    # fifaWorldCupTeamPlayer = FifaWorldCupTeamPlayer()
    # fifaWorldCupTeamPlayer.name = "ssdf"
    # fifaWorldCupTeamPlayer.add_goal(fifaWorldCupGoal)
    fifaWorldCupTeamGoalkeeper = FifaWorldCupTeamGoalkeeper()
    fifaWorldCupTeamGoalkeeper.name = "dgfhgj"
    # fifaWorldCupGame.home_team.add_player(fifaWorldCupTeamPlayer)
    fifaWorldCupGame.home_team.add_goalkeeper(fifaWorldCupTeamGoalkeeper)
    fifaWorldCupGame.away_team = FifaWorldCupTeam()
    # fifaWorldCupGame.away_team.add_player(fifaWorldCupTeamPlayer)
    fifaWorldCupGame.away_team.add_goalkeeper(fifaWorldCupTeamGoalkeeper)

    # scorebox_meta
    # print(page)
    scorebox_meta = extract_scorebox_meta(page,fifaWorldCupGame)
    scorebox_meta_complete = InfoComplete()
    scorebox_meta_complete.name = 'Scorebox Meta'
    scorebox_meta_complete.data = scorebox_meta
    allInfo.append(scorebox_meta_complete)

    # player stats team 1
    print('Home player')
    home_players = extract_players(page,fifaWorldCupGame,'home')
    home_player_complete = InfoComplete()
    home_player_complete.name = 'Home player'
    home_player_complete.data = home_players
    allInfo.append(home_player_complete)

    # away batting
    print('Away player')
    away_players = extract_players(page,fifaWorldCupGame,'away')
    away_player_complete = InfoComplete()
    away_player_complete.name = 'Away player'
    away_player_complete.data = away_players
    allInfo.append(away_player_complete)

    # procesing goals
    procesing_goals = extract_goals(page,fifaWorldCupGame)

    
    time.sleep(10)

    nombre_archivo_game     = fifaWorldCupGame.date +'_'+ game_name                
    ruta_archivo_game_txt   = os.path.join(ruta_game_txt, nombre_archivo_game +'.txt')          
    ruta_archivo_game_json  = os.path.join(ruta_game_json, nombre_archivo_game +'.json')
    # saveArrayOfArray(ruta_archivo_game_txt,linescore_wrap,home_batting)
    saveInfoComplete(ruta_archivo_game_txt,allInfo)
    fifaWorldCupGame.save_to_json(ruta_archivo_game_json)

    print('<--' + current_game)

