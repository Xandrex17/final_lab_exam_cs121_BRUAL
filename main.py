#main function to run dice game
from util.User import User_Contain
from util.dice_game import DiceGames
import os

def main():
    while True:
        os.system('cls')
        user = User_Contain("","")
        print("WELCOME TO DICE ROLL GAME!")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            user.sign_up()
        elif choice == '2':
            user.login()
            if user.login():
                login = DiceGames(user.username)
                login.main_game()
        elif choice == '3':
            print("EXITING...")
            input("press enter key to continue...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("press enter key to continue...")
            continue

if __name__ == "__main__":
    main()
    