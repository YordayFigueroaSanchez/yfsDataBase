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
'/boxes/ANA/ANA202309160.shtml',
'/boxes/ARI/ARI202309160.shtml',
'/boxes/BAL/BAL202309160.shtml',
'/boxes/CHA/CHA202309160.shtml',
'/boxes/CLE/CLE202309160.shtml',
'/boxes/COL/COL202309161.shtml',
'/boxes/COL/COL202309162.shtml',
'/boxes/KCA/KCA202309160.shtml',
'/boxes/MIA/MIA202309160.shtml',
'/boxes/MIL/MIL202309160.shtml',
'/boxes/NYN/NYN202309160.shtml',
'/boxes/OAK/OAK202309160.shtml',
'/boxes/PIT/PIT202309160.shtml',
'/boxes/SEA/SEA202309160.shtml',
'/boxes/SLN/SLN202309160.shtml',
'/boxes/TOR/TOR202309160.shtml',
'/boxes/ANA/ANA202309170.shtml',
'/boxes/ARI/ARI202309170.shtml',
'/boxes/BAL/BAL202309170.shtml',
'/boxes/CHA/CHA202309170.shtml',
'/boxes/CLE/CLE202309170.shtml',
'/boxes/COL/COL202309170.shtml',
'/boxes/KCA/KCA202309170.shtml',
'/boxes/MIA/MIA202309170.shtml',
'/boxes/MIL/MIL202309170.shtml',
'/boxes/NYN/NYN202309170.shtml',
'/boxes/OAK/OAK202309170.shtml',
'/boxes/PIT/PIT202309170.shtml',
'/boxes/SEA/SEA202309170.shtml',
'/boxes/SLN/SLN202309170.shtml',
'/boxes/TOR/TOR202309170.shtml',
'/boxes/ATL/ATL202309180.shtml',
'/boxes/CIN/CIN202309180.shtml',
'/boxes/HOU/HOU202309180.shtml',
'/boxes/KCA/KCA202309180.shtml',
'/boxes/LAN/LAN202309180.shtml',
'/boxes/MIA/MIA202309180.shtml',
'/boxes/OAK/OAK202309180.shtml',
'/boxes/SDN/SDN202309180.shtml',
'/boxes/SLN/SLN202309180.shtml',
'/boxes/TEX/TEX202309180.shtml',
'/boxes/WAS/WAS202309180.shtml',
'/boxes/ARI/ARI202309190.shtml',
'/boxes/ATL/ATL202309190.shtml',
'/boxes/CHN/CHN202309190.shtml',
'/boxes/CIN/CIN202309190.shtml',
'/boxes/HOU/HOU202309190.shtml',
'/boxes/KCA/KCA202309190.shtml',
'/boxes/LAN/LAN202309190.shtml',
'/boxes/MIA/MIA202309190.shtml',
'/boxes/NYA/NYA202309190.shtml',
'/boxes/OAK/OAK202309190.shtml',
'/boxes/SDN/SDN202309190.shtml',
'/boxes/SLN/SLN202309190.shtml',
'/boxes/TBA/TBA202309190.shtml',
'/boxes/TEX/TEX202309190.shtml',
'/boxes/WAS/WAS202309190.shtml',
'/boxes/ARI/ARI202309200.shtml',
'/boxes/ATL/ATL202309200.shtml',
'/boxes/CHN/CHN202309200.shtml',
'/boxes/CIN/CIN202309200.shtml',
'/boxes/HOU/HOU202309200.shtml',
'/boxes/KCA/KCA202309200.shtml',
'/boxes/LAN/LAN202309200.shtml',
'/boxes/MIA/MIA202309200.shtml',
'/boxes/NYA/NYA202309200.shtml',
'/boxes/OAK/OAK202309200.shtml',
'/boxes/SDN/SDN202309200.shtml',
'/boxes/SLN/SLN202309200.shtml',
'/boxes/TBA/TBA202309200.shtml',
'/boxes/TEX/TEX202309200.shtml',
'/boxes/WAS/WAS202309200.shtml',
'/boxes/CHN/CHN202309210.shtml',
'/boxes/CLE/CLE202309210.shtml',
'/boxes/LAN/LAN202309210.shtml',
'/boxes/NYA/NYA202309210.shtml',
'/boxes/OAK/OAK202309210.shtml',
'/boxes/PHI/PHI202309210.shtml',
'/boxes/SLN/SLN202309210.shtml',
'/boxes/TBA/TBA202309210.shtml',
'/boxes/WAS/WAS202309210.shtml',
'/boxes/BOS/BOS202309220.shtml',
'/boxes/CHN/CHN202309220.shtml',
'/boxes/CIN/CIN202309220.shtml',
'/boxes/CLE/CLE202309220.shtml',
'/boxes/HOU/HOU202309220.shtml',
'/boxes/LAN/LAN202309220.shtml',
'/boxes/MIA/MIA202309220.shtml',
'/boxes/MIN/MIN202309220.shtml',
'/boxes/NYA/NYA202309220.shtml',
'/boxes/OAK/OAK202309220.shtml',
'/boxes/PHI/PHI202309220.shtml',
'/boxes/SDN/SDN202309220.shtml',
'/boxes/TBA/TBA202309220.shtml',
'/boxes/TEX/TEX202309220.shtml',
'/boxes/WAS/WAS202309220.shtml',
'/boxes/BOS/BOS202309230.shtml',
'/boxes/CHN/CHN202309230.shtml',
'/boxes/CIN/CIN202309230.shtml',
'/boxes/CLE/CLE202309230.shtml',
'/boxes/HOU/HOU202309230.shtml',
'/boxes/LAN/LAN202309230.shtml',
'/boxes/MIA/MIA202309230.shtml',
'/boxes/MIN/MIN202309230.shtml',
'/boxes/OAK/OAK202309230.shtml',
'/boxes/PHI/PHI202309230.shtml',
'/boxes/SDN/SDN202309230.shtml',
'/boxes/TBA/TBA202309230.shtml',
'/boxes/TEX/TEX202309230.shtml',
'/boxes/BOS/BOS202309240.shtml',
'/boxes/CHN/CHN202309240.shtml',
'/boxes/CIN/CIN202309240.shtml',
'/boxes/CLE/CLE202309240.shtml',
'/boxes/HOU/HOU202309240.shtml',
'/boxes/LAN/LAN202309240.shtml',
'/boxes/MIA/MIA202309240.shtml',
'/boxes/MIN/MIN202309240.shtml',
'/boxes/NYA/NYA202309240.shtml',
'/boxes/OAK/OAK202309240.shtml',
'/boxes/PHI/PHI202309240.shtml',
'/boxes/SDN/SDN202309240.shtml',
'/boxes/TBA/TBA202309240.shtml',
'/boxes/TEX/TEX202309240.shtml',
'/boxes/WAS/WAS202309241.shtml',
'/boxes/WAS/WAS202309242.shtml',
'/boxes/ANA/ANA202309250.shtml',
'/boxes/NYA/NYA202309250.shtml',
'/boxes/SEA/SEA202309250.shtml',
'/boxes/SFN/SFN202309250.shtml',
'/boxes/ANA/ANA202309260.shtml',
'/boxes/ATL/ATL202309260.shtml',
'/boxes/BAL/BAL202309260.shtml',
'/boxes/BOS/BOS202309260.shtml',
'/boxes/CHA/CHA202309260.shtml',
'/boxes/CLE/CLE202309260.shtml',
'/boxes/COL/COL202309261.shtml',
'/boxes/COL/COL202309262.shtml',
'/boxes/DET/DET202309260.shtml',
'/boxes/MIL/MIL202309260.shtml',
'/boxes/MIN/MIN202309260.shtml',
'/boxes/PHI/PHI202309260.shtml',
'/boxes/SEA/SEA202309260.shtml',
'/boxes/SFN/SFN202309260.shtml',
'/boxes/TOR/TOR202309260.shtml',
'/boxes/ANA/ANA202309270.shtml',
'/boxes/ATL/ATL202309270.shtml',
'/boxes/BAL/BAL202309270.shtml',
'/boxes/BOS/BOS202309270.shtml',
'/boxes/CHA/CHA202309270.shtml',
'/boxes/CLE/CLE202309270.shtml',
'/boxes/COL/COL202309270.shtml',
'/boxes/DET/DET202309270.shtml',
'/boxes/MIL/MIL202309270.shtml',
'/boxes/MIN/MIN202309270.shtml',
'/boxes/NYN/NYN202309271.shtml',
'/boxes/NYN/NYN202309272.shtml',
'/boxes/PHI/PHI202309270.shtml',
'/boxes/SEA/SEA202309270.shtml',
'/boxes/SFN/SFN202309270.shtml',
'/boxes/TOR/TOR202309270.shtml',
'/boxes/ATL/ATL202309280.shtml',
'/boxes/BAL/BAL202309280.shtml',
'/boxes/CHA/CHA202309280.shtml',
'/boxes/COL/COL202309280.shtml',
'/boxes/DET/DET202309280.shtml',
'/boxes/MIL/MIL202309280.shtml',
'/boxes/MIN/MIN202309280.shtml',
'/boxes/NYN/NYN202309280.shtml',
'/boxes/PHI/PHI202309280.shtml',
'/boxes/SEA/SEA202309280.shtml',
'/boxes/TOR/TOR202309280.shtml',
'/boxes/ANA/ANA202309290.shtml',
'/boxes/ARI/ARI202309290.shtml',
'/boxes/ATL/ATL202309290.shtml',
'/boxes/BAL/BAL202309290.shtml',
'/boxes/CHA/CHA202309290.shtml',
'/boxes/COL/COL202309290.shtml',
'/boxes/DET/DET202309290.shtml',
'/boxes/KCA/KCA202309290.shtml',
'/boxes/MIL/MIL202309290.shtml',
'/boxes/PIT/PIT202309290.shtml',
'/boxes/SEA/SEA202309290.shtml',
'/boxes/SFN/SFN202309290.shtml',
'/boxes/SLN/SLN202309290.shtml',
'/boxes/TOR/TOR202309290.shtml',
'/boxes/ANA/ANA202309300.shtml',
'/boxes/ARI/ARI202309300.shtml',
'/boxes/ATL/ATL202309300.shtml',
'/boxes/BAL/BAL202309300.shtml',
'/boxes/CHA/CHA202309300.shtml',
'/boxes/COL/COL202309300.shtml',
'/boxes/DET/DET202309300.shtml',
'/boxes/KCA/KCA202309300.shtml',
'/boxes/MIL/MIL202309300.shtml',
'/boxes/NYN/NYN202309301.shtml',
'/boxes/NYN/NYN202309302.shtml',
'/boxes/PIT/PIT202309300.shtml',
'/boxes/SEA/SEA202309300.shtml',
'/boxes/SFN/SFN202309300.shtml',
'/boxes/SLN/SLN202309300.shtml',
'/boxes/TOR/TOR202309300.shtml',
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

