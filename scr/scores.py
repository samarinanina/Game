import pygame.font
from pygame.sprite import Group
from scr.life import Life
from scr.config import const


class Scores():
    """вывод игровой информации"""

    def __init__(self, screen, stats):
        """инициализируем подсчет очкоы"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (const.scores_colour)
        self.font = pygame.font.SysFont(None, const.scores_font_size)
        self.image_score()
        self.image_best_score()
        self.image_lives()

    def image_score(self):
        """преобразует текст счета в изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, const.screen_colour)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - const.position_score[0]
        self.score_rect.top = const.position_score[1]

    def image_best_score(self):
        """преобразует рекорд в изображение"""
        self.best_img = self.font.render(str(self.stats.best_score), True, self.text_color, const.screen_colour)
        self.best_rect = self.best_img.get_rect()
        self.best_rect.centerx = self.screen_rect.centerx
        self.best_rect.top = const.position_best_score

    def image_lives(self):
        """количество оставшихся жизней"""
        self.lives = Group()
        for life in range(self.stats.lives_left):
            live = Life(self.screen)
            live.rect.x = const.position_life[0] + life * live.rect.width
            live.rect.y = const.position_life[1]
            self.lives.add(live)

    def show_score(self):
        """вывод счета и рекорда на экран + количество оставшихся жизней"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.best_img, self.best_rect)
        self.lives.draw(self.screen)
