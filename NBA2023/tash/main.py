import json
from player import Player
from stats import Stats
from team import Team
from game import Game

# Create team instances
home_team = Team("Home Team")
away_team = Team("Away Team")

# Create player instances and add them to teams
player1 = Player("Player 1", 1, "image1.jpg", "Active")
player2 = Player("Player 2", 2, "image2.jpg", "Injured")
player3 = Player("Player 3", 3, "image3.jpg", "Active")
player3.full_name = "Yorday"

home_team.add_player(player1)
home_team.add_player(player2)
away_team.add_player(player3)

# Create a game and assign teams
game = Game(home_team, away_team)

# Convert game structure to dictionary
game_data = game.to_dict()

# Save game structure to JSON file
with open('game_data.json', 'w') as file:
    json.dump(game_data, file, indent=4)
