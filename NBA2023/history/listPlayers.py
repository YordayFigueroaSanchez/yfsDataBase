from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from entity_table import EntityTable
from entity_element import EntityElement

table = EntityTable('test')

# url de la data
all_player_link = "https://www.nba.com/stats/alltime-leaders?SeasonType=Regular+Season"

ubicacion = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver"
driver = webdriver.Chrome(ubicacion)
driver.get(all_player_link)
page = BeautifulSoup(driver.page_source,'html.parser')

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


#identificar las diferencias de estructura entre profile de jugadores

