class Stats():
    """статистика"""
    def __init__(self):
        """инициализация статистики"""
        self.reset_stats()
        self.run_game = True
        with open("../best_score.txt", 'r') as f:
            self.best_score = int(f.readline())
    def reset_stats(self):
        """изменение статистики во время игры"""
        self.lives_left = 3
        self.score = 0
