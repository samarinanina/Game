import pygame
import sys
import pygame_menu

from scr.carrot import Carrot
from scr.face import Face
from scr.config import const
import time


def events(screen, rabbit, carrot):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rabbit.mright = True
            elif event.key == pygame.K_LEFT:
                rabbit.mleft = True
            elif event.key == pygame.K_SPACE:
                new_carrot = Carrot(screen, rabbit)
                carrot.add(new_carrot)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rabbit.mright = False
            elif event.key == pygame.K_LEFT:
                rabbit.mleft = False


def create_army(screen, faces, number):
    """создание армии недовольных лиц"""
    face = Face(screen)
    const.check += const.check_speed
    face_width = face.rect.width
    face_height = face.rect.height
    number_face_x = int((const.height - 2 * face_width) / face_width)
    number_face_y = int((const.width - const.height / 2 - 2 * face_height) / face_height)

    for row_number in range(number_face_y):
        for face_number in range(number_face_x):
            face = Face(screen)
            faces.add(face)
            face.x = face_width * (face_number + 1)
            face.y = face_height * (row_number + 1)
            face.rect.x = face.x
            face.rect.y = face.rect.height * (1 + row_number)
            face.change_speed()


def lost_life(stats, screen, scores, rabbit, faces, carrots):
    """потеря одной жизни при столкновении с лицами"""

    if stats.lives_left > const.min_life:
        stats.lives_left -= const.min_life
        scores.image_lives()
        faces.empty()
        carrots.empty()
        create_army(screen, faces, False)
        rabbit.create_rabbit()
        const.check -= const.check_speed
        time.sleep(const.sec_stop)
    else:
        const.new_record = True
        const.check = const.check_speed
        import MyGame
        sys.exit()
