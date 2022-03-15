# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.color import THECOLORS
import random

pygame.init()

screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

random_balls = []
for _ in range(100):
    x = random.randrange(0, 1200)
    y = random.randrange(0, 600)
    random_balls.append((x, y))
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# Нарисовать 10 пузырьков в ряд
# Нарисовать три ряда по 10 пузырьков
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    center = (200, 200)
    radius = 50
    for i in range(6):
        radius += 10
        pygame.draw.circle(screen, THECOLORS['red'], center, radius, width=2)

    for j in range(200, 701, 50):
        for k in range(400, 461, 30):
            pygame.draw.circle(screen, THECOLORS['blue'], (j, k), 50, width=2)

    for _ in random_balls:
        pygame.draw.circle(screen, THECOLORS['blue'], (_[0], _[1]), 40, width=3)


    pygame.display.update()
    clock.tick(60)





