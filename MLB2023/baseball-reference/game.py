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
ruta_chrome_driver = 'C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver.exe'  # Sustituye por tu ruta real
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
'/boxes/CIN/CIN202309012.shtml',
'/boxes/CLE/CLE202309010.shtml',
'/boxes/COL/COL202309010.shtml',
'/boxes/HOU/HOU202309010.shtml',
'/boxes/KCA/KCA202309010.shtml',
'/boxes/LAN/LAN202309010.shtml',
'/boxes/MIL/MIL202309010.shtml',
'/boxes/NYN/NYN202309010.shtml',
'/boxes/OAK/OAK202309010.shtml',
'/boxes/SDN/SDN202309010.shtml',
'/boxes/SLN/SLN202309010.shtml',
'/boxes/TEX/TEX202309010.shtml',
'/boxes/WAS/WAS202309010.shtml',
'/boxes/ARI/ARI202309020.shtml',
'/boxes/CHA/CHA202309020.shtml',
'/boxes/CIN/CIN202309020.shtml',
'/boxes/CLE/CLE202309020.shtml',
'/boxes/COL/COL202309020.shtml',
'/boxes/HOU/HOU202309020.shtml',
'/boxes/KCA/KCA202309020.shtml',
'/boxes/LAN/LAN202309020.shtml',
'/boxes/MIL/MIL202309020.shtml',
'/boxes/NYN/NYN202309020.shtml',
'/boxes/OAK/OAK202309020.shtml',
'/boxes/SDN/SDN202309020.shtml',
'/boxes/SLN/SLN202309020.shtml',
'/boxes/TEX/TEX202309020.shtml',
'/boxes/WAS/WAS202309020.shtml',
'/boxes/ARI/ARI202309030.shtml',
'/boxes/CHA/CHA202309030.shtml',
'/boxes/CIN/CIN202309030.shtml',
'/boxes/CLE/CLE202309030.shtml',
'/boxes/COL/COL202309030.shtml',
'/boxes/HOU/HOU202309030.shtml',
'/boxes/KCA/KCA202309030.shtml',
'/boxes/LAN/LAN202309030.shtml',
'/boxes/MIL/MIL202309030.shtml',
'/boxes/NYN/NYN202309030.shtml',
'/boxes/OAK/OAK202309030.shtml',
'/boxes/SDN/SDN202309030.shtml',
'/boxes/SLN/SLN202309030.shtml',
'/boxes/TEX/TEX202309030.shtml',
'/boxes/WAS/WAS202309030.shtml',
'/boxes/ANA/ANA202309040.shtml',
'/boxes/ARI/ARI202309040.shtml',
'/boxes/CHN/CHN202309040.shtml',
'/boxes/CIN/CIN202309040.shtml',
'/boxes/CLE/CLE202309040.shtml',
'/boxes/KCA/KCA202309040.shtml',
'/boxes/OAK/OAK202309040.shtml',
'/boxes/PIT/PIT202309040.shtml',
'/boxes/SDN/SDN202309040.shtml',
'/boxes/TBA/TBA202309040.shtml',
'/boxes/TEX/TEX202309040.shtml',
'/boxes/ANA/ANA202309050.shtml',
'/boxes/ARI/ARI202309050.shtml',
'/boxes/ATL/ATL202309050.shtml',
'/boxes/CHN/CHN202309050.shtml',
'/boxes/CIN/CIN202309050.shtml',
'/boxes/CLE/CLE202309050.shtml',
'/boxes/KCA/KCA202309050.shtml',
'/boxes/MIA/MIA202309050.shtml',
'/boxes/NYA/NYA202309050.shtml',
'/boxes/OAK/OAK202309050.shtml',
'/boxes/PIT/PIT202309050.shtml',
'/boxes/SDN/SDN202309050.shtml',
'/boxes/TBA/TBA202309050.shtml',
'/boxes/TEX/TEX202309050.shtml',
'/boxes/WAS/WAS202309050.shtml',
'/boxes/ANA/ANA202309060.shtml',
'/boxes/ARI/ARI202309060.shtml',
'/boxes/ATL/ATL202309060.shtml',
'/boxes/CHN/CHN202309060.shtml',
'/boxes/CIN/CIN202309060.shtml',
'/boxes/CLE/CLE202309060.shtml',
'/boxes/KCA/KCA202309060.shtml',
'/boxes/MIA/MIA202309060.shtml',
'/boxes/NYA/NYA202309060.shtml',
'/boxes/OAK/OAK202309060.shtml',
'/boxes/PIT/PIT202309060.shtml',
'/boxes/SDN/SDN202309060.shtml',
'/boxes/TBA/TBA202309060.shtml',
'/boxes/TEX/TEX202309060.shtml',
'/boxes/WAS/WAS202309060.shtml',
'/boxes/ANA/ANA202309070.shtml',
'/boxes/ATL/ATL202309070.shtml',
'/boxes/CHN/CHN202309070.shtml',
'/boxes/MIA/MIA202309070.shtml',
'/boxes/NYA/NYA202309070.shtml',
'/boxes/TBA/TBA202309070.shtml',
'/boxes/ANA/ANA202309080.shtml',
'/boxes/ATL/ATL202309080.shtml',
'/boxes/BOS/BOS202309080.shtml',
'/boxes/CHN/CHN202309080.shtml',
'/boxes/CIN/CIN202309080.shtml',
'/boxes/DET/DET202309080.shtml',
'/boxes/HOU/HOU202309080.shtml',
'/boxes/MIN/MIN202309080.shtml',
'/boxes/NYA/NYA202309080.shtml',
'/boxes/PHI/PHI202309080.shtml',
'/boxes/SFN/SFN202309080.shtml',
'/boxes/TBA/TBA202309080.shtml',
'/boxes/TEX/TEX202309080.shtml',
'/boxes/TOR/TOR202309080.shtml',
'/boxes/WAS/WAS202309080.shtml',
'/boxes/ANA/ANA202309090.shtml',
'/boxes/ATL/ATL202309090.shtml',
'/boxes/BOS/BOS202309090.shtml',
'/boxes/CHN/CHN202309090.shtml',
'/boxes/CIN/CIN202309090.shtml',
'/boxes/DET/DET202309090.shtml',
'/boxes/HOU/HOU202309090.shtml',
'/boxes/MIN/MIN202309090.shtml',
'/boxes/NYA/NYA202309090.shtml',
'/boxes/PHI/PHI202309090.shtml',
'/boxes/SFN/SFN202309090.shtml',
'/boxes/TBA/TBA202309090.shtml',
'/boxes/TEX/TEX202309090.shtml',
'/boxes/TOR/TOR202309090.shtml',
'/boxes/WAS/WAS202309090.shtml',
'/boxes/ANA/ANA202309100.shtml',
'/boxes/ATL/ATL202309100.shtml',
'/boxes/BOS/BOS202309100.shtml',
'/boxes/CHN/CHN202309100.shtml',
'/boxes/CIN/CIN202309100.shtml',
'/boxes/DET/DET202309100.shtml',
'/boxes/HOU/HOU202309100.shtml',
'/boxes/MIN/MIN202309100.shtml',
'/boxes/NYA/NYA202309100.shtml',
'/boxes/PHI/PHI202309100.shtml',
'/boxes/SFN/SFN202309100.shtml',
'/boxes/TBA/TBA202309100.shtml',
'/boxes/TEX/TEX202309100.shtml',
'/boxes/TOR/TOR202309100.shtml',
'/boxes/WAS/WAS202309100.shtml',
'/boxes/BAL/BAL202309110.shtml',
'/boxes/COL/COL202309110.shtml',
'/boxes/HOU/HOU202309110.shtml',
'/boxes/LAN/LAN202309110.shtml',
'/boxes/MIL/MIL202309110.shtml',
'/boxes/MIN/MIN202309110.shtml',
'/boxes/NYN/NYN202309110.shtml',
'/boxes/PHI/PHI202309111.shtml',
'/boxes/PHI/PHI202309112.shtml',
'/boxes/PIT/PIT202309110.shtml',
'/boxes/SEA/SEA202309110.shtml',
'/boxes/SFN/SFN202309110.shtml',
'/boxes/TOR/TOR202309110.shtml',
'/boxes/BAL/BAL202309120.shtml',
'/boxes/BOS/BOS202309121.shtml',
'/boxes/BOS/BOS202309122.shtml',
'/boxes/CHA/CHA202309121.shtml',
'/boxes/CHA/CHA202309122.shtml',
'/boxes/COL/COL202309120.shtml',
'/boxes/DET/DET202309120.shtml',
'/boxes/HOU/HOU202309120.shtml',
'/boxes/LAN/LAN202309120.shtml',
'/boxes/MIL/MIL202309120.shtml',
'/boxes/MIN/MIN202309120.shtml',
'/boxes/NYN/NYN202309120.shtml',
'/boxes/PHI/PHI202309120.shtml',
'/boxes/PIT/PIT202309120.shtml',
'/boxes/SEA/SEA202309120.shtml',
'/boxes/SFN/SFN202309120.shtml',
'/boxes/TOR/TOR202309120.shtml',
'/boxes/BAL/BAL202309130.shtml',
'/boxes/CHA/CHA202309130.shtml',
'/boxes/COL/COL202309130.shtml',
'/boxes/DET/DET202309130.shtml',
'/boxes/HOU/HOU202309130.shtml',
'/boxes/LAN/LAN202309130.shtml',
'/boxes/MIL/MIL202309130.shtml',
'/boxes/MIN/MIN202309130.shtml',
'/boxes/NYN/NYN202309130.shtml',
'/boxes/PHI/PHI202309130.shtml',
'/boxes/PIT/PIT202309130.shtml',
'/boxes/SEA/SEA202309130.shtml',
'/boxes/SFN/SFN202309130.shtml',
'/boxes/TOR/TOR202309130.shtml',
'/boxes/BAL/BAL202309140.shtml',
'/boxes/BOS/BOS202309141.shtml',
'/boxes/BOS/BOS202309142.shtml',
'/boxes/CHA/CHA202309140.shtml',
'/boxes/DET/DET202309140.shtml',
'/boxes/MIL/MIL202309140.shtml',
'/boxes/NYN/NYN202309140.shtml',
'/boxes/PIT/PIT202309140.shtml',
'/boxes/TOR/TOR202309140.shtml',
'/boxes/ANA/ANA202309150.shtml',
'/boxes/ARI/ARI202309150.shtml',
'/boxes/BAL/BAL202309150.shtml',
'/boxes/CHA/CHA202309150.shtml',
'/boxes/CLE/CLE202309150.shtml',
'/boxes/COL/COL202309150.shtml',
'/boxes/KCA/KCA202309150.shtml',
'/boxes/MIA/MIA202309150.shtml',
'/boxes/MIL/MIL202309150.shtml',
'/boxes/NYN/NYN202309150.shtml',
'/boxes/OAK/OAK202309150.shtml',
'/boxes/PIT/PIT202309150.shtml',
'/boxes/SEA/SEA202309150.shtml',
'/boxes/SLN/SLN202309150.shtml',
'/boxes/TOR/TOR202309150.shtml',
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

