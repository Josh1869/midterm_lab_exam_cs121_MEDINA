# utils/dice_game.py
import random

class DiceGame:
    def play(self, username, score_manager):
        points = 0
        stages_won = 0

        while True:
            if not self.play_stage():
                print("GAME OVER. You didn't win any stages.")
                break
            stages_won += 1
            points += 3
            print(f"Current points: {points}. Stages won: {stages_won}.")

            keep_playing = input("Enter 1 to continue playing, 0 to stop: ")
            if keep_playing != "1":
                break

        if stages_won > 0:  # Change based on your requirements for when to record scores
            score_manager.record_score(username, points, stages_won)

    def play_stage(self):
        wins = 0
        tries = 0
        while wins < 2 and tries < 3:
            user_roll = random.randint(1, 6)
            computer_roll = random.randint(1, 6)
            print(f"You rolled {user_roll}, Computer rolled {computer_roll}")

            if user_roll > computer_roll:
                wins += 1
                print("You won this round!")
            elif user_roll == computer_roll:
                print("It's a tie. Rolling again...")
                tries -= 1  # Ties do not count as a try.

            tries += 1

        return wins == 2