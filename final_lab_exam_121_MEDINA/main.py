# main.py
from utils.user_manager import UserManager
from utils.dice_game import DiceGame
from utils.score import ScoreManager

def main():
    user_manager = UserManager()
    dice_game = DiceGame()
    score_manager = ScoreManager()

    while True:
        user_manager.show_main_menu()
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            user_manager.register()
        elif choice == "2":
            if user_manager.login():
                while True:
                    if not user_manager.logged_in_menu(dice_game, score_manager):
                        break
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()