import controls

def faces_check(stats, screen, scores, rabbit, faces, carrots):
    """проверка, что лица дошли до низа экрана"""
    screen_rect = screen.get_rect()
    for face in faces.sprites():
        if face.rect.bottom >= screen_rect.bottom:
            controls.lost_life(stats, screen, scores, rabbit, faces, carrots)
            break

def check_record(stats, scores):
    if stats.score > stats.best_score:
        stats.best_score = stats.score
        scores.image_best_score()
        with open("images_text/best_score.txt", 'w') as f:
            f.write(str(stats.best_score))