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
from funciones import extract_linescore_wrap
from funciones import extract_batting
from funciones import extract_pitching
from funciones import extract_indiv_events
from funciones import extract_section_content
from funciones import extract_div_lineups
from funciones import extract_top_plays
from funciones import extract_div_play_by_play
from funciones import saveArrayOfArray
from funciones import saveInfoComplete
from classes import BaseballGame
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
link_base           = "https://www.baseball-reference.com"
# list_game           = ['/boxes/BAL/BAL202308100.shtml','/boxes/CHN/CHN202303300.shtml','/boxes/PIT/PIT202304070.shtml']
list_game           = [
'/boxes/MIL/MIL202310030.shtml',
'/boxes/MIN/MIN202310030.shtml',
'/boxes/PHI/PHI202310030.shtml',
'/boxes/TBA/TBA202310030.shtml',
'/boxes/MIL/MIL202310040.shtml',
'/boxes/MIN/MIN202310040.shtml',
'/boxes/PHI/PHI202310040.shtml',
'/boxes/TBA/TBA202310040.shtml',
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
    # ruta_game = createDirectory('game')

    link_complete = link_base + link_game
    driver.get(link_complete)
    page = BeautifulSoup(driver.page_source,'html.parser')

    baseballGame = BaseballGame()
    baseballGame.game_number = game_name

    # scorebox_meta
    scorebox_meta = extract_scorebox_meta(page,baseballGame)
    scorebox_meta_complete = InfoComplete()
    scorebox_meta_complete.name = 'Scorebox Meta'
    scorebox_meta_complete.data = scorebox_meta
    allInfo.append(scorebox_meta_complete)

    # linescore
    linescore_wrap = extract_linescore_wrap(page,baseballGame)
    linescore_wrap_complete = InfoComplete()
    linescore_wrap_complete.name = 'Boxscore'
    linescore_wrap_complete.data = linescore_wrap
    allInfo.append(linescore_wrap_complete)

    # home batting
    print('home batting')
    home_batting = extract_batting(page,baseballGame,'home')
    home_batting_complete = InfoComplete()
    home_batting_complete.name = 'Batting home'
    home_batting_complete.data = home_batting
    allInfo.append(home_batting_complete)

    # away batting
    print('away batting')
    away_batting = extract_batting(page,baseballGame,'away')
    away_batting_complete = InfoComplete()
    away_batting_complete.name = 'Batting away'
    away_batting_complete.data = away_batting
    allInfo.append(away_batting_complete)

    # home pitching
    print('home pitching')
    home_pitching = extract_pitching(page,baseballGame,'home')
    home_pitching_complete = InfoComplete()
    home_pitching_complete.name = 'Pitching home'
    home_pitching_complete.data = home_pitching
    allInfo.append(home_pitching_complete)

    # away pitching
    print('away pitching')
    away_pitching = extract_pitching(page,baseballGame,'away')
    away_pitching_complete = InfoComplete()
    away_pitching_complete.name = 'Pitching away'
    away_pitching_complete.data = away_pitching
    allInfo.append(away_pitching_complete)

    # indiv_events
    indiv_events = extract_indiv_events(page,baseballGame)
    indiv_events_complete = InfoComplete()
    indiv_events_complete.name = 'indiv_events'
    indiv_events_complete.data = indiv_events
    allInfo.append(indiv_events_complete)
    
    # section_content
    section_content = extract_section_content(page,baseballGame)
    section_content_complete = InfoComplete()
    section_content_complete.name = 'section_content'
    section_content_complete.data = section_content
    allInfo.append(section_content_complete)

    # div_lineups
    div_lineups = extract_div_lineups(page,baseballGame)
    div_lineups_complete = InfoComplete()
    div_lineups_complete.name = 'div_lineups'
    div_lineups_complete.data = div_lineups
    allInfo.append(div_lineups_complete)

    # top_plays
    top_plays = extract_top_plays(page,baseballGame)
    top_plays_complete = InfoComplete()
    top_plays_complete.name = 'top_plays'
    top_plays_complete.data = top_plays
    allInfo.append(top_plays_complete)

    # div_play_by_play
    div_play_by_play = extract_div_play_by_play(page,baseballGame)
    div_play_by_play_complete = InfoComplete()
    div_play_by_play_complete.name = 'div_play_by_play'
    div_play_by_play_complete.data = div_play_by_play
    allInfo.append(div_play_by_play_complete)
        
    time.sleep(5)

    nombre_archivo_game     = baseballGame.date +'_'+ game_name                
    ruta_archivo_game_txt   = os.path.join(ruta_game_txt, nombre_archivo_game +'.txt')          
    ruta_archivo_game_json  = os.path.join(ruta_game_json, nombre_archivo_game +'.json')
    # saveArrayOfArray(ruta_archivo_game_txt,linescore_wrap,home_batting)
    saveInfoComplete(ruta_archivo_game_txt,allInfo)
    baseballGame.save_to_json(ruta_archivo_game_json)

    print('<--' + current_game)

