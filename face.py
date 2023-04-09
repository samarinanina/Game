import pygame

class Face(pygame.sprite.Sprite):
    """класс одного недовольного лица"""

    def __init__(self, screen):
        super(Face, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("../image/face.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.02

    def draw(self):
        """прорисовка лица"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def change_speed(self):
        self.speed += 0.02


