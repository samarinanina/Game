import pygame
from pygame.sprite import Sprite


class Life(Sprite):
    """инициализация жизни"""

    def __init__(self, screen):
        super(Life, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images_text/life.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center = float(self.rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        self.screen.blit(self.image, self.rect)  # отрисовка