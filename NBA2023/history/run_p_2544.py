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

from history_traditional import traditional_row
from history_traditional import advanced_row
from history_traditional import misc_row
from history_traditional import scoring_row
from history_traditional import usage_row
from history_data import history_data
from entity_table import EntityTable
from entity_element import EntityElement

def fileDirectory():
    return 'dfd'
def extractTraditionals(traditionalTd):
   tds = traditionalTd.findAll("td")
   traditionalRow = traditional_row(YEAR=tds[0].text, 
                                    TEAM=tds[1].text, 
                                    GP=tds[2].text, 
                                    MIN=tds[3].text, 
                                    PTS=tds[4].text, 
                                    FGM=tds[5].text, 
                                    FGA=tds[6].text, 
                                    FG_PERCENT=tds[7].text,
                                    THREE_PM=tds[8].text, 
                                    THREE_PA=tds[9].text, 
                                    THREE_P_PERCENT=tds[10].text, 
                                    FTM=tds[11].text, 
                                    FTA=tds[12].text, 
                                    FT_PERCENT=tds[13].text,
                                    OREB=tds[14].text, 
                                    DREB=tds[15].text, 
                                    REB=tds[16].text, 
                                    AST=tds[17].text, 
                                    TOV=tds[18].text, 
                                    STL=tds[19].text, 
                                    BLK=tds[20].text, 
                                    PF=tds[21].text, 
                                    FP=tds[22].text, 
                                    DD2=tds[23].text, 
                                    TD3=tds[24].text, 
                                    PLUS_MINUS=tds[25].text)
   return traditionalRow
def extractAdvanceds(traditionalTd):
   tds = traditionalTd.findAll("td")
   traditionalRow = advanced_row(YEAR=tds[0].text, 
                                    TEAM=tds[1].text, 
                                    GP=tds[2].text, 
                                    MIN=tds[3].text, 
                                    OFFRTG=tds[4].text, 
                                    DEFRTG=tds[5].text, 
                                    NETRTG=tds[6].text, 
                                    AST_PERCENT=tds[7].text,
                                    AST_TO=tds[8].text, 
                                    AST_RATIO=tds[9].text, 
                                    OREB_PERCENT=tds[10].text, 
                                    DREB_PERCENT=tds[11].text, 
                                    REB_PERCENT=tds[12].text, 
                                    TO_RATIO=tds[13].text,
                                    EFG_PERCENT=tds[14].text, 
                                    TS_PERCENT=tds[15].text, 
                                    USG_PERCENT=tds[16].text, 
                                    PACE=tds[17].text, 
                                    PIE=tds[18].text)
   return traditionalRow
def extractMiscs(traditionalTd):
   tds = traditionalTd.findAll("td")
   traditionalRow = misc_row(BY_YEAR=tds[0].text, 
                                    TEAM=tds[1].text, 
                                    GP=tds[2].text, 
                                    MIN=tds[3].text, 
                                    PTS_OFF_TO=tds[4].text, 
                                    SECOND_PTS=tds[5].text, 
                                    FBPS=tds[6].text, 
                                    PITP=tds[7].text,
                                    OPP_PTS_OFF_TO=tds[8].text, 
                                    OPP_SECOND_PTS=tds[9].text, 
                                    OPP_FBPS=tds[10].text, 
                                    OPP_PITP=tds[11].text, 
                                    BLK=tds[12].text, 
                                    BLKA=tds[13].text,
                                    PF=tds[14].text, 
                                    PFD=tds[15].text)
   return traditionalRow
def extractScorings(traditionalTd):
   tds = traditionalTd.findAll("td")
   traditionalRow = scoring_row(BY_YEAR=tds[0].text, 
                                    TEAM=tds[1].text, 
                                    GP=tds[2].text, 
                                    MIN=tds[3].text, 
                                    FGA_2PT_PERCENT=tds[4].text, 
                                    FGA_3PT_PERCENT=tds[5].text, 
                                    PTS_2PT_PERCENT=tds[6].text, 
                                    PTS_2PT_MR_PERCENT=tds[7].text,
                                    PTS_3PT_PERCENT=tds[8].text, 
                                    PTS_FBPS_PERCENT=tds[9].text, 
                                    PTS_FT_PERCENT=tds[10].text, 
                                    PTS_OFFTO_PERCENT=tds[11].text, 
                                    PTS_PITP_PERCENT=tds[12].text, 
                                    FGM_2FGM_AST_PERCENT=tds[13].text,
                                    FGM_2FGM_UAST_PERCENT=tds[14].text, 
                                    FGM_3FGM_AST_PERCENT=tds[15].text,
                                    FGM_3FGM_UAST_PERCENT=tds[16].text,
                                    FGM_AST_PERCENT=tds[17].text, 
                                    FGM_UAST_PERCENT=tds[18].text
                                    )
   return traditionalRow
def extractUsagess(traditionalTd):
   tds = traditionalTd.findAll("td")
   traditionalRow = usage_row(BY_YEAR=tds[0].text, 
                                    TEAM=tds[1].text, 
                                    GP=tds[2].text, 
                                    MIN=tds[3].text, 
                                    USG_PERCENT=tds[4].text, 
                                    FGM_PERCENT=tds[5].text, 
                                    FGA_PERCENT=tds[6].text, 
                                    THREE_PM_PERCENT=tds[7].text,
                                    THREE_PA_PERCENT=tds[8].text, 
                                    FTM_PERCENT=tds[9].text, 
                                    FTA_PERCENT=tds[10].text, 
                                    OREB_PERCENT=tds[11].text, 
                                    DREB_PERCENT=tds[12].text, 
                                    REB_PERCENT=tds[13].text,
                                    AST_PERCENT=tds[14].text, 
                                    TOV_PERCENT=tds[15].text,
                                    STL_PERCENT=tds[16].text,
                                    BLK_PERCENT=tds[17].text, 
                                    BLKA_PERCENT=tds[18].text,
                                    PF_PERCENT=tds[19].text, 
                                    PFD_PERCENT=tds[20].text, 
                                    PTS_PERCENT=tds[21].text
                                    )
   return traditionalRow
def saveFile(data):
    # Parsear la URL
    # parsed_url = urlparse(url)
    # Obtener la ruta
    # path = parsed_url.path
    # Dividir la ruta por "/"
    # segments = path.split("/")
    # Eliminar segmentos vacíos
    # segments = [segment for segment in segments if segment]
    #id player
    idPlayer = data.id
    # Obtener la fecha actual
    fecha_actual = datetime.date.today()
    # Formatear la fecha en AAAAMMDD
    fecha_formateada = fecha_actual.strftime("%Y%m%d")

    # Obtener la ruta absoluta del directorio actual
    directorio_actual = os.path.abspath(os.path.dirname(__file__))
    # Nombre del directorio donde deseas guardar el archivo
    nombre_directorio = fecha_formateada
    # Crear la ruta completa del directorio
    ruta_directorio = os.path.join(directorio_actual, nombre_directorio)
    # Comprobar si el directorio existe, si no, crearlo
    if not os.path.exists(ruta_directorio):
        os.makedirs(ruta_directorio)
    # Nombre del archivo que deseas guardar
    nombre_archivo = 'player_' + idPlayer + '.json'
    # Combinar la ruta del directorio actual con el nombre del archivo
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    # Save game structure to JSON file
    with open(ruta_archivo, 'w') as file:
        json.dump(data.to_dict(), file, indent=4)
    return 0
def saveFileCsv(data):
    #id player
    idPlayer = data.id
    # Obtener la fecha actual
    fecha_actual = datetime.date.today()
    # Formatear la fecha en AAAAMMDD
    fecha_formateada = fecha_actual.strftime("%Y%m%d")

    # Obtener la ruta absoluta del directorio actual
    directorio_actual = os.path.abspath(os.path.dirname(__file__))
    # Nombre del directorio donde deseas guardar el archivo
    nombre_directorio = fecha_formateada
    # Crear la ruta completa del directorio
    ruta_directorio = os.path.join(directorio_actual, nombre_directorio)
    # Comprobar si el directorio existe, si no, crearlo
    if not os.path.exists(ruta_directorio):
        os.makedirs(ruta_directorio)
    # Nombre del archivo que deseas guardar
    nombre_archivo = 'player_' + idPlayer + '.csv'
    # dataCsv
    # dataCsv = [["NAME","YEAR","PTS"]]
    # for element in data.traditional_data:
    #     dataCsv.append([data.name,element.YEAR,element.PTS])
    # Combinar la ruta del directorio actual con el nombre del archivo
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    # Guardar los datos en el archivo CSV
    with open(ruta_archivo, mode='w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(data.to_csv())
    return 0
def extractGeneral(url):
    ubicacion = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver"
    driver = webdriver.Chrome(ubicacion)
    driver.get(url)

    # Parsear la URL
    parsed_url = urlparse(url)
    # Obtener la ruta
    path = parsed_url.path
    # Dividir la ruta por "/"
    segments = path.split("/")
    # Eliminar segmentos vacíos
    segments = [segment for segment in segments if segment]
    #id player
    idPlayer = segments[2]

    page = BeautifulSoup(driver.page_source,'html.parser')

    # info player
    elemntsSection = page.findAll("section", class_=lambda c: c and c.startswith("PlayerSummary_summaryTop"))
    print(len(elemntsSection))
    elemntsSectionName = page.findAll("p", class_=lambda c: c and c.startswith("PlayerSummary_playerNameText"))
    print(len(elemntsSectionName))
    name = ''
    for elemntSectionName in elemntsSectionName:
        name += elemntSectionName.text
    
    history = history_data(id=idPlayer, name=name)

    elemntsTable = page.findAll("table", class_=lambda c: c and c.startswith("Crom_table"))
    # print(len(elemntsTable))

    # 1 TRADITIONAL SPLITS
    traditionalsTd = elemntsTable[0].select("tbody > tr")
    # print(traditionalsTd)
    for traditionalTd in traditionalsTd:
        # history.traditional_data.add_row(extractTraditionals(traditionalTd))
        history.traditional_data.append(extractTraditionals(traditionalTd))

    # 2 ADVANCED SPLITS
    advancedsTd = elemntsTable[1].select("tbody > tr")
    # print(len(advancedsTd))
    for advancedTd in advancedsTd:
        history.advanced_data.append(extractAdvanceds(advancedTd))

    # 3 MISC SPLITS
    miscsTd = elemntsTable[2].select("tbody > tr")
    # print(len(miscsTd))
    for miscTd in miscsTd:
        history.misc_data.append(extractMiscs(miscTd))

    # 4 SCORING SPLITS
    scoringsTd = elemntsTable[3].select("tbody > tr")
    # print(len(scoringsTd))
    for scoringTd in scoringsTd:
        history.scoring_data.append(extractScorings(scoringTd))

    # 5 USAGE SPLITS
    usagesTd = elemntsTable[4].select("tbody > tr")
    # print(len(usagesTd))
    for usageTd in usagesTd:
        history.usage_data.append(extractUsagess(usageTd))
    return history
def extractAllPlayers(url):
    ubicacion = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver"
    driver = webdriver.Chrome(ubicacion)
    driver.get(url)
    
    page = BeautifulSoup(driver.page_source,'html.parser')
    table = EntityTable('test')
    elemntsThead = page.findAll("thead")
    # print(len(elemntsThead))

    elemntsTheadTh = elemntsThead[0].select("tr > th")
    # print(len(elemntsTheadTh))

    head = EntityElement()
    for indice, elemntTheadTh in enumerate(elemntsTheadTh):
        if indice == 1:
            head.add_element(elemntTheadTh.text)
            head.add_element('url')
        else:    
            head.add_element(elemntTheadTh.text)
    table.head.append(head)

    elemntsTbody = page.findAll("tbody", class_=lambda c: c and c.startswith("Crom_body"))
    # print(len(elemntsTbody))

    elemntsTbodyTr = elemntsTbody[0].select("tr")
    # print(len(elemntsTbodyTr))
    for elementTbodyTr in elemntsTbodyTr:
        body = EntityElement()
        for indice, elemntTbodyTd in enumerate(elementTbodyTr):
            if indice == 1:
                body.add_element(elemntTbodyTd.text)
                elemntTbodyTdA = elemntTbodyTd.select("a")
                body.add_element(elemntTbodyTdA[0].get('href'))
                # print(elemntTbodyTdA[0].get('href'))
            else:
                body.add_element(elemntTbodyTd.text)
                
        table.body.append(body)
    # table.print()
    return table
def saveFileCsvGeneric(data,file_name):
    # Obtener la fecha actual
    fecha_actual = datetime.date.today()
    # Formatear la fecha en AAAAMMDD
    fecha_formateada = fecha_actual.strftime("%Y%m%d")
    # Obtener la ruta absoluta del directorio actual
    directorio_actual = os.path.abspath(os.path.dirname(__file__))
    # Nombre del directorio donde deseas guardar el archivo
    nombre_directorio = fecha_formateada
    # Crear la ruta completa del directorio
    ruta_directorio = os.path.join(directorio_actual, nombre_directorio)
    # Comprobar si el directorio existe, si no, crearlo
    if not os.path.exists(ruta_directorio):
        os.makedirs(ruta_directorio)
    # Nombre del archivo que deseas guardar
    nombre_archivo = file_name
    # Combinar la ruta del directorio actual con el nombre del archivo
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    # Guardar los datos en el archivo CSV
    with open(ruta_archivo, mode='w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(data.to_csv())
    return 0


# url de la data
home_link = "https://www.nba.com/stats/player/2544?PerMode=Totals"

# data player
data = extractGeneral(home_link)

# Save file in json url,history_data
# saveFile(data)
# Save file in csv url,history_data
saveFileCsv(data)



