import scr.controls
import pygame
from scr.config import const


def faces_check(stats, screen, scores, rabbit, faces, carrots):
    """проверка, что лица дошли до низа экрана"""
    screen_rect = screen.get_rect()
    for face in faces.sprites():
        if face.rect.bottom >= screen_rect.bottom:
            scr.controls.lost_life(stats, screen, scores, rabbit, faces, carrots)
            break

def check_record(stats, scores, screen):
    if stats.score > stats.best_score:
        stats.best_score = stats.score
        scores.image_best_score()
        with open("scr/images_text/best_score.txt", 'w') as f:
            f.write(str(stats.best_score))
        scores.show_score()
        if const.new_record:
            rec_surf = pygame.image.load("scr/images_text/record.png")
            rec_rect = rec_surf.get_rect(center=(const.record_position))
            screen.blit(rec_surf, rec_rect)
            pygame.display.update()
            pygame.time.delay(const.record_time)
            const.new_record = False
