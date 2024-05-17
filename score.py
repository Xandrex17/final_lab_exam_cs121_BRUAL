#score
from datetime import datetime
from util.User import User_Contain

class Score:
    def __init__(self, username, game_date, points = 0, wins = 0):
        self.username = username 
        self.game_date = game_date
        self.points = point
        self.wins = win
    
    def reset_score(self):
        point = 0
        wins = 0
        return
    
    def reset_total_score(self):
        self.points = 0
        self.wins = 0
        
    def update_score(self, score, wins):
        self.points += points
        self.wins += wins
    
    def record_score(self):
        self.game_date = datetime.now().strftime("%Y-%m-%d %H: %M: %S")
        return self.username, self.points, self.wins, self.game_date