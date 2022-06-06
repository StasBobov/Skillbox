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
        screen.fill(black)
        if dir == 'left':
            self.center[0] -= 20
        if dir == 'right':
            self.center[0] += 20
        if dir == 'down':
            self.center[1] += 20


    # TODO здесь ваш код

def get_flakes(count):
    flake = []
    for i in range(count):
        flake.append(Snowflake(screen=screen, center=[randint(0, 1200), randint(0, 100)], length=randint(10, 30), color= colors[randint(1, 10)]))
    return flake

flakes = get_flakes(count=20)
flake = Snowflake(screen=screen, center=[500, 50], length=40, color=gold)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            for flake in flakes:
                if event.key == pygame.K_LEFT:
                    flake.move('left')
                if event.key == pygame.K_RIGHT:
                    flake.move('right')
                if event.key == pygame.K_DOWN:
                    flake.move('down')
    flake.draw()
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


