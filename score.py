#score
from datetime import datetime
from util.User import User_Contain

class Score:
    def __init__(self, username, game_date, points = 0, wins = 0):
        self.username = username 
        self.game_date = game_date
        self.points = points
        self.wins = wins
    
    def reset_score(self):
        points = 0
        wins = 0
        return points, wins
    
    def reset_total_score(self):
        self.points = 0
        self.wins = 0
        
    def update_score(self, points, wins):
        self.points += points
        self.wins += wins
    
    def record_score(self):
        self.game_date = datetime.now().strftime("%Y-%m-%d %H: %M: %S")
        return self.username, self.points, self.wins, self.game_date