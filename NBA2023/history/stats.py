import json

class Stats:
    def __init__(self):
        self.minutes = 0  # MIN (Minutes played)
        self.field_goals_made = 0  # FGM (Field Goals Made)
        self.field_goals_attempted = 0  # FGA (Field Goals Attempted)
        self.field_goal_percentage = 0.0  # FG% (Field Goal Percentage)
        self.three_pointers_made = 0  # 3PM (Three-Pointers Made)
        self.three_pointers_attempted = 0  # 3PA (Three-Pointers Attempted)
        self.three_point_percentage = 0.0  # 3P% (Three-Point Percentage)
        self.free_throws_made = 0  # FTM (Free Throws Made)
        self.free_throws_attempted = 0  # FTA (Free Throws Attempted)
        self.free_throw_percentage = 0.0  # FT% (Free Throw Percentage)
        self.offensive_rebounds = 0  # OREB (Offensive Rebounds)
        self.defensive_rebounds = 0  # DREB (Defensive Rebounds)
        self.total_rebounds = 0  # REB (Total Rebounds)
        self.assists = 0  # AST (Assists)
        self.steals = 0  # STL (Steals)
        self.blocks = 0  # BLK (Blocks)
        self.turnovers = 0  # TO (Turnovers)
        self.personal_fouls = 0  # PF (Personal Fouls)
        self.points = 0  # PTS (Points)
        self.plus_minus = 0.0  # +/- (Plus/Minus)

    def to_dict(self):
        return {
            'minutes': self.minutes,
            'field_goals_made': self.field_goals_made,
            'field_goals_attempted': self.field_goals_attempted,
            'field_goal_percentage': self.field_goal_percentage,
            'three_pointers_made': self.three_pointers_made,
            'three_pointers_attempted': self.three_pointers_attempted,
            'three_point_percentage': self.three_point_percentage,
            'free_throws_made': self.free_throws_made,
            'free_throws_attempted': self.free_throws_attempted,
            'free_throw_percentage': self.free_throw_percentage,
            'offensive_rebounds': self.offensive_rebounds,
            'defensive_rebounds': self.defensive_rebounds,
            'total_rebounds': self.total_rebounds,
            'assists': self.assists,
            'steals': self.steals,
            'blocks': self.blocks,
            'turnovers': self.turnovers,
            'personal_fouls': self.personal_fouls,
            'points': self.points,
            'plus_minus': self.plus_minus
        }
    
    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        self._minutes = value

    @property
    def field_goals_made(self):
        return self._field_goals_made

    @field_goals_made.setter
    def field_goals_made(self, value):
        self._field_goals_made = value

    @property
    def field_goals_attempted(self):
        return self._field_goals_attempted

    @field_goals_attempted.setter
    def field_goals_attempted(self, value):
        self._field_goals_attempted = value

    @property
    def field_goal_percentage(self):
        return self._field_goal_percentage

    @field_goal_percentage.setter
    def field_goal_percentage(self, value):
        self._field_goal_percentage = value

    @property
    def three_pointers_made(self):
        return self._three_pointers_made

    @three_pointers_made.setter
    def three_pointers_made(self, value):
        self._three_pointers_made = value

    @property
    def three_pointers_attempted(self):
        return self._three_pointers_attempted

    @three_pointers_attempted.setter
    def three_pointers_attempted(self, value):
        self._three_pointers_attempted = value

    @property
    def three_point_percentage(self):
        return self._three_point_percentage

    @three_point_percentage.setter
    def three_point_percentage(self, value):
        self._three_point_percentage = value

    @property
    def free_throws_made(self):
        return self._free_throws_made

    @free_throws_made.setter
    def free_throws_made(self, value):
        self._free_throws_made = value

    @property
    def free_throws_attempted(self):
        return self._free_throws_attempted

    @free_throws_attempted.setter
    def free_throws_attempted(self, value):
        self._free_throws_attempted = value

    @property
    def free_throw_percentage(self):
        return self._free_throw_percentage

    @free_throw_percentage.setter
    def free_throw_percentage(self, value):
        self._free_throw_percentage = value

    @property
    def offensive_rebounds(self):
        return self._offensive_rebounds

    @offensive_rebounds.setter
    def offensive_rebounds(self, value):
        self._offensive_rebounds = value

    @property
    def defensive_rebounds(self):
        return self._defensive_rebounds

    @defensive_rebounds.setter
    def defensive_rebounds(self, value):
        self._defensive_rebounds = value

    @property
    def total_rebounds(self):
        return self._total_rebounds

    @total_rebounds.setter
    def total_rebounds(self, value):
        self._total_rebounds = value

    @property
    def assists(self):
        return self._assists

    @assists.setter
    def assists(self, value):
        self._assists = value

    @property
    def steals(self):
        return self._steals

    @steals.setter
    def steals(self, value):
        self._steals = value

    @property
    def blocks(self):
        return self._blocks

    @blocks.setter
    def blocks(self, value):
        self._blocks = value

    @property
    def turnovers(self):
        return self._turnovers

    @turnovers.setter
    def turnovers(self, value):
        self._turnovers = value

    @property
    def personal_fouls(self):
        return self._personal_fouls

    @personal_fouls.setter
    def personal_fouls(self, value):
        self._personal_fouls = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def plus_minus(self):
        return self._plus_minus

    @plus_minus.setter
    def plus_minus(self, value):
        self._plus_minus = value
