# -*- coding: utf-8 -*-


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
import sys

import pygame
import math

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (128, 0, 128)
white = (255, 255, 255)

def get_polygon(n):
    screen = pygame.display.set_mode((1200, 600))
    angles = {3: 120, 4: 90, 5: 72, 6: 60}
    if n in angles:
        def paint_figure(start_point, length, angle):
            point_0 = start_point
            direction = (angle * math.pi) / 180
            dx = math.cos(direction) * length
            dy = math.sin(direction) * length
            new_angle = angle
            for i in range(n):
                direction = (new_angle * math.pi) / 180
                dx = math.cos(direction) * length
                dy = math.sin(direction) * length
                end_point = (point_0[0] + dx, (point_0[1] - dy))
                pygame.draw.line(screen, white, point_0, end_point, 3)
                point_0 = end_point
                ang = angles[n]
                new_angle += ang
    else:
        raise ValueError('The program does not support this value of sides {n}')
    return paint_figure

pygame.init()
clock = pygame.time.Clock()

draw_triangle = get_polygon(n=3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    draw_triangle(start_point=(200, 200), angle=60, length=100)
    pygame.display.update()
    clock.tick(60)



