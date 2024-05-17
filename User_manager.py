#User Management
import os

class UserManager:
    def __init__(self):
        self.users_folder = "user_data"
        self.users_file = os.path.join(self.users_folder, "list users.txt")
        self.create_users_folder()
        
    def create_users_folder(self):
        if not os.path.exists(self.users_folder):
            os.makedirs(self.users_folder)
    
    def load_users(self):
        users = {}
        if os.path.exists(self.users_file):
            with open(self.users_file, "r") as file_keep:
                for line in file_keep:
                    data = line.strip().split(",")
                    if len(data) == 2:
                        username, password = data
                        users[username] = password
                    else:
                        print(f"Skipping invalid line in users file: {line.strip()}")
        return users
    
    def save_users_load(self, users=None):
        if users is None:
            users = self.load_users()
        with open(self.users_file, "w") as file_keep:
            for username, password in users.items():
                file_keep.write(f"{username}, {password}\n")
        return users
    
    def register_user(self, username, password):
        users = self.load_users()
        if username in users:
            input("Username already exists. press enter key to continue...")
            return 
        users[username] = password
        self.save_users_load(users)
        return "Registration Successful."
    
    def login_user(self, username, password):
        users = self.load_users()
        if username not in users:
            return
        print("Stored password:", users[username])
        return "Login Successful."

    