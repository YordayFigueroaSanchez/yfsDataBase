import json
import os

# from funciones import createDirectory

class InfoComplete:
    def __init__(self):
        self.name = ""
        self.data = []

class Batter:
    def __init__(self):
        self.name       = ""
        self.AB	        = ""
        self.R	        = ""
        self.H	        = ""
        self.RBI	    = ""
        self.BB	        = ""
        self.SO	        = ""
        self.PA	        = ""
        self.BA	        = ""    
        self.OBP	    = ""
        self.SLG	    = ""
        self.OPS	    = ""
        self.Pit	    = ""
        self.Str	    = ""
        self.WPA	    = ""
        self.aLI	    = ""
        self.WPA_plus	= ""
        self.WPA_minus	= ""
        self.cWPA	    = ""
        self.acLI	    = ""
        self.RE24	    = ""
        self.PO	        = ""
        self.A	        = ""
        self.Details    = ""
        self.HR         = ""
        self.B2         = ""
        self.B3         = ""
        self.CS         = ""
        self.SB         = ""
        self.id         = ""
        
    def __str__(self):
        return f"{self.name}: {self.H} hits in {self.AB} at-bats, {self.RBI} RBI"

class Pitcher:
    def __init__(self):
        self.name       = ""
        self.IP	        = ""
        self.H	        = ""
        self.R	        = ""
        self.ER	        = ""
        self.BB	        = ""
        self.SO	        = ""
        self.HR	        = ""
        self.ERA	    = ""    
        self.BF	        = ""
        self.Pit	    = ""
        self.Str	    = ""
        self.Ctct	    = ""
        self.StS	    = ""
        self.StL	    = ""
        self.GB	        = ""
        self.FB	        = ""
        self.LD	        = ""
        self.Unk	    = ""
        self.GSc	    = ""
        self.IR	        = ""
        self.IS	        = ""
        self.WPA	    = ""
        self.aLI        = ""
        self.cWPA       = ""
        self.acLI       = ""
        self.RE24       = ""
        self.id         = ""
        
    def __str__(self):
        return f"{self.name}: {self.H} hits in {self.IP} at-bats, {self.ERA} RBI"

class Team:
    def __init__(self):
        self.name = ""
        self.logo = ""
        self.url = ""
        self.runs = 0
        self.hits = 0
        self.errors = 0
        self.inning_scores = {}
        self.batters = []  # Lista de bateadores
        self.pitchers = []  # Lista de pitchers

    def add_batter(self, batter):
        self.batters.append(batter)
    
    def add_pitcher(self, pitcher):
        self.pitchers.append(pitcher)

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

# Ejemplo de uso
# game1 = BaseballGame()

# game1.game_number = 1
# game1.home_team.name = "Team A"
# game1.home_team.logo = "team_a_logo.png"
# game1.home_team.url = "http://www.teamA.com"
# game1.away_team.name = "Team B"
# game1.away_team.logo = "team_b_logo.png"
# game1.away_team.url = "http://www.teamB.com"

# game1.add_inning_score("home", 1, 1)
# game1.add_inning_score("home", 2, 0)
# game1.add_inning_score("home", 3, 2)
# game1.add_inning_score("away", 1, 0)
# game1.add_inning_score("away", 2, 1)
# game1.add_inning_score("away", 3, 0)

# print(game1)
# ruta_game = createDirectory('game')
# ruta_archivo_game = os.path.join(ruta_game, "game1.json")   
# game1.save_to_json(ruta_archivo_game)
