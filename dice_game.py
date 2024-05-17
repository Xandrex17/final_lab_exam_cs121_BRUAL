#dice_gane
import os
import random
from util.score import Score

class DiceGames:
    def __init__(self, username):
        self.username = username
        self.folder_score = "list of scores"
        self.file_score = os.path.join(self.folder_score, "list of rankings")
        self.create_folder_score()
        self.score = Score(self.username,"")
    
    def create_folder_score(self):
        if not os.path.exists(self.folder_score):
            os.makedirs(self.folder_score)
    
    def get_scores(self):
        scores =[]
        try:
            if os.path.exists(self.folder_score):
                with open(self.file_score, "r") as score_file:
                    for i in score_file:
                        username, score, player_round, date = i.strip().split(",")
                        scores.append((username, int(score), int(player_round), date))
            return scores
        except FileNotFoundError:
            return None
        
    def save_scores(self, score):
        with open(self.file_score, "w") as score_file:
            for username, score, player_round, game_date in scores:
                scores.append((username, int(score),int(player_round), game_date))
                score_file.write(f"{username},{score},{wins},{game_date}")
                
    def show_scores(self):
        os.system('cls')
        print("This are the Top Scres:")
        scores = self.get_scores()
        if not scores:
            print("You haven't played any games..")
            input("press enter key to continue...")
        for i, (username, score, win_stages, date) in enumerate(scores, start=1):
            print(f"{i}. {username}: Points won: {score}, Wins: {win_stages} (Achieved On: {date})")
        input("press enter key to continue...")
    
    def to_continue_main(self):
            choice = input("\nDo you want to continue to the next stage? (1 for yes or 0 for no): ")
            if choice == '1':
                return True
            elif choice == '0':
                print("Thank you for playing")
                input("press enter key to continue...")
                return False
            else:
                print("Invalid choice. please try again.")
                input("press enter key to continue...")
    
    def main_game(self):
        os.system('cls')
        player_points = 0
        cpu_points = 0
        player_round = 0
        
        while True: 
            for i in range(3):
                cpu_play = random.randint(1,6)
                player_play = random.randint(1,6)
                
                print(f"{self.username} rolled: {player_play}")
                print(f" CPU rolled: {cpu_play}")
                if player_play > cpu_play:
                    player_points += 1
                    print(f"You win this round! {self.username}")
                elif player_play < cpu_play:
                    cpu_play += 1
                    print("CPU wint this round!")
                if player_play == cpu_play:
                    print("Its a tie\n")
            
            if player_points == cpu_points:
                while player_play == cpu_points:
                    cpu_play = random.randint(1,6)
                    player_play = random.randint(1,6)
                
                    print(f"{self.username} rolled: {player_play}")
                    print(f" CPU rolled: {cpu_play}")
                    if player_play > cpu_play:
                        player_points += 1
                        print(f"You win this round! {self.username}")
                    if player_play < cpu_play:
                        cpu_points += 1
                        print("CPU wint this round!")
                    if player_play == cpu_play:
                        print("Its a tie\n")
                    
            if player_play > cpu_play:
                player_points += 3
                player_round += 1
                self.score.update_score(player_points, player_round)
                player_points, cpu_points = self.score.reset_score()
                print(f"\n You won this Stage {self.username}!\n")
                
                if self.to_continue_main():
                    continue
                else:
                    high_score = self.get_scores()
                    high_score.append(self.score.record_score())
                    high_score.sort(key=self.get_scores, reverse=True)
                    high_score = top_scores[:10] #slice to only the first 10 index
                    self.save_scores(high_score) #save scores
                    self.score.reset_total_score() #reset overall score
                    if player_round < 1:
                        print(f"Game Over. You won {player_round} stage.")    
                    else:
                        print(f"Game Over. You won {player_round} stages.")
                    break
            if player_points < cpu_points:
                if player_round == 0:
                    player_points = self.score.reset_score()
                    print("\n You lost this stage \n")
                    print("Game Over. You didn't win any stages")
                    input("press enter key to continue...")
                    break
                
            self.score.update_score(player_points, 0)
            player_points, cpu_points = self.score.reset_score()
            high_score = self.get_scores()
            high_score.append(self.score.record_score())
            high_score.sort(key=lambda x: x[1], reverse=True)
            high_score = high_score[:10]
            self.save_scores(high_score)
            self.score.reset_total_score
            print("you've lost this stage")
            if player_round <1:
                print(f"Game Over. You won {player_round} stage.")
            else:
                print(f"Game Over. You won {player_round} stages.")
            input("Press Enter to Continue...")
            break
    def menu(self):
        while True:
            os.system('cls')
            print(f"Welcome, {self.username}")
            print("Menu: ")
            print("1. Start")
            print("2. Show Top Scores")
            print("3. Logout")
            choice = input("Enter the number of your choice: ")
            if choice == '1':
                self.main_game()
            elif choice == '2':
                self.show_scores()
            elif choice == '3':
                print(f"Thank You for playing, Good bye {self.username}")        
                input("Logging out...press enter key to continue...")
                return
            else:
                print("Invalid choice. Please try again....")
                input("press enter key to continue...")
                continue