from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from entity_table import EntityTable
from entity_element import EntityElement


# url de la data
# https://www.nba.com/stats/player/2544?PerMode=Totals
# https://www.nba.com/stats/player/977?SeasonType=Regular+Season&PerMode=Totals

all_player_link = "https://www.nba.com/stats/player/977?PerMode=Totals"

ubicacion = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver"
try:
    driver = webdriver.Chrome(ubicacion)
    driver.get(all_player_link)
    # Si la página se carga correctamente, el controlador se ha inicializado correctamente
    print("El controlador se ha inicializado correctamente y la página se ha cargado.")
    # Puedes realizar más acciones con el controlador aquí si es necesario
    # ...
    # Cuando hayas terminado, no olvides cerrar el controlador
    page = BeautifulSoup(driver.page_source,'html.parser')
    driver.quit()
except WebDriverException as e:
    print("Error al inicializar el controlador o cargar la página:", e)




# print(page)

#identificar las diferencias de estructura entre profile de jugadores

