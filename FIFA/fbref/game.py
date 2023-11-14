from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import json
import os
import datetime
from urllib.parse import urlparse
import csv
import re
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
from classes import FifaWorldCupTeamPlayer
from classes import FifaWorldCupTeamGoalkeeper
from classes import FifaWorldCupGoal
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
'/en/matches/c54abca0/United-States-Belgium-July-13-1930-FIFA-World-Cup',
'/en/matches/f24db046/France-Mexico-July-13-1930-FIFA-World-Cup',
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

    fifaWorldCupGoal = FifaWorldCupGoal()
    fifaWorldCupGoal.minute = "22"
    fifaWorldCupGoal.result = "2-2"

    fifaWorldCupGame = FifaWorldCupGame()
    fifaWorldCupGame.game_number = game_name
    fifaWorldCupGame.date = "20231103"
    fifaWorldCupGame.attendance = "1234"
    fifaWorldCupTeamPlayer = FifaWorldCupTeamPlayer()
    fifaWorldCupTeamPlayer.name = "ssdf"
    fifaWorldCupTeamPlayer.add_goal(fifaWorldCupGoal)
    fifaWorldCupTeamGoalkeeper = FifaWorldCupTeamGoalkeeper()
    fifaWorldCupTeamGoalkeeper.name = "dgfhgj"
    # fifaWorldCupGame.home_team.add_player(fifaWorldCupTeamPlayer)
    fifaWorldCupGame.home_team.add_goalkeeper(fifaWorldCupTeamGoalkeeper)
    fifaWorldCupGame.away_team = FifaWorldCupTeam()
    # fifaWorldCupGame.away_team.add_player(fifaWorldCupTeamPlayer)
    fifaWorldCupGame.away_team.add_goalkeeper(fifaWorldCupTeamGoalkeeper)

    # scorebox_meta
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

    # linescore
    # linescore_wrap = extract_linescore_wrap(page,fifaWorldCupGame)
    # linescore_wrap_complete = InfoComplete()
    # linescore_wrap_complete.name = 'Boxscore'
    # linescore_wrap_complete.data = linescore_wrap
    # allInfo.append(linescore_wrap_complete)

    # home batting
    # print('home player')
    # home_batting = extract_batting(page,fifaWorldCupGame,'home')
    # home_batting_complete = InfoComplete()
    # home_batting_complete.name = 'Batting home'
    # home_batting_complete.data = home_batting
    # allInfo.append(home_batting_complete)

    # away batting
    print('Away player')
    away_players = extract_players(page,fifaWorldCupGame,'away')
    away_player_complete = InfoComplete()
    away_player_complete.name = 'Away player'
    away_player_complete.data = away_players
    allInfo.append(away_player_complete)

    # procesing goals
    procesing_goals = extract_goals(page,fifaWorldCupGame)


    # home pitching
    # print('home pitching')
    # home_pitching = extract_pitching(page,fifaWorldCupGame,'home')
    # home_pitching_complete = InfoComplete()
    # home_pitching_complete.name = 'Pitching home'
    # home_pitching_complete.data = home_pitching
    # allInfo.append(home_pitching_complete)

    # away pitching
    # print('away pitching')
    # away_pitching = extract_pitching(page,fifaWorldCupGame,'away')
    # away_pitching_complete = InfoComplete()
    # away_pitching_complete.name = 'Pitching away'
    # away_pitching_complete.data = away_pitching
    # allInfo.append(away_pitching_complete)

    # indiv_events
    # indiv_events = extract_indiv_events(page,fifaWorldCupGame)
    # indiv_events_complete = InfoComplete()
    # indiv_events_complete.name = 'indiv_events'
    # indiv_events_complete.data = indiv_events
    # allInfo.append(indiv_events_complete)
    
    # section_content
    # section_content = extract_section_content(page,fifaWorldCupGame)
    # section_content_complete = InfoComplete()
    # section_content_complete.name = 'section_content'
    # section_content_complete.data = section_content
    # allInfo.append(section_content_complete)

    # div_lineups
    # div_lineups = extract_div_lineups(page,fifaWorldCupGame)
    # div_lineups_complete = InfoComplete()
    # div_lineups_complete.name = 'div_lineups'
    # div_lineups_complete.data = div_lineups
    # allInfo.append(div_lineups_complete)

    # top_plays
    # top_plays = extract_top_plays(page,fifaWorldCupGame)
    # top_plays_complete = InfoComplete()
    # top_plays_complete.name = 'top_plays'
    # top_plays_complete.data = top_plays
    # allInfo.append(top_plays_complete)

    # div_play_by_play
    # div_play_by_play = extract_div_play_by_play(page,fifaWorldCupGame)
    # div_play_by_play_complete = InfoComplete()
    # div_play_by_play_complete.name = 'div_play_by_play'
    # div_play_by_play_complete.data = div_play_by_play
    # allInfo.append(div_play_by_play_complete)
        
    time.sleep(5)

    nombre_archivo_game     = fifaWorldCupGame.date +'_'+ game_name                
    ruta_archivo_game_txt   = os.path.join(ruta_game_txt, nombre_archivo_game +'.txt')          
    ruta_archivo_game_json  = os.path.join(ruta_game_json, nombre_archivo_game +'.json')
    # saveArrayOfArray(ruta_archivo_game_txt,linescore_wrap,home_batting)
    saveInfoComplete(ruta_archivo_game_txt,allInfo)
    fifaWorldCupGame.save_to_json(ruta_archivo_game_json)

    print('<--' + current_game)

