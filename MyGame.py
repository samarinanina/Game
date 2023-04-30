import pygame, pygame_menu
import scr.controls
import scr.update

from scr.rabbit import Rabbit
from pygame.sprite import Group
from scr.stats import Stats
from scr.scores import Scores

pygame.init()
screen = pygame.display.set_mode([600, 500])
pygame.display.set_caption("Cool Bunny")
bg_color = (250, 204, 190)
rabbit = Rabbit(screen)
carrots = Group()
faces = Group()
scr.controls.create_army(screen, faces, False)
stats = Stats()
scores = Scores(screen, stats)


def run():
    while True:
        scr.controls.events(screen, rabbit, carrots)
        if stats.run_game:
            rabbit.update_rabbit()
            scr.update.update_screen(bg_color, rabbit, screen, stats, scores, faces, carrots)
            scr.update.update_carrots(screen, faces, carrots, stats, scores)
            scr.update.update_faces(stats, screen, scores, rabbit, faces, carrots)


menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_SOLARIZED)
table = menu.add.table(table_id='my_table', font_size=20)
table.add_row(['Reсord :', stats.best_score])
menu.add.button('Play', run)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
