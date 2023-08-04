import json

class Game:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def to_dict(self):
        return {
            'home_team': self.home_team.to_dict(),
            'away_team': self.away_team.to_dict()
        }
