import pygame, pygame_menu
import scr.controls
import scr.update
import scr.config

from scr.rabbit import Rabbit
from pygame.sprite import Group
from scr.stats import Stats
from scr.scores import Scores
from scr.config import const

pygame.init()
screen = pygame.display.set_mode([const.height, const.width])
pygame.display.set_caption(const.name)
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
            scr.update.update_screen(const.screen_colour, rabbit, screen, stats, scores, faces, carrots)
            scr.update.update_carrots(screen, faces, carrots, stats, scores)
            scr.update.update_faces(stats, screen, scores, rabbit, faces, carrots)


menu = pygame_menu.Menu(const.menu_inscription[0],  const.menu[0], const.menu[1], theme=pygame_menu.themes.THEME_SOLARIZED)

table = menu.add.table(table_id=const.menu_inscription[1], font_size=const.table)
table.add_row([const.menu_inscription[2], stats.best_score])
menu.add.button(const.menu_inscription[3], run)
menu.add.button(const.menu_inscription[4], pygame_menu.events.EXIT)

menu.mainloop(screen)
