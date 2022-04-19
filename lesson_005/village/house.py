
import pygame

yellow = (255, 255, 0)
blue = (0, 0, 255)

def wall(screen, x1, y1):
    x = x1
    y = y1

    for j in range(5): # Обозначиваем ряд
        y += 20
        x = x1
        for i in range(10): # Рисуем кирпич
            x += 40
            pygame.draw.rect(screen, (244, 164, 96), (x, y, 40, 20), 2)
        y += 20
        x = 400
        pygame.draw.rect(screen, (244, 164, 96), (x, y, 20, 20), 2)
        x = 380
        for i in range(9): # Рисуем кирпич
            x += 40
            pygame.draw.rect(screen, (244, 164, 96), (x, y, 40, 20), 2)
        pygame.draw.rect(screen, (244, 164, 96), (x+40, y, 20, 20), 2)


def smile(screen, j):
    pygame.draw.circle(screen, yellow, (j[0], j[1]), 50)
    pygame.draw.circle(screen, blue, ((j[0]) - 15, (j[1] - 8)), 5, 1)
    pygame.draw.circle(screen, blue, ((j[0]) + 15, (j[1] - 8)), 5, 1)
    pygame.draw.arc(screen, blue, ((j[0]) - 25, (j[1] - 20), 50, 50),
                    3.14, 2 * 3.14, 1)
