from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date
import time

def extraNameFull( element): 
  div_a_span_element = element.select('div > a > span', class_=lambda c: c and c.startswith("GameBoxscoreTablePlayer_gbpNameFull"))
  return div_a_span_element[0].text


ubicacion = "C:/Users/yfigueroa/Documents/GitHub/yfsDataBase/NBA2023/chromedriver" #Ruta del driver
driver = webdriver.Chrome(ubicacion)

home_link = "https://www.nba.com/game/phx-vs-den-0042200225/box-score#box-score"
search_kw = "iphone x".replace(" ","+")

driver.get(home_link)

phone_title = []
phone_link = []
phone_status = []
phone_score = []
phone_reviews_amt = []
phone_price = []
phone_location = []

pg_amount = 5

page = BeautifulSoup(driver.page_source,'html.parser')

elemntsTBODY = page.findAll("tbody", class_=lambda c: c and c.startswith("StatsTableBody_tbody"))
for elemntTBODY in elemntsTBODY:
  elementsTR = elemntTBODY.find_all("tr")
  for elemenTR in elementsTR:
    elementsTD = elemenTR.find_all("td")
    #for elemenTD in elementsTD:
    print(len(elementsTD))
    #extraer nombre
    print(extraNameFull(elementsTD[0]))

