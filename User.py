#user
from util.User_manager import UserManager
import os

class User_Contain:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_manager = UserManager()
        
    def sign_up(self):
        while True:
            os.system('cls')
            print("Registration: \n")
            username = input("Enter the username you want (atleast 4 characters or leave blank to cancel): ")
            if not username:
                return
            if len(username) < 4:
                print("username must be at least 4 characters")
                input("press enter key to continue...")
                continue
            password = input("Enter the password you want (atleast 8 characters or leave blank to cancel): ")
            if not password:
                return
            if len(password) < 8:
                print("password must be atleast 8 characters")
                input("press enter key to continue...")
                continue
            register = self.user_manager.register_user(username, password)
            print(register)
            input("Press enter key to continue...")
            if register == "Registration Successful.":
                break
    def login(self):
        while True:
            os.system('cls')
            print("Login:\n")
            username = input("Enter your username, or leave blank to cancel: ")
            if not username:
                return False
            password = input("Enter your password, or leave blank to cancel: ")
            if not password:
                return False
            login_check = self.user_manager.login_user(username, password)
            self.username = username
            print(login_check)
            if login_check == "Login Successful.":
                self.username = username
                return True
            input("press enter key to continue...")
            continue
      