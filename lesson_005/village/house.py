
import pygame

yellow = (255, 255, 0)
blue = (0, 0, 255)

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

def smile(screen, j):
    pygame.draw.circle(screen, yellow, (j[0], j[1]), 50)
    pygame.draw.circle(screen, blue, ((j[0]) - 15, (j[1] - 8)), 5, 1)
    pygame.draw.circle(screen, blue, ((j[0]) + 15, (j[1] - 8)), 5, 1)
    pygame.draw.arc(screen, blue, ((j[0]) - 25, (j[1] - 20), 50, 50),
                    3.14, 2 * 3.14, 1)
