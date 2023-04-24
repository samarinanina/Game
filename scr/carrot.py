import pygame


class Carrot(pygame.sprite.Sprite):
    """инициализация моркови"""

    def __init__(self, screen, rabbit):
        super(Carrot, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("carrot.png")
        self.rect = self.image.get_rect()
        self.speed = 2.5
        self.rect.centerx = rabbit.rect.centerx
        self.rect.top = rabbit.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение моркови вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_carrot(self):
        """прорисовка моркови"""
        self.screen.blit(self.image, self.rect)
