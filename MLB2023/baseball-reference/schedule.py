from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
import time
import json
import os
import datetime
from urllib.parse import urlparse
import csv
import re

def lastStrInUrlBeforeDot(paramUrl):
    elementos = paramUrl.split("/")
    # Obtener el último elemento
    ultimo_elemento = elementos[-1]
    # Dividir el último elemento por el punto (.) para separar el nombre de la extensión
    nombre_archivo, extension = ultimo_elemento.split(".")
    return nombre_archivo

def transform_date(date_str):
    # Definimos los formatos de entrada y salida de la fecha
    input_format = "%a, %b %d, %Y"
    output_format = "%d/%m/%Y"

    try:
        # Convertimos la cadena a un objeto datetime
        date_obj = datetime.datetime.strptime(date_str, input_format)
        # Formateamos la fecha como una cadena en el formato deseado
        transformed_date = date_obj.strftime(output_format)
        return transformed_date
    except ValueError:
        return date_str
    

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


# Obtener la fecha actual
fecha_actual = datetime.datetime.now()
# Formatear la fecha en AAAAMMDD
fecha_formateada = fecha_actual.strftime("%Y%m%d")
# Formatear la hora en HHMM
hora_formateada = fecha_actual.strftime("%H%M")
# Combinar la fecha y la hora con _
fecha_resultante = fecha_formateada + "_" + hora_formateada
# fecha_resultante = '20230723_2026'
# Obtener la ruta absoluta del directorio actual
directorio_actual = os.path.abspath(os.path.dirname(__file__))
# Nombre del directorio donde deseas guardar el archivo
directory_schedule = 'schedule'
# Crear la ruta completa del directorio
ruta_schedule = os.path.join(directorio_actual, directory_schedule)
directory_game = 'game'
ruta_game = os.path.join(directorio_actual, directory_game)
# Comprobar si el directorio existe, si no, crearlo
if not os.path.exists(ruta_schedule):
    os.makedirs(ruta_schedule)
if not os.path.exists(ruta_game):
    os.makedirs(ruta_game)
# Nombre del archivo que deseas guardar
nombre_archivo_schedule = fecha_resultante +'.txt'
nombre_archivo_schedule_game = fecha_resultante +'_game.txt'
# Combinar la ruta del directorio actual con el nombre del archivo
ruta_archivo_schedule = os.path.join(ruta_schedule, nombre_archivo_schedule)
ruta_archivo_schedule_game = os.path.join(ruta_schedule, nombre_archivo_schedule_game)

ubicacion = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver"
driver = webdriver.Chrome(ubicacion)

listGameTemp = []
listGameLink = []

# url de la data
schedule_link = "https://www.baseball-reference.com/leagues/majors/2023-schedule.shtml"
driver.get(schedule_link)
page = BeautifulSoup(driver.page_source,'html.parser')
div_schedule = page.find('div', id='div_2122175774')
divs = div_schedule.find_all('div')
for div in divs:
    div_h3 = div.find('h3')
    listGameLink.append([div_h3.text])

    div_ps = div.find_all('p')
    print(div_ps)
    # Bandera para saltar el último ciclo
    skip_last = False

    for i,div_p in enumerate(div_ps):
        # Verificamos si estamos en la penúltima iteración
        if i == len(div_ps) - 1:
            skip_last = True

        # Si la bandera es True, continuamos al siguiente ciclo sin hacer nada
        if skip_last:
            continue

        print(div_p)
        p_em_a = div_p.find('em').find('a')
        listGameLink.append([p_em_a.text,p_em_a['href']])

    # table_body_tr_ths = table_body_tr.find_all('th')
    # element_0 = transform_date(table_body_tr_ths[0].text)
    # if element_0 == 'Date':
    #     continue;
    # # print(table_body_tr_ths)
    # table_body_tr_tds = table_body_tr.find_all('td')
    # # print(table_body_tr_tds)
    # element_1 = table_body_tr_tds[0].text
    # print(element_1)

    # element_team_visitor_td = table_body_tr_tds[1]
    # element_team_visitor_name = element_team_visitor_td.text
    # element_team_visitor_link = element_team_visitor_td.find('a')['href']
    # element_team_visitor_link_split = element_team_visitor_link.split("/")
    # element_team_visitor_link_name = element_team_visitor_link_split[2]
    
    # element_3 = table_body_tr_tds[2].text
    
    # element_team_home_td = table_body_tr_tds[3]
    # element_team_home_name = element_team_home_td.text
    # element_team_home_link = element_team_home_td.find('a')['href']
    # element_team_home_link_split = element_team_home_link.split("/")
    # element_team_home_link_name = element_team_home_link_split[2]
    
    # element_5 = table_body_tr_tds[4].text
    
    # element_6 = table_body_tr_tds[5].text
    # element_6_link = table_body_tr_tds[5].find('a')['href']
    
    # element_7 = table_body_tr_tds[6].text
    
    # element_attend = table_body_tr_tds[7].text
    # element_attend = re.sub(r',', '', element_attend)
    
    # element_9 = table_body_tr_tds[8].text
    
    # element_10 = table_body_tr_tds[9].text
    
    # listGameLink.append([element_0,'https://www.basketball-reference.com'+element_6_link])
    # listGameTemp.append([element_0,
    #                      element_1,
    #                      element_team_visitor_name,element_team_visitor_link_name,
    #                      element_3,
    #                      element_team_home_name,element_team_home_link_name,
    #                      element_5,
    #                      element_6_link,
    #                      element_7,
    #                      element_attend,
    #                      element_9,
    #                      element_10])
time.sleep(5)


with open(ruta_archivo_schedule, 'w') as archivo:
    for fila in listGameLink:
       result = ''
       for element in fila:
           result += str(element) +';' 
       result = result[:-1] + '\n'
       archivo.write(result)

# with open(ruta_archivo_schedule, 'w') as archivo:
#     for fila in listGameTemp:
#        result = ''
#        for element in fila:
#            result += str(element) +';' 
#        result = result[:-1] + '\n'
#        archivo.write(result)
# with open(ruta_archivo_schedule_game, 'w') as archivo:
#     for fila in listGameLink:
#        result = '["'+fila[0]+'","'+fila[1]+'"],\n'
#        archivo.write(result)