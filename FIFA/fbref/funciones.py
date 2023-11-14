import datetime
import os
import re
from classes import FifaWorldCupTeamPlayer
from classes import FifaWorldCupGoal

def lastStrInUrlBeforeDot(paramUrl):
    elementos = paramUrl.split("/")
    # Obtener el último elemento
    ultimo_elemento = elementos[-1]
    # Dividir el último elemento por el punto (.) para separar el nombre de la extensión
    # nombre_archivo, extension = ultimo_elemento.split(".")
    return ultimo_elemento
def lastStrInUrlBeforeDot2(paramUrl):
    elementos = paramUrl.split("/")
    # Obtener el último elemento
    ultimo_elemento = elementos[-2]
    # Dividir el último elemento por el punto (.) para separar el nombre de la extensión
    # nombre_archivo, extension = ultimo_elemento.split(".")
    return ultimo_elemento
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
def dateInYYYYMMDD_MMSS():
    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now()
    # Formatear la fecha en AAAAMMDD
    fecha_formateada = fecha_actual.strftime("%Y%m%d")
    # Formatear la hora en HHMM
    hora_formateada = fecha_actual.strftime("%H%M")
    # Combinar la fecha y la hora con _
    fecha_resultante = fecha_formateada + "_" + hora_formateada
    return fecha_resultante
def dateInYYYYMMDD():
    fecha_actual = datetime.datetime.now()
    # Formatear la fecha en AAAAMMDD
    return fecha_actual.strftime("%Y%m%d")
def dateInHHMM():
    fecha_actual = datetime.datetime.now()
    return fecha_actual.strftime("%H%M")
def createDirectory(nameDirectory):
    # Obtener la ruta absoluta del directorio actual
    directory_current = os.path.abspath(os.path.dirname(__file__))
    path_directory = os.path.join(directory_current, nameDirectory)
    # Comprobar si el directorio existe, si no, crearlo
    if not os.path.exists(path_directory):
        os.makedirs(path_directory)
    return path_directory
def createDirectoryInPath(currentDirectory, directory):
    path_directory = os.path.join(currentDirectory, directory)
    # Comprobar si el directorio existe, si no, crearlo
    if not os.path.exists(path_directory):
        os.makedirs(path_directory)
    return path_directory
def createDirectoryAndSubdirectory(nameParentDirectory,nameChildDirectory):
    # Obtener la ruta absoluta del directorio actual
    directory_current = os.path.abspath(os.path.dirname(__file__))
    path_nameParentDirectory = os.path.join(directory_current, nameParentDirectory)
    # Comprobar si el directorio existe, si no, crearlo
    if not os.path.exists(path_nameParentDirectory):
        os.makedirs(path_nameParentDirectory)
    path_nameChildDirectory = os.path.join(path_nameParentDirectory, nameChildDirectory)
    # Comprobar si el directorio existe, si no, crearlo
    if not os.path.exists(path_nameChildDirectory):
        os.makedirs(path_nameChildDirectory)
    return path_nameChildDirectory
def extract_linescore_wrap(page,baseballGame):
    dataTable = []
    div_linescore_wrap = page.find('div', class_='linescore_wrap')
    div_tbody_trs = div_linescore_wrap.find('tbody').find_all('tr')
    for iTeam,div_tbody_tr in enumerate(div_tbody_trs):
        dataTableRow = []
        div_tbody_tr_tds = div_tbody_tr.find_all('td')
        for i,td in enumerate(div_tbody_tr_tds):
            # 0-logo
            # 1-name
            # en el inter las anotaciones
            # ultimos 3 - R H E
            if i == 0:
                element_0 = td.find('img')
                dataTableRow.append(element_0['src'])
                if iTeam == 0:
                    baseballGame.away_team.logo = element_0['src']
                else:
                    baseballGame.home_team.logo = element_0['src']
            elif i == 1:
                element_1 = td.find('a')
                dataTableRow.append(element_1['href'])
                if iTeam == 0:
                    baseballGame.away_team.url = element_1['href']
                    baseballGame.away_team.name = element_1.text
                else:
                    baseballGame.home_team.url = element_1['href']
                    baseballGame.home_team.name = element_1.text
            elif i == len(div_tbody_tr_tds)-3:
                dataTableRow.append(td.text)
                if iTeam == 0:
                    baseballGame.away_team.runs = td.text
                else:
                    baseballGame.home_team.runs = td.text
            elif i == len(div_tbody_tr_tds)-2:
                dataTableRow.append(td.text)
                if iTeam == 0:
                    baseballGame.away_team.hits = td.text
                else:
                    baseballGame.home_team.hits = td.text
            elif i == len(div_tbody_tr_tds)-1:
                dataTableRow.append(td.text)
                if iTeam == 0:
                    baseballGame.away_team.errors = td.text
                else:
                    baseballGame.home_team.errors = td.text
            else:
                dataTableRow.append(td.text)
                if iTeam == 0:
                    baseballGame.add_inning_score("away", i-1, td.text)
                else:
                    baseballGame.add_inning_score("home", i-1, td.text)
            
        dataTable.append(dataTableRow)
    return dataTable
def dateTo_YYYYMMDD(date_string ):
    input_format = "%A, %B %d, %Y"
    parsed_date = datetime.datetime.strptime(date_string, input_format)
    output_format = "%Y%m%d"
    formatted_date = parsed_date.strftime(output_format)
    return formatted_date
def extractSubStr(completeStr,subStr):
    posicion = completeStr.find(subStr)
    if posicion != -1:
        subcadena_encontrada = completeStr[posicion + len(subStr):]
    else:
        subcadena_encontrada = ""
    return subcadena_encontrada
def strTotalMinutes(paramStr):
    horas, minutos = map(int, paramStr.split(":"))
    total_minutos = horas * 60 + minutos
    return total_minutos
def extract_scorebox_meta(page,gameTemp):
    dataTable = []
    div = page.find('div', class_='scorebox_meta')
    div_scorebox = div.find_all('div')
    for index,div_current in enumerate(div_scorebox):
        tmpTextCurrent = div_current.text
        if index == 0:
            venuetime = div_current.find('span', class_='venuetime')
            # temDate = dateTo_YYYYMMDD(tmpTextCurrent)
            gameTemp.date = venuetime['data-venue-date']
            gameTemp.start_time = venuetime['data-venue-time']
            dataTable.append(venuetime['data-venue-date'])
            dataTable.append(venuetime['data-venue-time'])
            # print('Date:'  + temDate)
        if 'Start Time: ' in tmpTextCurrent:
            tempStartTime = extractSubStr(tmpTextCurrent,'Start Time: ')
            gameTemp.start_time = tempStartTime
            dataTable.append(tempStartTime)
            # print('Start Time:'  + tmpTextCurrent)
        if 'Attendance: ' in tmpTextCurrent:
            tempAttendance = extractSubStr(tmpTextCurrent,'Attendance: ').replace(',','')
            gameTemp.attendance = tempAttendance
            dataTable.append(tempAttendance)
            # print('Attendance:'  + tmpTextCurrent)
        if 'Venue: ' in tmpTextCurrent:
            tempVenue = extractSubStr(tmpTextCurrent,'Venue: ')
            gameTemp.venue = tempVenue
            dataTable.append(tempVenue)
            # print('Venue:'  + tmpTextCurrent)
        if 'Game Duration: ' in tmpTextCurrent:
            tempGameDuration = str(strTotalMinutes(extractSubStr(tmpTextCurrent,'Game Duration: ')))
            gameTemp.game_duration = tempGameDuration
            dataTable.append(tempGameDuration)
            # print('Game Duration:'  + tmpTextCurrent)
    scorebox = page.find('div', class_='scorebox')
    div_scorebox = scorebox.select('div > div > strong > a')
    print(len(div_scorebox))
    team_01 = div_scorebox[0]
    gameTemp.home_team.name = team_01.text
    gameTemp.home_team.url = team_01['href']
    patron = r"/en/squads/([a-f0-9]+)/"
    resultado = re.search(patron, gameTemp.home_team.url)
    if resultado:
        fragmento = resultado.group(1)
        print("El fragmento es:", fragmento)
        gameTemp.home_team.id = fragmento
    else:
        print("No se encontró ningún fragmento con el patrón proporcionado.")
    print(div_scorebox[1])
    team_02 = div_scorebox[1]
    gameTemp.away_team.name = team_02.text
    gameTemp.away_team.url = team_02['href']
    resultado = re.search(patron, gameTemp.away_team.url)
    if resultado:
        fragmento = resultado.group(1)
        print("El fragmento es:", fragmento)
        gameTemp.away_team.id = fragmento
    else:
        print("No se encontró ningún fragmento con el patrón proporcionado.")
    return dataTable
def substr_from_last_space(texto):
    ultimo_espacio = texto.rfind(" ")
    
    if ultimo_espacio != -1:
        subcadena = texto[ultimo_espacio + 1:]
        return subcadena
    else:
        return texto
def substr_from_last_coma(texto):
    ultimo_espacio = texto.rfind(",")
    
    if ultimo_espacio != -1:
        subcadena = texto[ultimo_espacio + 1:]
        return subcadena
    else:
        return texto
def extract_Details(batter, details):
    arr_details = details.split(",")
    for current_details in arr_details:
        element_amount = "1"
        if "·" in current_details:
            values = current_details.split("·")
            element_amount = values[0]
        if 'HR' in current_details:
            batter.HR = element_amount
        elif '2B' in current_details:
            batter.B2 = element_amount
        elif '3B' in current_details:
            batter.B3 = element_amount
        elif 'CS' in current_details:
            batter.CS = element_amount
        elif 'SB' in current_details:
            batter.SB = element_amount
def extract_players(page,gameParam,status):
    dataTable = []
    if status == 'home':
        nameTeam = gameParam.home_team.id
    else:
        nameTeam = gameParam.away_team.id
    # div_stats_0f66725b_summary
    div_batting_team = 'div_stats_' + nameTeam + '_summary'
    print(div_batting_team)
    div_batting_team_data = page.find('div', id=div_batting_team)
    div_batting_team_data_trs = div_batting_team_data.find('tbody').find_all('tr')
    for index,div_tbody_tr in enumerate(div_batting_team_data_trs):
        dataTableRow = []
        # name
        div_tbody_tr_th_a   = div_tbody_tr.find('th').find('a')
        # print(div_tbody_tr_th_a)
        if div_tbody_tr_th_a == None:
            tmpName = ""
        else:
            tmpName = div_tbody_tr_th_a.text
            tmpLink = div_tbody_tr_th_a['href']
            dataTableRow.append(tmpName)
            dataTableRow.append(tmpLink)
            # pos
            div_tbody_tr_th     = div_tbody_tr.find('th')
            tmpPos = substr_from_last_space(div_tbody_tr_th.text)
            dataTableRow.append(tmpPos)
            # crear batter
            playerTemp = FifaWorldCupTeamPlayer()
            playerTemp.name     = tmpName
            playerTemp.url     = tmpLink
            playerTemp.id       = lastStrInUrlBeforeDot2(tmpLink)
            # more data
            for indexTd,div_tbody_tr_td in enumerate(div_tbody_tr.find_all('td')):
                tempValue = div_tbody_tr_td.text
                dataTableRow.append(tempValue)
                #  0 AB	
                if indexTd == 0:
                    playerTemp.shirtnumber = tempValue
                #  1 R	
                if indexTd == 1:
                    playerTemp.position = tempValue
                #  2 H	
                if indexTd == 2:
                    playerTemp.age = tempValue
                #  3 RBI	
                if indexTd == 3:
                    playerTemp.minutes = tempValue
                #  4 BB	
                if indexTd == 4:
                    playerTemp.goals = tempValue
                #  5 SO	
                if indexTd == 5:
                    playerTemp.assists = tempValue
                #  6 PA	
                if indexTd == 6:
                    playerTemp.pens_made = tempValue
                #  7 BA	
                if indexTd == 7:
                    playerTemp.pens_att = tempValue
                #  8 OBP	
                if indexTd == 8:
                    playerTemp.shots = tempValue
                #  9 SLG	
                if indexTd == 9:
                    playerTemp.shots_on_target = tempValue
                # 10 OPS	
                if indexTd == 10:
                    playerTemp.cards_yellow = tempValue
                # 11 Pit	
                if indexTd == 11:
                    playerTemp.cards_red = tempValue
                # 12 Str	
                if indexTd == 12:
                    playerTemp.fouls = tempValue
                # 13 WPA	
                if indexTd == 13:
                    playerTemp.fouled = tempValue
                # 14 aLI	
                if indexTd == 14:
                    playerTemp.offsides = tempValue
                # 15 WPA+	
                if indexTd == 15:
                    playerTemp.crosses = tempValue
                # 16 WPA-	
                if indexTd == 16:
                    playerTemp.tackles_won = tempValue
                # 17 cWPA	
                if indexTd == 17:
                    playerTemp.interceptions = tempValue
                # 18 acLI	
                if indexTd == 18:
                    playerTemp.own_goals = tempValue
                # 19 RE24	
                if indexTd == 19:
                    playerTemp.pens_won = tempValue
                # 20 PO	
                if indexTd == 20:
                    playerTemp.pens_conceded = tempValue
            if status == 'home':
                gameParam.home_team.add_player(playerTemp)
            else:
                gameParam.away_team.add_player(playerTemp)
            dataTable.append(dataTableRow)
    
    div_batting_team_tfooter = 'tfooter_' + nameTeam.replace(" ", "").replace(".", "") + 'batting'
    div_batting_team_data_tfooter = page.find_all('div', id=div_batting_team_tfooter)
    for current_div in div_batting_team_data_tfooter:
        divs = current_div.find('div')
        for div in divs:
            dataTable.append(div.text)
    return dataTable
def extract_goals(page,gameParam):
    dataTable = []
    div_goals_a = page.find_all('div', class_='event a')
    div_goals_b = page.find_all('div', class_='event b')
    print(len(div_goals_a))
    for element_a in div_goals_a:
        # print(element_a)
        divs_temp = element_a.find_all('div')
        # print(len(divs_temp))
        # for index,div_temp in enumerate(divs_temp):
        #     print(index)
        #     print(div_temp)
        print(divs_temp[0].text.strip().split('’')[0])
        print(divs_temp[0].find('span').text)
        print(lastStrInUrlBeforeDot2(divs_temp[4].find('a')['href']))
        goal_new = FifaWorldCupGoal()
        goal_new.minute = divs_temp[0].text.strip().split('’')[0]
        goal_new.result = divs_temp[0].find('span').text
        gameParam.home_team.add_goal(lastStrInUrlBeforeDot2(divs_temp[4].find('a')['href']),goal_new)
    print(len(div_goals_b))
    for element_b in div_goals_b:
    #     print(element_b)
        # print(element_a)
        divs_temp = element_b.find_all('div')
        # print(len(divs_temp))
        # for index,div_temp in enumerate(divs_temp):
        #     print(index)
        #     print(div_temp)
        print(divs_temp[0].text.strip().split('’')[0])
        print(divs_temp[0].find('span').text)
        print(lastStrInUrlBeforeDot2(divs_temp[4].find('a')['href']))
    return dataTable
def extract_indiv_events(page,baseballGame):
    dataTable = []
    divs = page.find('div', class_='indiv_events').find_all('div')
    for div in divs:
        dataTable.append(div.text)
    return dataTable
def extract_section_content(page,baseballGame):
    dataTable = []
    divs_section_content = page.find_all('div', class_='section_content')
    for div in divs_section_content:
        divs = div.find_all('div')
        for current_div in divs:
            if 'Umpires: ' in current_div.text:
                dataTable.append(current_div.text)
            if 'Time of Game: ' in current_div.text:
                dataTable.append(current_div.text)
            if 'Attendance: ' in current_div.text:
                dataTable.append(current_div.text)
            if 'Field Condition: ' in current_div.text:
                dataTable.append(current_div.text)
            if 'Start Time Weather: ' in current_div.text:
                dataTable.append(current_div.text)
    return dataTable
def extract_div_lineups(page,baseballGame):
    dataTable = []
    div_lineups = page.find('div', id='div_lineups')
    lineups_1 = div_lineups.find('div', id='lineups_1')
    caption = lineups_1.find('caption')
    dataTable.append(caption.text)
    trs = lineups_1.find_all('tr')
    for tr in trs:
        dataTableRow = []
        tds = tr.find_all('td')
        for td in tds:
            dataTableRow.append(td.text)
            tag_a_s = td.find('a')
            if tag_a_s != None:
                dataTableRow.append(tag_a_s['href'])
        dataTable.append(dataTableRow)
    lineups_2 = div_lineups.find('div', id='lineups_2')
    caption = lineups_2.find('caption')
    dataTable.append(caption.text)
    trs = lineups_2.find_all('tr')
    for tr in trs:
        dataTableRow = []
        tds = tr.find_all('td')
        for td in tds:
            dataTableRow.append(td.text)
            tag_a_s = td.find('a')
            if tag_a_s != None:
                dataTableRow.append(tag_a_s['href'])
        dataTable.append(dataTableRow)
    return dataTable
def extract_top_plays(page,baseballGame):
    dataTable = []
    table_top_plays = page.find('table', id='top_plays')
    table_thead = table_top_plays.find('thead').find('tr').find_all('th')
    dataTableRow = []
    for tag_th in table_thead:
        dataTableRow.append(tag_th.text)
    dataTable.append(dataTableRow)
    table_tbody = table_top_plays.find('tbody').find_all('tr')
    for tag_tr in table_tbody:
        dataTableRow = []
        tag_th = tag_tr.find('th')
        dataTableRow.append(tag_th.text)
        tag_tds = tag_tr.find_all('td')
        for tag_td in tag_tds:
            dataTableRow.append(tag_td.text)
        dataTable.append(dataTableRow)
    return dataTable
def extract_div_play_by_play(page,baseballGame):
    dataTable = []
    table_play_by_play = page.find('table', id='play_by_play')
    table_thead = table_play_by_play.find('thead').find('tr').find_all('th')
    dataTableRow = []
    for tag_th in table_thead:
        dataTableRow.append(tag_th.text)
    dataTable.append(dataTableRow)
    table_tbody = table_play_by_play.find('tbody').find_all('tr')
    for tag_tr in table_tbody:
        dataTableRow = []
        tag_th = tag_tr.find('th')
        dataTableRow.append(tag_th.text)
        tag_tds = tag_tr.find_all('td')
        for tag_td in tag_tds:
            dataTableRow.append(tag_td.text)
        dataTable.append(dataTableRow)
    return dataTable
def saveArrayOfArray(path_file,linescore_wrap, home_batting):
    with open(path_file, 'w', encoding="utf-8") as archivo:
        archivo.write('Boxscore' + '\n')
        for fila in linescore_wrap:
            result = ''
            for element in fila:
                result += str(element) +';' 
            result = result[:-1] + '\n'
            archivo.write(result)
        archivo.write('Batting home' + '\n')
        for fila in home_batting:
            result = ''
            for element in fila:
                result += str(element) +';' 
            result = result[:-1] + '\n'
            archivo.write(result)
def saveInfoComplete(path_file,allInfo):
    with open(path_file, 'w', encoding="utf-8") as archivo:
        for elementInfo in allInfo:
            archivo.write( '\n' + elementInfo.name + '\n')
            for fila in elementInfo.data:
                if isinstance(fila, list):
                    result = ''
                    for element in fila:
                        result += str(element) +';' 
                    result = result[:-1]
                else:
                    result = fila
                archivo.write(result + '\n')
        
