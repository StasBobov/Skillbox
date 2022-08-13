# -*- coding: utf-8 -*-

import pygame
import sys
import math

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg



screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (128, 0, 128)
white = (255, 255, 255)

def triangle(start_point, length, angle, screen=screen,):
    # Хуй знает как оно работает, но делает углы
    point_0 = start_point
    direction = (angle * math.pi) / 180
    dx = math.cos(direction) * length
    dy = math.sin(direction) * length
    new_angle = angle
    for i in range(3):
        direction = (new_angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_point = (point_0[0] + dx, (point_0[1] - dy))
        pygame.draw.line(screen, white, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 120

def kvadrat(start_point, length, angle, screen=screen,):
    # Хуй знает как оно работает, но делает углы
    point_0 = start_point
    direction = (angle * math.pi) / 180
    dx = math.cos(direction) * length
    dy = math.sin(direction) * length
    new_angle = angle
    for i in range(4):
        direction = (new_angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_point = (point_0[0] + dx, (point_0[1] - dy))
        pygame.draw.line(screen, white, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 90


def five(start_point, length, angle, screen=screen,):
    # Хуй знает как оно работает, но делает углы
    point_0 = start_point
    direction = (angle * math.pi) / 180
    dx = math.cos(direction) * length
    dy = math.sin(direction) * length
    new_angle = angle
    for i in range(5):
        direction = (new_angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_point = (point_0[0] + dx, (point_0[1] - dy))
        pygame.draw.line(screen, white, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 72

def six(start_point, length, angle, screen=screen,):
    # Хуй знает как оно работает, но делает углы
    point_0 = start_point
    direction = (angle * math.pi) / 180
    dx = math.cos(direction) * length
    dy = math.sin(direction) * length
    new_angle = angle
    for i in range(6):
        direction = (new_angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_point = (point_0[0] + dx, (point_0[1] - dy))
        pygame.draw.line(screen, white, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 60


pygame.init()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    # pygame.draw.line(screen, white, [0, 0], [200, 200], 3)
    triangle(start_point=[300, 250], length=200, angle=90)
    kvadrat(start_point=[600, 300], length=200, angle=60)
    five(start_point=[900, 300], length=150, angle=0)
    six(start_point=[350, 500], length=120, angle=0)

    pygame.display.update()
    clock.tick(60)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
