# -*- coding: utf-8 -*-

# (цикл for)
import pygame
import sys
from pygame.color import THECOLORS

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

#
pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

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

    pygame.display.update()
    clock.tick(60)


