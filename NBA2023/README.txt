**********************************************************************************************************************************
**********************************************************************************************************************************
RESULTADO DE SCRIPT NBA box score by player
player/box score

const elements = $x('//div[@class="nba-stat-table__overflow"]/table/tbody/tr/td[@class="player-name first"]/..'); 	
for (element in elements) {
		var cadena = '{';
		var aaa = elements[element];
		var listTd = aaa.querySelectorAll('td');
		cadena += '"player":"' + listTd[0].querySelector('a').text + '",';
		cadena += '"player_url":"' + listTd[0].querySelector('a').href + '",';
		cadena += '"team":"' + listTd[1].querySelector('a').text + '",';
		cadena += '"team_url":"' + listTd[1].querySelector('a').href + '",';
		cadena += '"match":"' + listTd[2].querySelector('a').text + '",';
		cadena += '"match_url":"' + listTd[2].querySelector('a').href + '",';
		cadena += '"date":"' + listTd[3].querySelector('a').text + '",';
		cadena += '"date_url":"' + listTd[3].querySelector('a').href + '",';
		cadena += '"result":"' + listTd[5].innerHTML + '",';
		cadena += '"min":"' + listTd[6].innerHTML + '",';
		cadena += '"pts":"' + listTd[7].innerHTML + '",';
		var elemnt8 = listTd[8].querySelector('a');
		if (elemnt8 == null){
			cadena += '"fgm":"' + listTd[8].innerText + '",';
		}
		else {
			cadena += '"fgm":"' + elemnt8.innerText + '",';
		}
		var elemnt9 = listTd[9].querySelector('a');
		if (elemnt9 == null){
			cadena += '"fga":"' + listTd[9].innerText + '",';
		}
		else {
			cadena += '"fga":"' + elemnt9.innerText + '",';
		}
		cadena += '"fg100":"' + listTd[10].innerHTML + '",';
		
		var elemnt11 = listTd[11].querySelector('a');
		if (elemnt11 == null){
			cadena += '"mp3":"' + listTd[11].innerText + '",';
		}
		else {
			cadena += '"mp3":"' + elemnt11.innerText + '",';
		}
		var elemnt12 = listTd[12].querySelector('a');
		if (elemnt12 == null){
			cadena += '"ap3":"' + listTd[12].innerText + '",';
		}
		else {
			cadena += '"ap3":"' + elemnt12.innerText + '",';
		}
		cadena += '"p3100":"' + listTd[13].innerHTML + '",';
		
		var elemnt14 = listTd[14].querySelector('a');
		if (elemnt14 == null){
			cadena += '"ftm":"' + listTd[14].innerText + '",';
		}
		else {
			cadena += '"ftm":"' + elemnt14.innerText + '",';
		}
		var elemnt15 = listTd[15].querySelector('a');
		if (elemnt15 == null){
			cadena += '"fta":"' + listTd[15].innerText + '",';
		}
		else {
			cadena += '"fta":"' + elemnt15.innerText + '",';
		}
		cadena += '"ft100":"' + listTd[16].innerHTML + '",';
		
		var elemnt17 = listTd[17].querySelector('a');
		if (elemnt17 == null){
			cadena += '"oreb":"' + listTd[17].innerText + '",';
		}
		else {
			cadena += '"oreb":"' + elemnt17.innerText + '",';
		}
		
		var elemnt18 = listTd[18].querySelector('a');
		if (elemnt18 == null){
			cadena += '"dreb":"' + listTd[18].innerText + '",';
		}
		else {
			cadena += '"dreb":"' + elemnt18.innerText + '",';
		}
		
		var elemnt19 = listTd[19].querySelector('a');
		if (elemnt19 == null){
			cadena += '"reb":"' + listTd[19].innerText + '",';
		}
		else {
			cadena += '"reb":"' + elemnt19.innerText + '",';
		}
		
		var elemnt20 = listTd[20].querySelector('a');
		if (elemnt20 == null){
			cadena += '"ast":"' + listTd[20].innerText + '",';
		}
		else {
			cadena += '"ast":"' + elemnt20.innerText + '",';
		}
		
		var elemnt21 = listTd[21].querySelector('a');
		if (elemnt21 == null){
			cadena += '"stl":"' + listTd[21].innerText + '",';
		}
		else {
			cadena += '"stl":"' + elemnt21.innerText + '",';
		}
		
		var elemnt22 = listTd[22].querySelector('a');
		if (elemnt22 == null){
			cadena += '"blk":"' + listTd[22].innerText + '",';
		}
		else {
			cadena += '"blk":"' + elemnt22.innerText + '",';
		}
		
		var elemnt23 = listTd[23].querySelector('a');
		if (elemnt23 == null){
			cadena += '"tov":"' + listTd[23].innerText + '",';
		}
		else {
			cadena += '"tov":"' + elemnt23.innerText + '",';
		}
		
		cadena += '"pf":"' + listTd[24].innerHTML + '",';
		
		cadena += '"minusplus":"' + listTd[25].innerHTML + '",';
		
		cadena += '"fp":"' + listTd[26].innerHTML + '",';
		
		cadena += '},';
		console.log(cadena);
				
	}
	
	notas
		copiar todo
		llevar a notepad++
		sustituir "script : 1"
		agregar [ al inicio
		agregar ] al final
		

**********************************************************************************************************************************
**********************************************************************************************************************************
https://www.nba.com/players
List of player

const elements = $x('//table/tbody/tr'); 	
for (element in elements) 
{
	var cadena = '{';
	var aaa = elements[element];
	var listTd = aaa.querySelectorAll('td');
	
	var elemnt00_0 = listTd[0].querySelector('a');
	cadena += 'player_url:"' + elemnt00_0.href + '",';
	
	var elemnt00_1 = listTd[0].querySelector('a > div > img');
	cadena += 'player_img:"' + elemnt00_1.src + '",';
	cadena += 'player_alt:"' + elemnt00_1.alt + '",';
	
	var elemnt00_2 = listTd[0].querySelectorAll('a > div > p');
	cadena += 'player_first_name:"' + elemnt00_2[0].innerText + '",';
	cadena += 'player_last_name:"' + elemnt00_2[1].innerText + '",';
	
	var elemnt01 = listTd[1].querySelector('a');
	if(elemnt01 == null){
		cadena += 'team_url:"N/A",';
		cadena += 'team_name:"N/A",';
	} else {
		cadena += 'team_url:"' + elemnt01.href + '",';
		cadena += 'team_name:"' + elemnt01.innerText + '",';
	}
	
	cadena += 'number:"' + listTd[2].innerText + '",';
	cadena += 'position:"' + listTd[3].innerText + '",';
	cadena += 'height:"' + listTd[4].innerText + '",';
	cadena += 'weight:"' + listTd[5].innerText + '",';
	cadena += 'last_attended:"' + listTd[6].innerText + '",';
	cadena += 'country:"' + listTd[7].innerText + '",';
	
	cadena += '}';
	console.log(cadena);
}
**********************************************************************************************************************************
**********************************************************************************************************************************
**																																**
**															NOTES BEFORE														**
**																																**
**********************************************************************************************************************************
**********************************************************************************************************************************
var all = $x('//div[@class="nba-stat-table__overflow"]/table/tbody/tr');
for (element in all) {
		var cadena = element.text;
        console.log(cadena); 
    }
	
	
var all = $x('//div[@class="nba-stat-table__overflow"]/table/tbody/tr');
for (tr in all) {
		var cadena = all[tr].innerHtml;
    }

var all = $x('//div[@class="nba-stat-table__overflow"]/table/tbody/tr');
for (tr in all) {
		console.log(all[tr]);
    }

const elements = $x('//div[@class="nba-stat-table__overflow"]/table/tbody/tr/td[@class="player-name first"]/..'); 	
for (element in elements) {
		var aaa = elements[element];
		var listTd = aaa.querySelectorAll('td');
		console.log(listTd[0])
	}
	
*******************************************************************************************************************************	
RESULTADO DE SCRIPT NBA box score by player
player/box score

const elements = $x('//div[@class="nba-stat-table__overflow"]/table/tbody/tr/td[@class="player-name first"]/..'); 	
for (element in elements) {
		var cadena = '{';
		var aaa = elements[element];
		var listTd = aaa.querySelectorAll('td');
		cadena += '"player":"' + listTd[0].querySelector('a').text + '",';
		cadena += '"player_url":"' + listTd[0].querySelector('a').href + '",';
		cadena += '"team":"' + listTd[1].querySelector('a').text + '",';
		cadena += '"team_url":"' + listTd[1].querySelector('a').href + '",';
		cadena += '"match":"' + listTd[2].querySelector('a').text + '",';
		cadena += '"match_url":"' + listTd[2].querySelector('a').href + '",';
		cadena += '"date":"' + listTd[3].querySelector('a').text + '",';
		cadena += '"date_url":"' + listTd[3].querySelector('a').href + '",';
		cadena += '"result":"' + listTd[5].innerHTML + '",';
		cadena += '"min":"' + listTd[6].innerHTML + '",';
		cadena += '"pts":"' + listTd[7].innerHTML + '",';
		var elemnt8 = listTd[8].querySelector('a');
		if (elemnt8 == null){
			cadena += '"fgm":"' + listTd[8].innerText + '",';
		}
		else {
			cadena += '"fgm":"' + elemnt8.innerText + '",';
		}
		var elemnt9 = listTd[9].querySelector('a');
		if (elemnt9 == null){
			cadena += '"fga":"' + listTd[9].innerText + '",';
		}
		else {
			cadena += '"fga":"' + elemnt9.innerText + '",';
		}
		cadena += '"fg100":"' + listTd[10].innerHTML + '",';
		
		var elemnt11 = listTd[11].querySelector('a');
		if (elemnt11 == null){
			cadena += '"mp3":"' + listTd[11].innerText + '",';
		}
		else {
			cadena += '"mp3":"' + elemnt11.innerText + '",';
		}
		var elemnt12 = listTd[12].querySelector('a');
		if (elemnt12 == null){
			cadena += '"ap3":"' + listTd[12].innerText + '",';
		}
		else {
			cadena += '"ap3":"' + elemnt12.innerText + '",';
		}
		cadena += '"p3100":"' + listTd[13].innerHTML + '",';
		
		var elemnt14 = listTd[14].querySelector('a');
		if (elemnt14 == null){
			cadena += '"ftm":"' + listTd[14].innerText + '",';
		}
		else {
			cadena += '"ftm":"' + elemnt14.innerText + '",';
		}
		var elemnt15 = listTd[15].querySelector('a');
		if (elemnt15 == null){
			cadena += '"fta":"' + listTd[15].innerText + '",';
		}
		else {
			cadena += '"fta":"' + elemnt15.innerText + '",';
		}
		cadena += '"ft100":"' + listTd[16].innerHTML + '",';
		
		var elemnt17 = listTd[17].querySelector('a');
		if (elemnt17 == null){
			cadena += '"oreb":"' + listTd[17].innerText + '",';
		}
		else {
			cadena += '"oreb":"' + elemnt17.innerText + '",';
		}
		
		var elemnt18 = listTd[18].querySelector('a');
		if (elemnt18 == null){
			cadena += '"dreb":"' + listTd[18].innerText + '",';
		}
		else {
			cadena += '"dreb":"' + elemnt18.innerText + '",';
		}
		
		var elemnt19 = listTd[19].querySelector('a');
		if (elemnt19 == null){
			cadena += '"reb":"' + listTd[19].innerText + '",';
		}
		else {
			cadena += '"reb":"' + elemnt19.innerText + '",';
		}
		
		var elemnt20 = listTd[20].querySelector('a');
		if (elemnt20 == null){
			cadena += '"ast":"' + listTd[20].innerText + '",';
		}
		else {
			cadena += '"ast":"' + elemnt20.innerText + '",';
		}
		
		var elemnt21 = listTd[21].querySelector('a');
		if (elemnt21 == null){
			cadena += '"stl":"' + listTd[21].innerText + '",';
		}
		else {
			cadena += '"stl":"' + elemnt21.innerText + '",';
		}
		
		var elemnt22 = listTd[22].querySelector('a');
		if (elemnt22 == null){
			cadena += '"blk":"' + listTd[22].innerText + '",';
		}
		else {
			cadena += '"blk":"' + elemnt22.innerText + '",';
		}
		
		var elemnt23 = listTd[23].querySelector('a');
		if (elemnt23 == null){
			cadena += '"tov":"' + listTd[23].innerText + '",';
		}
		else {
			cadena += '"tov":"' + elemnt23.innerText + '",';
		}
		
		cadena += '"pf":"' + listTd[24].innerHTML + '",';
		
		cadena += '"minusplus":"' + listTd[25].innerHTML + '",';
		
		cadena += '"fp":"' + listTd[26].innerHTML + '",';
		
		cadena += '},';
		console.log(cadena);
				
	}
	
	notas
		copiar todo
		llevar a notepad++
		sustituir "script : 1"
		agregar [ al inicio
		agregar ] al final
		
	
*******************************************************************************************************************************
List of player

const elements = $x('//table/tbody/tr'); 	
for (element in elements) 
{
	var cadena = '{';
	var aaa = elements[element];
	var listTd = aaa.querySelectorAll('td');
	
	var elemnt00_0 = listTd[0].querySelector('a');
	cadena += 'player_url:"' + elemnt00_0.href + '",';
	
	var elemnt00_1 = listTd[0].querySelector('a > div > img');
	cadena += 'player_img:"' + elemnt00_1.src + '",';
	cadena += 'player_alt:"' + elemnt00_1.alt + '",';
	
	var elemnt00_2 = listTd[0].querySelectorAll('a > div > p');
	cadena += 'player_first_name:"' + elemnt00_2[0].innerText + '",';
	cadena += 'player_last_name:"' + elemnt00_2[1].innerText + '",';
	
	var elemnt01 = listTd[1].querySelector('a');
	if(elemnt01 == null){
		cadena += 'team_url:"N/A",';
		cadena += 'team_name:"N/A",';
	} else {
		cadena += 'team_url:"' + elemnt01.href + '",';
		cadena += 'team_name:"' + elemnt01.innerText + '",';
	}
	
	cadena += 'number:"' + listTd[2].innerText + '",';
	cadena += 'position:"' + listTd[3].innerText + '",';
	cadena += 'height:"' + listTd[4].innerText + '",';
	cadena += 'weight:"' + listTd[5].innerText + '",';
	cadena += 'last_attended:"' + listTd[6].innerText + '",';
	cadena += 'country:"' + listTd[7].innerText + '",';
	
	cadena += '}';
	console.log(cadena);
}
