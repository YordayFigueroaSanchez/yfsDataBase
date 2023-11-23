from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import date
import time
import json
import os
import datetime
from urllib.parse import urlparse
import csv

def lastStrInUrlBeforeDot(paramUrl):
    elementos = paramUrl.split("/")
    # Obtener el último elemento
    ultimo_elemento = elementos[-1]
    # Dividir el último elemento por el punto (.) para separar el nombre de la extensión
    nombre_archivo, extension = ultimo_elemento.split(".")
    return nombre_archivo
def procesingUrlGame(driver,ruta_game,fecha_resultante,paramUrl,dateParam):
    print(paramUrl)
    nombre_archivo = lastStrInUrlBeforeDot(paramUrl)
    driver.get(paramUrl)
    page = BeautifulSoup(driver.page_source,'html.parser')
    # teamId
    teamAway = ''
    teamHome = ''
    # Scoring
    arrLineScoring = []
    div_line_score = page.find('div', id='div_line_score')
    table_head_trs = div_line_score.find('thead').find_all('tr')
    arrLineScoringHead = []
    arrLineScoringHead.append('dateId')
    for table_head_trs_th in table_head_trs[1].find_all('th'):
        arrLineScoringHead.append(table_head_trs_th.text)
    arrLineScoring.append(arrLineScoringHead)
    table_body_trs = div_line_score.find('tbody').find_all('tr')
    for indice, table_body_tr in enumerate(table_body_trs):
        arrLineScoringBody = []
        arrLineScoringBody.append(dateParam)
        table_body_tr_ths = table_body_tr.find_all('th')
        arrLineScoringBody.append(table_body_tr_ths[0].text)
        if indice == 0:
            teamAway = table_body_tr_ths[0].text
        else:
            teamHome = table_body_tr_ths[0].text
        table_body_tr_tds = table_body_tr.find_all('td')
        for table_body_tr_td in table_body_tr_tds:
            arrLineScoringBody.append(table_body_tr_td.text)
        arrLineScoring.append(arrLineScoringBody)
    nombre_archivo_game = fecha_resultante + '_Scoring_' + nombre_archivo +'.txt'
    ruta_archivo_game = os.path.join(ruta_game, nombre_archivo_game)
    with open(ruta_archivo_game, 'w', encoding='utf-8') as archivo2:
        for fila in arrLineScoring:
            result = ''
            for element in fila:
                result += str(element) +';' 
            result = result[:-1] + '\n'
            archivo2.write(result)
    # Four Factors
    arrLineScoring = []
    div_line_score = page.find('div', id='div_four_factors')
    table_head_trs = div_line_score.find('thead').find_all('tr')
    arrLineScoringHead = []
    arrLineScoringHead.append('dateId')
    for table_head_trs_th in table_head_trs[1].find_all('th'):
        arrLineScoringHead.append(table_head_trs_th.text)
    arrLineScoring.append(arrLineScoringHead)
    table_body_trs = div_line_score.find('tbody').find_all('tr')
    for table_body_tr in table_body_trs:
        arrLineScoringBody = []
        arrLineScoringBody.append(dateParam)
        table_body_tr_ths = table_body_tr.find_all('th')
        arrLineScoringBody.append(table_body_tr_ths[0].text)
        table_body_tr_tds = table_body_tr.find_all('td')
        for table_body_tr_td in table_body_tr_tds:
            arrLineScoringBody.append(table_body_tr_td.text)
        arrLineScoring.append(arrLineScoringBody)
    nombre_archivo_game = fecha_resultante + '_FourFactors_' + nombre_archivo +'.txt'
    ruta_archivo_game = os.path.join(ruta_game, nombre_archivo_game)
    with open(ruta_archivo_game, 'w', encoding='utf-8') as archivo3:
        for fila in arrLineScoring:
            result = ''
            for element in fila:
                result += str(element) +';' 
            result = result[:-1] + '\n'
            archivo3.write(result)
    # Basic Box Score Stats
    arrLine = []
    div_data = page.find('div', id='all_box-'+teamAway+'-game-basic')
    table_head_trs = div_data.find('thead').find_all('tr')
    arrLineHead = []
    arrLineHead.append('dateId')
    arrLineHead.append('teamId')
    arrLineHead.append('order')
    arrLineHead.append('playerId')
    for table_head_trs_th in table_head_trs[1].find_all('th'):
        arrLineHead.append(table_head_trs_th.text)
    arrLine.append(arrLineHead)
    table_body_trs = div_data.find('tbody').find_all('tr')
    for indice,table_body_tr in enumerate(table_body_trs):
        arrLineBody = []
        arrLineBody.append(dateParam)
        arrLineBody.append(teamAway)
        arrLineBody.append(indice)
        table_body_tr_ths = table_body_tr.find_all('th')
        try:
            playerId = lastStrInUrlBeforeDot(table_body_tr_ths[0].find('a')['href'])
        except:
            playerId = table_body_tr_ths[0].text
        arrLineBody.append(playerId)
        arrLineBody.append(table_body_tr_ths[0].text)
        table_body_tr_tds = table_body_tr.find_all('td')
        for table_body_tr_td in table_body_tr_tds:
            arrLineBody.append(table_body_tr_td.text)
        arrLine.append(arrLineBody)
    div_data = page.find('div', id='all_box-'+teamHome+'-game-basic')
    table_body_trs = div_data.find('tbody').find_all('tr')
    for indice,table_body_tr in enumerate(table_body_trs):
        arrLineBody = []
        arrLineBody.append(dateParam)
        arrLineBody.append(teamAway)
        arrLineBody.append(indice)
        table_body_tr_ths = table_body_tr.find_all('th')
        try:
            playerId = lastStrInUrlBeforeDot(table_body_tr_ths[0].find('a')['href'])
        except:
            playerId = table_body_tr_ths[0].text
        arrLineBody.append(playerId)
        arrLineBody.append(table_body_tr_ths[0].text)
        table_body_tr_tds = table_body_tr.find_all('td')
        for table_body_tr_td in table_body_tr_tds:
            arrLineBody.append(table_body_tr_td.text)
        arrLine.append(arrLineBody)
    nombre_archivo_game = fecha_resultante + '_BasicBoxScoreStats_' + nombre_archivo +'.txt'
    ruta_archivo_game = os.path.join(ruta_game, nombre_archivo_game)
    with open(ruta_archivo_game, 'w', encoding='utf-8') as archivo3:
        for fila in arrLine:
            result = ''
            for element in fila:
                result += str(element) +';' 
            result = result[:-1] + '\n'
            archivo3.write(result)
    # Advanced Box Score Stats
    arrLine = []
    div_data = page.find('div', id='all_box-'+teamAway+'-game-advanced')
    table_head_trs = div_data.find('thead').find_all('tr')
    arrLineHead = []
    arrLineHead.append('dateId')
    arrLineHead.append('teamId')
    arrLineHead.append('order')
    arrLineHead.append('playerId')
    for table_head_trs_th in table_head_trs[1].find_all('th'):
        arrLineHead.append(table_head_trs_th.text)
    arrLine.append(arrLineHead)
    table_body_trs = div_data.find('tbody').find_all('tr')
    for indice,table_body_tr in enumerate(table_body_trs):
        arrLineBody = []
        arrLineBody.append(dateParam)
        arrLineBody.append(teamAway)
        arrLineBody.append(indice)
        table_body_tr_ths = table_body_tr.find_all('th')
        try:
            playerId = lastStrInUrlBeforeDot(table_body_tr_ths[0].find('a')['href'])
        except:
            playerId = table_body_tr_ths[0].text
        arrLineBody.append(playerId)
        arrLineBody.append(table_body_tr_ths[0].text)
        table_body_tr_tds = table_body_tr.find_all('td')
        for table_body_tr_td in table_body_tr_tds:
            arrLineBody.append(table_body_tr_td.text)
        arrLine.append(arrLineBody)
    div_data = page.find('div', id='all_box-'+teamHome+'-game-advanced')
    table_body_trs = div_data.find('tbody').find_all('tr')
    for indice,table_body_tr in enumerate(table_body_trs):
        arrLineBody = []
        arrLineBody.append(dateParam)
        arrLineBody.append(teamAway)
        arrLineBody.append(indice)
        table_body_tr_ths = table_body_tr.find_all('th')
        try:
            playerId = lastStrInUrlBeforeDot(table_body_tr_ths[0].find('a')['href'])
        except:
            playerId = table_body_tr_ths[0].text
        arrLineBody.append(playerId)
        arrLineBody.append(table_body_tr_ths[0].text)
        table_body_tr_tds = table_body_tr.find_all('td')
        for table_body_tr_td in table_body_tr_tds:
            arrLineBody.append(table_body_tr_td.text)
        arrLine.append(arrLineBody)
    nombre_archivo_game = fecha_resultante + '_AdvancedBoxScoreStats_' + nombre_archivo +'.txt'
    ruta_archivo_game = os.path.join(ruta_game, nombre_archivo_game)
    with open(ruta_archivo_game, 'w', encoding='utf-8') as archivo3:
        for fila in arrLine:
            result = ''
            for element in fila:
                result += str(element) +';' 
            result = result[:-1] + '\n'
            archivo3.write(result)
# url de la data
gameLink = "https://www.basketball-reference.com/boxscores/202306120DEN.html"
# Obtener la fecha actual
# fecha_actual = datetime.datetime.now()
# Formatear la fecha en AAAAMMDD
# fecha_formateada = fecha_actual.strftime("%Y%m%d")
# Formatear la hora en HHMM
# hora_formateada = fecha_actual.strftime("%H%M")
# Combinar la fecha y la hora con _
# fecha_resultante = fecha_formateada + "_" + hora_formateada
fecha_resultante = '20230724_0954'
# Obtener la ruta absoluta del directorio actual
directorio_actual = os.path.abspath(os.path.dirname(__file__))
# Crear la ruta completa del directorio
directory_game = 'game'
ruta_game = os.path.join(directorio_actual, directory_game)
# Comprobar si el directorio existe, si no, crearlo
if not os.path.exists(ruta_game):
    os.makedirs(ruta_game)
ruta_chrome_driver = 'C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/chromedriver.exe'  # Sustituye por tu ruta real
# Crea un objeto Service con la ruta del ejecutable
servicio_chrome = Service(ruta_chrome_driver)
# Crea una instancia de Chrome WebDriver utilizando el objeto Service
driver = webdriver.Chrome(service=servicio_chrome)
listGameLink =[
["24/10/2023","https://www.basketball-reference.com/boxscores/202310240DEN.html"],
]
for gameLink in listGameLink:
    print(gameLink)
    procesingUrlGame(driver,ruta_game,fecha_resultante,gameLink[1],gameLink[0])
    time.sleep(5)