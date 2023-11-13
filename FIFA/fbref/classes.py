import json
import os

class InfoComplete:
    def __init__(self):
        self.name = ""
        self.data = []
# class Batter:
#     def __init__(self):
#         self.name       = ""
#         self.AB	        = ""
#         self.R	        = ""
#         self.H	        = ""
#         self.RBI	    = ""
#         self.BB	        = ""
#         self.SO	        = ""
#         self.PA	        = ""
#         self.BA	        = ""    
#         self.OBP	    = ""
#         self.SLG	    = ""
#         self.OPS	    = ""
#         self.Pit	    = ""
#         self.Str	    = ""
#         self.WPA	    = ""
#         self.aLI	    = ""
#         self.WPA_plus	= ""
#         self.WPA_minus	= ""
#         self.cWPA	    = ""
#         self.acLI	    = ""
#         self.RE24	    = ""
#         self.PO	        = ""
#         self.A	        = ""
#         self.Details    = ""
#         self.HR         = ""
#         self.B2         = ""
#         self.B3         = ""
#         self.CS         = ""
#         self.SB         = ""
#         self.id         = ""
#     def __str__(self):
#         return f"{self.name}: {self.H} hits in {self.AB} at-bats, {self.RBI} RBI"
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
# class Pitcher:
#     def __init__(self):
#         self.name       = ""
#         self.IP	        = ""
#         self.H	        = ""
#         self.R	        = ""
#         self.ER	        = ""
#         self.BB	        = ""
#         self.SO	        = ""
#         self.HR	        = ""
#         self.ERA	    = ""    
#         self.BF	        = ""
#         self.Pit	    = ""
#         self.Str	    = ""
#         self.Ctct	    = ""
#         self.StS	    = ""
#         self.StL	    = ""
#         self.GB	        = ""
#         self.FB	        = ""
#         self.LD	        = ""
#         self.Unk	    = ""
#         self.GSc	    = ""
#         self.IR	        = ""
#         self.IS	        = ""
#         self.WPA	    = ""
#         self.aLI        = ""
#         self.cWPA       = ""
#         self.acLI       = ""
#         self.RE24       = ""
#         self.id         = ""
#     def __str__(self):
#         return f"{self.name}: {self.H} hits in {self.IP} at-bats, {self.ERA} RBI"

# class Team:
#     def __init__(self):
#         self.name = ""
#         self.logo = ""
#         self.url = ""
#         self.runs = 0
#         self.hits = 0
#         self.errors = 0
#         self.inning_scores = {}
#         self.batters = []  # Lista de bateadores
#         self.pitchers = []  # Lista de pitchers
#     def add_batter(self, batter):
#         self.batters.append(batter)
#     def add_pitcher(self, pitcher):
#         self.pitchers.append(pitcher)
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
class BaseballGame:
    def __init__(self):
        self.game_number = ""
        self.date = ""
        self.start_time = ""
        self.attendance = ""
        self.venue = ""
        self.game_duration = ""
        self.home_team = Team()
        self.away_team = Team()
    def __str__(self):
        home_scores = "\n".join([f"Inning {inning}: {score}" for inning, score in self.home_team.inning_scores.items()])
        away_scores = "\n".join([f"Inning {inning}: {score}" for inning, score in self.away_team.inning_scores.items()])
        return f"Game {self.game_number}: {self.home_team.name} vs {self.away_team.name}\n" \
               f"{self.home_team.name} runs: {self.home_team.runs}, hits: {self.home_team.hits}, errors: {self.home_team.errors}\n" \
               f"{self.away_team.name} runs: {self.away_team.runs}, hits: {self.away_team.hits}, errors: {self.away_team.errors}\n" \
               f"{self.home_team.name} inning scores:\n{home_scores}\n" \
               f"{self.away_team.name} inning scores:\n{away_scores}"
    def add_inning_score(self, team, inning, score):
        if team == "home":
            self.home_team.inning_scores[inning] = score
        elif team == "away":
            self.away_team.inning_scores[inning] = score
    def save_to_json(self, filename):
        game_data = {
            "game_number": self.game_number,
            "date": self.date,
            "start_time": self.start_time,
            "attendance": self.attendance,
            "venue": self.venue,
            "game_duration": self.game_duration,
            "home_team": {
                "name": self.home_team.name,
                "logo": self.home_team.logo,
                "url": self.home_team.url,
                "runs": self.home_team.runs,
                "hits": self.home_team.hits,
                "errors": self.home_team.errors,
                "inning_scores": self.home_team.inning_scores,
                "batters": [
                    {
                        "id": batter.id,
                        "name": batter.name,
                        "AB":batter.AB,
                        "R":batter.R,
                        "H":batter.H,
                        "RBI":batter.RBI,
                        "BB":batter.BB,
                        "SO":batter.SO,
                        "PA":batter.PA,
                        "BA":batter.BA,    
                        "OBP":batter.OBP,
                        "SLG":batter.SLG,
                        "OPS":batter.OPS,
                        "Pit":batter.Pit,
                        "Str":batter.Str,
                        "WPA":batter.WPA,
                        "aLI":batter.aLI,
                        "WPA_plus":batter.WPA_plus,
                        "WPA_minus":batter.WPA_minus,
                        "cWPA":batter.cWPA,
                        "acLI":batter.acLI,
                        "RE24":batter.RE24,
                        "PO":batter.PO,
                        "A":batter.A,
                        "Details":batter.Details,
                        "HR":batter.HR,
                        "B2":batter.B2,
                        "B3":batter.B3,
                        "CS":batter.CS,
                        "SB":batter.SB,
                    }
                    for batter in self.home_team.batters
                ],
                "pitchers": [
                    {
                        "id": pitcher.id,
                        "name": pitcher.name,
                        "IP":pitcher.IP,
                        "R":pitcher.R,
                        "H":pitcher.H,
                        "ER":pitcher.ER,
                        "BB":pitcher.BB,
                        "SO":pitcher.SO,
                        "HR":pitcher.HR,
                        "ERA":pitcher.ERA,    
                        "BF":pitcher.BF,
                        "Pit":pitcher.Pit,
                        "Str":pitcher.Str,
                        "Ctct":pitcher.Ctct,
                        "StS":pitcher.StS,
                        "StL":pitcher.StL,
                        "GB":pitcher.GB,
                        "FB":pitcher.FB,
                        "LD":pitcher.LD,
                        "Unk":pitcher.Unk,
                        "GSc":pitcher.GSc,
                        "IR":pitcher.IR,
                        "IS":pitcher.IS,
                        "WPA":pitcher.WPA,
                        "aLI":pitcher.aLI,
                        "cWPA":pitcher.cWPA,
                        "acLI":pitcher.acLI,
                        "RE24":pitcher.RE24,
                    }
                    for pitcher in self.home_team.pitchers
                ],
            },
            "away_team": {
                "name": self.away_team.name,
                "logo": self.away_team.logo,
                "url": self.away_team.url,
                "runs": self.away_team.runs,
                "hits": self.away_team.hits,
                "errors": self.away_team.errors,
                "inning_scores": self.away_team.inning_scores,
                "batters": [
                    {
                        "id": batter.id,
                        "name": batter.name,
                        "AB":batter.AB,
                        "R":batter.R,
                        "H":batter.H,
                        "RBI":batter.RBI,
                        "BB":batter.BB,
                        "SO":batter.SO,
                        "PA":batter.PA,
                        "BA":batter.BA,    
                        "OBP":batter.OBP,
                        "SLG":batter.SLG,
                        "OPS":batter.OPS,
                        "Pit":batter.Pit,
                        "Str":batter.Str,
                        "WPA":batter.WPA,
                        "aLI":batter.aLI,
                        "WPA_plus":batter.WPA_plus,
                        "WPA_minus":batter.WPA_minus,
                        "cWPA":batter.cWPA,
                        "acLI":batter.acLI,
                        "RE24":batter.RE24,
                        "PO":batter.PO,
                        "A":batter.A,
                        "Details":batter.Details,
                        "HR":batter.HR,
                        "B2":batter.B2,
                        "B3":batter.B3,
                        "CS":batter.CS,
                        "SB":batter.SB,
                    }
                    for batter in self.away_team.batters
                ],
                "pitchers": [
                    {
                        "id": pitcher.id,
                        "name": pitcher.name,
                        "IP":pitcher.IP,
                        "R":pitcher.R,
                        "H":pitcher.H,
                        "ER":pitcher.ER,
                        "BB":pitcher.BB,
                        "SO":pitcher.SO,
                        "HR":pitcher.HR,
                        "ERA":pitcher.ERA,    
                        "BF":pitcher.BF,
                        "Pit":pitcher.Pit,
                        "Str":pitcher.Str,
                        "Ctct":pitcher.Ctct,
                        "StS":pitcher.StS,
                        "StL":pitcher.StL,
                        "GB":pitcher.GB,
                        "FB":pitcher.FB,
                        "LD":pitcher.LD,
                        "Unk":pitcher.Unk,
                        "GSc":pitcher.GSc,
                        "IR":pitcher.IR,
                        "IS":pitcher.IS,
                        "WPA":pitcher.WPA,
                        "aLI":pitcher.aLI,
                        "cWPA":pitcher.cWPA,
                        "acLI":pitcher.acLI,
                        "RE24":pitcher.RE24,
                    }
                    for pitcher in self.away_team.pitchers
                ],
            }
        }
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(game_data, json_file, indent=4, ensure_ascii=False)


