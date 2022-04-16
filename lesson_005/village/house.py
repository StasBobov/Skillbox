
import pygame

def wall(screen):
    x = -150
    y = -51

    for j in range(12): # Обозначиваем ряд
        y += 50
        if x == 1150:
            x = -100
        else:
            x = -150
        for i in range(13): # Рисуем кирпич
            x += 100
            pygame.draw.rect(screen, (244, 164, 96), (x, y, 100, 50), 2)