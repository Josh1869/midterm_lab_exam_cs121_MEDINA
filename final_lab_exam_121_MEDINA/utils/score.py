# utils/score_manager.py
import os

class ScoreManager:
    def __init__(self):
        self.scores = []
        self.load_scores()

    def show_top_scores(self):
        self.create_file_if_not_exist('scores.txt')

        self.scores.sort(key=lambda x: int(x[1]), reverse=True)  # Sort by points which is the second element

        print("\nTop Scores:")
        for i, score in enumerate(self.scores[:10]):
            print(f"{i + 1}. User: {score[0]}, Points: {score[1]}, Stages Won: {score[2]}")

    def record_score(self, username, points, stages):
        self.scores.append([username, str(points), str(stages)])
        self.save_scores()
        print("Score recorded.")

    def load_scores(self):
        self.create_file_if_not_exist('scores.txt')

        with open('scores.txt', 'r') as f:
            self.scores = [line.strip().split(",") for line in f.readlines()]

    def save_scores(self):
        with open('scores.txt', 'w') as f:
            for score in self.scores:
                f.write(",".join(score) + "\n")

    def create_file_if_not_exist(self, filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                pass