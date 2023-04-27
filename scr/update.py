import pygame
import check
import controls

def update_screen(bg_color, rabbit, screen, stats, scores, faces, carrot):
    """обновление экрана"""
    screen.fill(bg_color)
    scores.show_score()
    for carrot in carrot.sprites():
        carrot.draw_carrot()
    rabbit.output()  # вывод кролика
    faces.draw(screen)
    pygame.display.flip()

def update_carrots(screen, faces, carrots, stats, scores):
    """ обновляем позицию моркови """
    carrots.update()
    for carrot in carrots.copy():
        if carrot.rect.bottom <= 0:
            carrots.remove(carrot)
    collisions = pygame.sprite.groupcollide(carrots, faces, True, True)
    if collisions:
        for faces in collisions.values():
            stats.score += 10 * len(faces)
        scores.image_score()
        check.check_record(stats, scores)
        scores.image_lives()
    if len(faces) == 0:
        carrots.empty()
        controls.create_army(screen, faces, True)

def update_faces(stats, screen, scores, rabbit, faces, carrots):
    """обновляет позицию лиц"""
    faces.update()
    if pygame.sprite.spritecollideany(rabbit, faces):
        controls.lost_life(stats, screen, scores, rabbit, faces, carrots)
    check.faces_check(stats, screen, scores, rabbit, faces, carrots)