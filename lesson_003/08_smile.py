# -*- coding: utf-8 -*-

# (определение функций)
import pygame
import sys
import random


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

yellow = (255, 255, 0)
blue = (0, 0, 255)

random_smile = []
for i in range(10):
    x = random.randrange(25, 1175)
    y = random.randrange(25, 575)
    random_smile.append((x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    x = random.randrange(25, 1175)
    y = random.randrange(25, 575)

    for j in random_smile:
        pygame.draw.circle(screen, yellow, (j[0], j[1]), 50)
        pygame.draw.circle(screen, blue, ((j[0]) - 15, (j[1] - 8)), 5, 1)
        pygame.draw.circle(screen, blue, ((j[0]) + 15, (j[1] - 8)), 5, 1)
        pygame.draw.arc(screen, blue, ((j[0]) - 25, (j[1] - 20), 50, 50),
                        3.14, 2 * 3.14, 1)



    pygame.display.update()
    clock.tick(60)

