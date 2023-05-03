import pygame
from pygame.sprite import Sprite
from scr.config import const

class Rabbit(Sprite):
    """инициализация кролика"""

    def __init__(self, screen):
        super(Rabbit, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("scr/images_text/main_hero.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center = float(self.rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        self.screen.blit(self.image, self.rect)  # отрисовка

    def update_rabbit(self):
        """ обновление позиции кролика"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += const.rabbit_speed
        elif self.mleft and self.rect.left > 0:
            self.center -= const.rabbit_speed

        self.rect.centerx = self.center

    def create_rabbit(self):
        """размещает кролика внизу по центру после того, как его убили"""
        self.center = self.screen_rect.centerx
