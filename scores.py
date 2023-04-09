import pygame.font
from pygame.sprite import Group
from life import Life


class Scores():
    """вывод игровой информации"""

    def __init__(self, screen, stats):
        """инициализируем подсчет очкоы"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (60, 60, 30)
        self.font = pygame.font.SysFont(None, 24)
        self.image_score()
        self.image_best_score()
        self.image_lives()

    def image_score(self):
        """преобразует текст счета в изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (250, 204, 190))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_best_score(self):
        """преобразует рекорд в изображение"""
        self.best_img = self.font.render(str(self.stats.best_score), True, self.text_color, (250, 204, 190))
        self.best_rect = self.best_img.get_rect()
        self.best_rect.centerx = self.screen_rect.centerx
        self.best_rect.top = 20

    def image_lives(self):
        """количество оставшихся жизней"""
        self.lives = Group()
        for life in range(self.stats.lives_left):
            live = Life(self.screen)
            live.rect.x = 10 + life * live.rect.width
            live.rect.y = 20
            self.lives.add(live)

    def show_score(self):
        """вывод счета и рекорда на экран + количество оставшихся жизней"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.best_img, self.best_rect)
        self.lives.draw(self.screen)
