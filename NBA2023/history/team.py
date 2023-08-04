import json
from stats import Stats

class Team:
    def __init__(self, name):
        self._name = name
        self._stats = Stats()
        self._players = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, value):
        self._stats = value

    @property
    def players(self):
        return self._players

    def add_player(self, player):
        self._players.append(player)

    def to_dict(self):
        player_list = [player.to_dict() for player in self._players]
        return {
            'name': self._name,
            'stats': self._stats.to_dict(),
            'players': player_list
        }
