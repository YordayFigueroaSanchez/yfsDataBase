from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
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

ubicacion = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver"
driver = webdriver.Chrome(ubicacion)

listGameLink =[

["16/04/2023","https://www.basketball-reference.com/boxscores/202304160MEM.html"],
["16/04/2023","https://www.basketball-reference.com/boxscores/202304160MIL.html"],
["16/04/2023","https://www.basketball-reference.com/boxscores/202304160PHO.html"],
["16/04/2023","https://www.basketball-reference.com/boxscores/202304160DEN.html"],
["17/04/2023","https://www.basketball-reference.com/boxscores/202304170PHI.html"],
["17/04/2023","https://www.basketball-reference.com/boxscores/202304170SAC.html"],
["18/04/2023","https://www.basketball-reference.com/boxscores/202304180BOS.html"],
["18/04/2023","https://www.basketball-reference.com/boxscores/202304180CLE.html"],
["18/04/2023","https://www.basketball-reference.com/boxscores/202304180PHO.html"],
["19/04/2023","https://www.basketball-reference.com/boxscores/202304190MEM.html"],
["19/04/2023","https://www.basketball-reference.com/boxscores/202304190MIL.html"],
["19/04/2023","https://www.basketball-reference.com/boxscores/202304190DEN.html"],
["20/04/2023","https://www.basketball-reference.com/boxscores/202304200BRK.html"],
["20/04/2023","https://www.basketball-reference.com/boxscores/202304200GSW.html"],
["20/04/2023","https://www.basketball-reference.com/boxscores/202304200LAC.html"],
["21/04/2023","https://www.basketball-reference.com/boxscores/202304210ATL.html"],
["21/04/2023","https://www.basketball-reference.com/boxscores/202304210NYK.html"],
["21/04/2023","https://www.basketball-reference.com/boxscores/202304210MIN.html"],
["22/04/2023","https://www.basketball-reference.com/boxscores/202304220BRK.html"],
["22/04/2023","https://www.basketball-reference.com/boxscores/202304220LAC.html"],
["22/04/2023","https://www.basketball-reference.com/boxscores/202304220MIA.html"],
["22/04/2023","https://www.basketball-reference.com/boxscores/202304220LAL.html"],
["23/04/2023","https://www.basketball-reference.com/boxscores/202304230NYK.html"],
["23/04/2023","https://www.basketball-reference.com/boxscores/202304230GSW.html"],
["23/04/2023","https://www.basketball-reference.com/boxscores/202304230ATL.html"],
["23/04/2023","https://www.basketball-reference.com/boxscores/202304230MIN.html"],
["24/04/2023","https://www.basketball-reference.com/boxscores/202304240MIA.html"],
["24/04/2023","https://www.basketball-reference.com/boxscores/202304240LAL.html"],
["25/04/2023","https://www.basketball-reference.com/boxscores/202304250BOS.html"],
["25/04/2023","https://www.basketball-reference.com/boxscores/202304250DEN.html"],
["25/04/2023","https://www.basketball-reference.com/boxscores/202304250PHO.html"],
["26/04/2023","https://www.basketball-reference.com/boxscores/202304260CLE.html"],
["26/04/2023","https://www.basketball-reference.com/boxscores/202304260MEM.html"],
["26/04/2023","https://www.basketball-reference.com/boxscores/202304260MIL.html"],
["26/04/2023","https://www.basketball-reference.com/boxscores/202304260SAC.html"],
["27/04/2023","https://www.basketball-reference.com/boxscores/202304270ATL.html"],
["28/04/2023","https://www.basketball-reference.com/boxscores/202304280GSW.html"],
["28/04/2023","https://www.basketball-reference.com/boxscores/202304280LAL.html"],
["29/04/2023","https://www.basketball-reference.com/boxscores/202304290DEN.html"],
["30/04/2023","https://www.basketball-reference.com/boxscores/202304300NYK.html"],
["30/04/2023","https://www.basketball-reference.com/boxscores/202304300SAC.html"],
["01/05/2023","https://www.basketball-reference.com/boxscores/202305010BOS.html"],
["01/05/2023","https://www.basketball-reference.com/boxscores/202305010DEN.html"],
["02/05/2023","https://www.basketball-reference.com/boxscores/202305020NYK.html"],
["02/05/2023","https://www.basketball-reference.com/boxscores/202305020GSW.html"],
["03/05/2023","https://www.basketball-reference.com/boxscores/202305030BOS.html"],
["04/05/2023","https://www.basketball-reference.com/boxscores/202305040GSW.html"],
["05/05/2023","https://www.basketball-reference.com/boxscores/202305050PHI.html"],
["05/05/2023","https://www.basketball-reference.com/boxscores/202305050PHO.html"],
["06/05/2023","https://www.basketball-reference.com/boxscores/202305060MIA.html"],
["06/05/2023","https://www.basketball-reference.com/boxscores/202305060LAL.html"],
["07/05/2023","https://www.basketball-reference.com/boxscores/202305070PHI.html"],
["07/05/2023","https://www.basketball-reference.com/boxscores/202305070PHO.html"],
["08/05/2023","https://www.basketball-reference.com/boxscores/202305080MIA.html"],
["08/05/2023","https://www.basketball-reference.com/boxscores/202305080LAL.html"],
["09/05/2023","https://www.basketball-reference.com/boxscores/202305090BOS.html"],
["09/05/2023","https://www.basketball-reference.com/boxscores/202305090DEN.html"],
["10/05/2023","https://www.basketball-reference.com/boxscores/202305100NYK.html"],
["10/05/2023","https://www.basketball-reference.com/boxscores/202305100GSW.html"],
["11/05/2023","https://www.basketball-reference.com/boxscores/202305110PHI.html"],
["11/05/2023","https://www.basketball-reference.com/boxscores/202305110PHO.html"],
["12/05/2023","https://www.basketball-reference.com/boxscores/202305120MIA.html"],
["12/05/2023","https://www.basketball-reference.com/boxscores/202305120LAL.html"],
["14/05/2023","https://www.basketball-reference.com/boxscores/202305140BOS.html"],
["16/05/2023","https://www.basketball-reference.com/boxscores/202305160DEN.html"],
["17/05/2023","https://www.basketball-reference.com/boxscores/202305170BOS.html"],
["18/05/2023","https://www.basketball-reference.com/boxscores/202305180DEN.html"],
["19/05/2023","https://www.basketball-reference.com/boxscores/202305190BOS.html"],
["20/05/2023","https://www.basketball-reference.com/boxscores/202305200LAL.html"],
["21/05/2023","https://www.basketball-reference.com/boxscores/202305210MIA.html"],
["22/05/2023","https://www.basketball-reference.com/boxscores/202305220LAL.html"],
["23/05/2023","https://www.basketball-reference.com/boxscores/202305230MIA.html"],
["25/05/2023","https://www.basketball-reference.com/boxscores/202305250BOS.html"],
["27/05/2023","https://www.basketball-reference.com/boxscores/202305270MIA.html"],
["29/05/2023","https://www.basketball-reference.com/boxscores/202305290BOS.html"],
["01/06/2023","https://www.basketball-reference.com/boxscores/202306010DEN.html"],
["04/06/2023","https://www.basketball-reference.com/boxscores/202306040DEN.html"],
["07/06/2023","https://www.basketball-reference.com/boxscores/202306070MIA.html"],
["09/06/2023","https://www.basketball-reference.com/boxscores/202306090MIA.html"],
["12/06/2023","https://www.basketball-reference.com/boxscores/202306120DEN.html"],


]
for gameLink in listGameLink:
    print(gameLink)
    procesingUrlGame(driver,ruta_game,fecha_resultante,gameLink[1],gameLink[0])
    time.sleep(5)
# procesingUrlGame(driver,ruta_game,fecha_resultante,gameLink,'23/10/2023')