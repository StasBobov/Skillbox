# -*- coding: utf-8 -*-

# (цикл for)

import pygame
import sys
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()


red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (128, 0, 128)

rainbow = (red, orange, yellow, green, cyan, blue, purple)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    x1 = 50
    y1 = 50
    x2 = 350
    y2 = 450
    screen.fill((255, 255, 255))

    for i in rainbow:
        x1 += 5
        x2 += 5
        pygame.draw.line(screen, i, [x1, y1], [x2, y2], 4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

    xr = 600
    yr = 1250

    for i in rainbow:
        yr -= 5
        pygame.draw.circle(screen, i, [xr, yr], 900, 4)


    pygame.display.update()
    clock.tick(60)

