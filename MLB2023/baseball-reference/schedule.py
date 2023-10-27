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
# Comprobar si el directorio existe, si no, crearlo
if not os.path.exists(ruta_schedule):
    os.makedirs(ruta_schedule)
# Nombre del archivo que deseas guardar
nombre_archivo_schedule = fecha_resultante +'.txt'
nombre_archivo_schedule_only_link = fecha_resultante +'_link.txt'
# Combinar la ruta del directorio actual con el nombre del archivo
ruta_archivo_schedule = os.path.join(ruta_schedule, nombre_archivo_schedule)
ruta_archivo_schedule_only_link = os.path.join(ruta_schedule, nombre_archivo_schedule_only_link)

# ubicacion = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver"
# driver = webdriver.Chrome(ubicacion)
# Especifica la ruta al ejecutable de ChromeDriver
# para actualizar el chromedriver https://googlechromelabs.github.io/chrome-for-testing/#stable
ruta_chrome_driver = 'C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/chromedriver.exe'  # Sustituye por tu ruta real
# Crea un objeto Service con la ruta del ejecutable
servicio_chrome = Service(ruta_chrome_driver)
# Crea una instancia de Chrome WebDriver utilizando el objeto Service
driver = webdriver.Chrome(service=servicio_chrome)

listGameTemp = []
listGameLink = []
listGameLinkOnly = []

# url de la data
schedule_link = "https://www.baseball-reference.com/leagues/majors/2023-schedule.shtml"
driver.get(schedule_link)
page = BeautifulSoup(driver.page_source,'html.parser')
#   div_4649142714
#   div_2554848825
#   div_4800524807
# div_1998533194
# div_9550324858
# div_3799355433
# div_1762894190 postseason
    
div_schedule = page.find('div', id='div_1762894190')
divs = div_schedule.find_all('div')
for div in divs:
    div_h3 = div.find('h3')
    listGameLink.append([div_h3.text])

    div_ps = div.find_all('p')
    # print(div_ps)
    # Bandera para saltar el último ciclo
    skip_last = False

    for i,div_p in enumerate(div_ps):
        # Verificamos si estamos en la penúltima iteración
        if i == len(div_ps) - 1:
            skip_last = True

        # Si la bandera es True, continuamos al siguiente ciclo sin hacer nada
        if skip_last:
            continue

        # print(div_p)
        p_em_a = div_p.find('em').find('a')
        listGameLink.append([p_em_a.text,p_em_a['href']])
        listGameLinkOnly.append(p_em_a['href'])
    
time.sleep(5)


with open(ruta_archivo_schedule, 'w') as archivo:
    for fila in listGameLink:
       result = ''
       for element in fila:
           result += str(element) +';' 
       result = result[:-1] + '\n'
       archivo.write(result)
with open(ruta_archivo_schedule_only_link, 'w') as archivo:
    for fila in listGameLinkOnly:
       archivo.write("'" + str(fila) + "'," + "\n")