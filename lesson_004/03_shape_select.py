# -*- coding: utf-8 -*-


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

import pygame
import sys
import math


choice_figure = int(input('Выберете фигуру \n Треугольник - 1 \n Квадрат - 2 \n Пятиугольник - 3 '
              '\n Шестиугольник - 4 \n '))

screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

center = [(1200/2-100), (600/2+100)]

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (128, 0, 128)
white = (255, 255, 255)

def triangle(length, angle, color=white, screen=screen, start_point=center):
    # Хуй знает как оно работает, но делает углы
    point_0 = start_point
    new_angle = angle
    for i in range(3):
        direction = (new_angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_point = (point_0[0] + dx, (point_0[1] - dy))
        pygame.draw.line(screen, color, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 120

def kvadrat(length, angle,color=white, screen=screen, start_point=center):
    # Хуй знает как оно работает, но делает углы
    point_0 = start_point
    new_angle = angle
    for i in range(4):
        direction = (new_angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_point = (point_0[0] + dx, (point_0[1] - dy))
        pygame.draw.line(screen, color, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 90


def five(length, angle, color=white, screen=screen, start_point=center):
    # Хуй знает как оно работает, но делает углы
    point_0 = start_point
    new_angle = angle
    for i in range(5):
        direction = (new_angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_point = (point_0[0] + dx, (point_0[1] - dy))
        pygame.draw.line(screen, color, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 72

def six(length, angle, color=white, screen=screen, start_point=center):
    # Хуй знает как оно работает, но делает углы
    point_0 = start_point
    new_angle = angle
    for i in range(6):
        direction = (new_angle * math.pi) / 180
        dx = math.cos(direction) * length
        dy = math.sin(direction) * length
        end_point = (point_0[0] + dx, (point_0[1] - dy))
        pygame.draw.line(screen, color, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 60

pygame.init()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if choice_figure == 1:
        triangle(length=200, angle=0)
    elif choice_figure == 2:
        kvadrat(length=200, angle=0)
    elif choice_figure == 3:
        five(length=150, angle=0)
    elif choice_figure == 4:
        six(length=120, angle=0)
    else:
        print('Вы ввели недопустимое значение, запустите программу снова.')
        pygame.quit()
        sys.exit()


    pygame.display.update()
    clock.tick(60)


