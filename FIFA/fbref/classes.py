import json
import os

class InfoComplete:
    def __init__(self):
        self.name = ""
        self.data = []
class FifaWorldCupGoal:
    def __init__(self) -> None:
        self.minute = ""
        self.result = ""
class FifaWorldCupTeamPlayer:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.url = ""
        self.name = ""
        self.shirtnumber = ""
        self.position = ""
        self.age = ""
        self.minutes = ""
        self.goals = ""
        self.assists = ""
        self.pens_made = ""
        self.pens_att = ""
        self.shots = ""
        self.shots_on_target = ""
        self.cards_yellow = ""
        self.cards_red = ""
        self.fouls = ""
        self.fouled = ""
        self.offsides = ""
        self.crosses = ""
        self.tackles_won = ""
        self.interceptions = ""
        self.own_goals = ""
        self.pens_won = ""
        self.pens_conceded = ""
        self.list_goals = []
    def add_goal(self, goal):
        self.list_goals.append(goal)
class FifaWorldCupTeamGoalkeeper:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.url = ""
        self.name = ""
        self.number = ""
        self.pos = ""
        self.age = ""
        self.min = ""
        self.sota = ""
        self.ga = ""
        self.saves = ""
        self.saveX100 = ""
        self.goals = []
    def add_goal(self, goal):
        self.goals.append(goal)
class FifaWorldCupTeam:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.logo = ""
        self.url = ""
        self.kickoff = 0
        self.players = []
        self.goalkeepers  = []
    def add_player(self, player):
        self.players.append(player)
    def add_goalkeeper(self, goalkeeper):
        self.goalkeepers.append(goalkeeper)
    def add_goal(self, id_player,goal):
        jugador_encontrado = next((FifaWorldCupTeamPlayer for jugador in self.players if jugador["id"] == id_player), None)
        if (jugador_encontrado):
            jugador_encontrado.add_goal(goal)
class FifaWorldCupGame:
    def __init__(self):
        self.date = ""
        self.start_time = ""
        self.attendance = ""
        self.venue = ""
        self.home_team = FifaWorldCupTeam()
        self.away_team = FifaWorldCupTeam()
    def save_to_json(self, filename):
        game_data = {
            "date": self.date,
            "start_time": self.start_time,
            "attendance": self.attendance,
            "venue": self.venue,
            "home_team": {
                "name": self.home_team.name,
                "id": self.home_team.id,
                "logo": self.home_team.logo,
                "url": self.home_team.url,
                "kickoff": self.home_team.kickoff,
                "players": [
                    {
                        "name":player.name,
                        "id":player.id,
                        "url":player.url,
                        "name":player.name,
                        "shirtnumber":player.shirtnumber,
                        "position":player.position,
                        "age":player.age,
                        "minutes":player.minutes,
                        "goals":player.goals,
                        "assists":player.assists,
                        "pens_made":player.pens_made,
                        "pens_att":player.pens_att,
                        "shots":player.shots,
                        "shots_on_target":player.shots_on_target,
                        "cards_yellow":player.cards_yellow,
                        "cards_red":player.cards_red,
                        "fouls":player.fouls,
                        "fouled":player.fouled,
                        "offsides":player.offsides,
                        "crosses":player.crosses,
                        "tackles_won":player.tackles_won,
                        "interceptions":player.interceptions,
                        "own_goals":player.own_goals,
                        "pens_won":player.pens_won,
                        "pens_conceded":player.pens_conceded,
                        "list_goals":[
                            {"minute": goal.minute, "result": goal.result}
                            if hasattr(goal, 'minute') and hasattr(goal, 'result')  # Verifica si goal tiene los atributos requeridos
                            else {"minute": None, "result": None}
                            for goal in player.list_goals
                                 ],
                    }
                    for player in self.home_team.players
                ],
                "goalkeepers": [
                    {
                        "id": goalkeeper.id,
                        "url": goalkeeper.url,
                        "name":goalkeeper.name,
                        "number":goalkeeper.number,
                        "pos":goalkeeper.pos,
                        "age":goalkeeper.age,
                        "min":goalkeeper.min,
                        "sota":goalkeeper.sota,
                        "ga":goalkeeper.ga,
                        "saves":goalkeeper.saves,    
                        "saveX100":goalkeeper.saveX100,
                        "goals":[{"minute":goal.minute,"result":goal.result}
                                 for goal in goalkeeper.goals],
                    }
                    for goalkeeper in self.home_team.goalkeepers
                ],
            },
            "away_team": {
                "name": self.away_team.name,
                "id": self.away_team.id,
                "logo": self.away_team.logo,
                "url": self.away_team.url,
                "kickoff": self.away_team.kickoff,
                "players": [
                    {
                        "name":player.name,
                        "id":player.id,
                        "url":player.url,
                        "name":player.name,
                        "shirtnumber":player.shirtnumber,
                        "position":player.position,
                        "age":player.age,
                        "minutes":player.minutes,
                        "goals":player.goals,
                        "assists":player.assists,
                        "pens_made":player.pens_made,
                        "pens_att":player.pens_att,
                        "shots":player.shots,
                        "shots_on_target":player.shots_on_target,
                        "cards_yellow":player.cards_yellow,
                        "cards_red":player.cards_red,
                        "fouls":player.fouls,
                        "fouled":player.fouled,
                        "offsides":player.offsides,
                        "crosses":player.crosses,
                        "tackles_won":player.tackles_won,
                        "interceptions":player.interceptions,
                        "own_goals":player.own_goals,
                        "pens_won":player.pens_won,
                        "pens_conceded":player.pens_conceded,
                        "list_goals":[
                            {"minute": goal.minute, "result": goal.result}
                            # if hasattr(goal, 'minute') and hasattr(goal, 'result')  # Verifica si goal tiene los atributos requeridos
                            # else {"minute": None, "result": None}
                            for goal in player.list_goals
                                 ],
                    }
                    for player in self.away_team.players
                ],
                "goalkeepers": [
                    {
                        "id": goalkeeper.id,
                        "url": goalkeeper.url,
                        "name":goalkeeper.name,
                        "number":goalkeeper.number,
                        "pos":goalkeeper.pos,
                        "age":goalkeeper.age,
                        "min":goalkeeper.min,
                        "sota":goalkeeper.sota,
                        "ga":goalkeeper.ga,
                        "saves":goalkeeper.saves,    
                        "saveX100":goalkeeper.saveX100,
                        
                    }
                    for goalkeeper in self.away_team.goalkeepers
                ],
            }
        }
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(game_data, json_file, indent=4, ensure_ascii=False)


