# -*- coding: utf-8 -*-



# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
import sys
import time
from random import randint
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 600))
gold = (255, 215, 0)
black = (0, 0, 0)
colors = {1: (255, 0, 0), 2: (255, 165, 0), 3: (255, 255, 0), 4: (0, 128, 0), 5: (0, 255, 255), 6: (0, 0, 255),
          7: (128, 0, 128), 8: (255, 255, 255), 9: (255, 215, 0), 10: (0, 0, 0)}
clock = pygame.time.Clock()
direction = 0
we_are_fall = []
forget_about_us = []

class Snowflake:

    def __init__(self, screen, center, length, color):
        self.screen = screen
        self.center = center
        self.length = length
        self.color = color

    def draw(self):
        '''Отрисовка снежинки'''
        # Основные лучики
        pygame.draw.line(self.screen, self.color, (self.center[0] - self.length, self.center[1]), (self.center[0] + self.length, self.center[1]), 1)
        pygame.draw.line(self.screen, self.color, (self.center[0] - (self.length * 0.792), self.center[1] - (self.length * 0.792)),
                         (self.center[0] + (self.length * 0.792), self.center[1] + (self.length * 0.792)), 1)
        pygame.draw.line(self.screen, self.color, (self.center[0] + (self.length * 0.792), self.center[1] - (self.length * 0.792)),
                         (self.center[0] - (self.length * 0.792), self.center[1] + (self.length * 0.792)), 1)
        # дополнительные лучики
        pygame.draw.line(self.screen, self.color, (self.center[0] + (self.length * 0.7), self.center[1]),
                         (self.center[0] + (self.length * 0.9), self.center[1] - (self.length * 0.15)), 1)
        pygame.draw.line(self.screen, self.color, (self.center[0] + (self.length * 0.7), self.center[1]),
                         (self.center[0] + (self.length * 0.9), self.center[1] + (self.length * 0.15)), 1)

        pygame.draw.line(self.screen, self.color, (self.center[0] - (self.length * 0.7), self.center[1]),
                         (self.center[0] - (self.length * 0.9), self.center[1] - (self.length * 0.15)), 1)
        pygame.draw.line(self.screen, self.color, (self.center[0] - (self.length * 0.7), self.center[1]),
                         (self.center[0] - (self.length * 0.9), self.center[1] + (self.length * 0.15)), 1)

        pygame.draw.line(self.screen, self.color, (self.center[0] - (self.length * 0.7), self.center[1]),
                         (self.center[0] - (self.length * 0.9), self.center[1] - (self.length * 0.15)), 1)
        pygame.draw.line(self.screen, self.color, (self.center[0] - (self.length * 0.7), self.center[1]),
                         (self.center[0] - (self.length * 0.9), self.center[1] + (self.length * 0.15)), 1)

        pygame.draw.line(self.screen, self.color, (self.center[0] - (self.length * 0.6), self.center[1] - (self.length * 0.6)),
                         (self.center[0] - (self.length * 0.6), self.center[1] - (self.length * 0.83)), 1)
        pygame.draw.line(self.screen, self.color, (self.center[0] - (self.length * 0.6), self.center[1] - (self.length * 0.6)),
                         (self.center[0] - (self.length * 0.85), self.center[1] - (self.length * 0.6)), 1)

        pygame.draw.line(self.screen, self.color, (self.center[0] + (self.length * 0.6), self.center[1] - (self.length * 0.6)),
                         (self.center[0] + (self.length * 0.6), self.center[1] - (self.length * 0.83)), 1)
        pygame.draw.line(self.screen, self.color, (self.center[0] + (self.length * 0.6), self.center[1] - (self.length * 0.6)),
                         (self.center[0] + (self.length * 0.85), self.center[1] - (self.length * 0.6)), 1)

        pygame.draw.line(self.screen, self.color, (self.center[0] - (self.length * 0.6), self.center[1] + (self.length * 0.6)),
                         (self.center[0] - (self.length * 0.6), self.center[1] + (self.length * 0.83)), 1)
        pygame.draw.line(self.screen, self.color, (self.center[0] - (self.length * 0.6), self.center[1] + (self.length * 0.6)),
                         (self.center[0] - (self.length * 0.85), self.center[1] + (self.length * 0.6)), 1)

        pygame.draw.line(self.screen, self.color, (self.center[0] + (self.length * 0.6), self.center[1] + (self.length * 0.6)),
                         (self.center[0] + (self.length * 0.6), self.center[1] + (self.length * 0.83)), 1)
        pygame.draw.line(self.screen, self.color, (self.center[0] + (self.length * 0.6), self.center[1] + (self.length * 0.6)),
                         (self.center[0] + (self.length * 0.85), self.center[1] + (self.length * 0.6)), 1)

    def move(self, dir):
        if dir != 0:
            if dir == 'left':
                self.center[0] -= 10
            if dir == 'right':
                self.center[0] += 10
            if dir == 'down':
                self.center[1] += 5

    def is_down(self):
        if self.center[1] >= 600 - self.length*1:
            forget_about_us.append(self)
            flakes.remove(self)
            we_are_fall.append(1)
            print('Уже упало {0} снежинок'.format(len(forget_about_us)))


# Функция делает список со снежинками
def get_flakes(count):
    flake = []
    for i in range(count):
        flake.append(Snowflake(screen=screen, center=[randint(0, 1200), randint(0, 100)], length=randint(10, 30), color= colors[randint(1, 10)]))
    return flake

def append_flakes(count):
    global flakes, we_are_fall
    for i in range(count):
        flakes.append(Snowflake(screen=screen, center=[randint(0, 1200), randint(0, 100)], length=randint(10, 30),
                               color=colors[randint(1, 10)]))



flakes = get_flakes(count=20)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'left'
            if event.key == pygame.K_RIGHT:
                direction = 'right'
            if event.key == pygame.K_DOWN:
                direction = 'down'
        else:
            direction = 0
    screen.fill(black)
    for flake in flakes:
        flake.is_down()
        flake.move(direction)
        flake.draw()
    for flake in forget_about_us:
        flake.draw()
    if we_are_fall != []:
        append_flakes(count=len(we_are_fall))
    we_are_fall = []
    time.sleep(0.1)
    pygame.display.update()
    clock.tick(60)

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


