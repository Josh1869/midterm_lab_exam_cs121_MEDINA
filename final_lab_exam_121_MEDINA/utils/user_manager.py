# utils/user_manager.py
import os
from .user import User

class UserManager:
    def __init__(self):
        self.current_user = None
        self.users = []
        self.load_users()

    def show_main_menu(self):
        print("\nWelcome to the Dice Game")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

    def register(self):
        self.create_file_if_not_exist('users.txt')

        while True:
            username = input("Enter username (leave blank to cancel): ")
            if username == "":
                return
            if len(username) < 4:
                print("Username must be at least 4 characters long.")
                continue

            password = input("Enter password (leave blank to cancel): ")
            if password == "":
                return
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
                continue

            if any(user.username == username for user in self.users):
                print("Username already exists.")
                continue

            new_user = User(username, password)
            self.users.append(new_user)
            self.save_users()
            print("Registration successful")
            break

    def login(self):
        self.create_file_if_not_exist('users.txt')

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                return True

        print("Invalid username or password.")
        return False

    def logged_in_menu(self, dice_game, score_manager):
        print(f"\nLogged in as {self.current_user.username}")
        print("1. Start Game")
        print("2. Show Top Scores")
        print("3. Log Out")

        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            dice_game.play(self.current_user.username, score_manager)
        elif choice == "2":
            score_manager.show_top_scores()
        elif choice == "3":
            self.current_user = None
            return False
        else:
            print("Invalid choice. Please try again.")
        return True

    def load_users(self):
        self.create_file_if_not_exist('users.txt')

        with open('users.txt', 'r') as f:
            user_data = [line.strip().split(",") for line in f.readlines()]
            self.users = [User(username, password) for username, password in user_data]

    def save_users(self):
        with open('users.txt', 'w') as f:
            for user in self.users:
                f.write(f"{user.username},{user.password}\n")

    def create_file_if_not_exist(self, filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                pass