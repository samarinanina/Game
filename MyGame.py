import pygame, pygame_menu
import controls

from rabbit import Rabbit
from pygame.sprite import Group
from stats import Stats
from scores import Scores

pygame.init()
screen = pygame.display.set_mode([600, 500])
pygame.display.set_caption("Cool Bunny")
bg_color = (250, 204, 190)
rabbit = Rabbit(screen)
carrots = Group()
faces = Group()
controls.create_army(screen, faces, False)
stats = Stats()
scores = Scores(screen, stats)


def run():
    while True:
        controls.events(screen, rabbit, carrots)
        if stats.run_game:
            rabbit.update_rabbit()
            controls.update_screen(bg_color, rabbit, screen, stats, scores, faces, carrots)
            controls.update_carrots(screen, faces, carrots, stats, scores)
            controls.update_faces(stats, screen, scores, rabbit, faces, carrots)


menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_SOLARIZED)
table = menu.add.table(table_id='my_table', font_size=20)
table.add_row(['Reсord :', stats.best_score])
menu.add.button('Play', run)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)


