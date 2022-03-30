# -*- coding: utf-8 -*-




# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


import pygame
import sys
import math


choice_color = int(input('Выберете цвет фигур \n Красный - 1 \n Оранженый - 2 \n Жёлтый - 3 '
              '\n Зелёный - 4 \n Голубой - 5 \n Синий - 6 \n Фиолетовый - 7 \n Белый - 8 \n '))

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

def triangle(start_point, length, angle, color, screen=screen,):
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
        pygame.draw.line(screen, color, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 120

def kvadrat(start_point, length, angle,color, screen=screen,):
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
        pygame.draw.line(screen, color, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 90


def five(start_point, length, angle, color, screen=screen,):
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
        pygame.draw.line(screen, color, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 72

def six(start_point, length, angle,color, screen=screen,):
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
        pygame.draw.line(screen, color, point_0, end_point, 3)
        point_0 = end_point
        new_angle += 60

pygame.init()

screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if choice_color == 1:
        color = red
    elif choice_color == 2:
        color = orange
    elif choice_color == 3:
        color = yellow
    elif choice_color == 4:
        color = green
    elif choice_color == 5:
        color = cyan
    elif choice_color == 6:
        color = blue
    elif choice_color == 7:
        color = purple
    elif choice_color == 8:
        color = white
    else:
        print('Вы ввели недопустимое значение, запустите программу снова.')
        pygame.quit()
        sys.exit()


    triangle(start_point=[300, 250], color=color, length=200, angle=90)
    kvadrat(start_point=[600, 300], color=color, length=200, angle=60)
    five(start_point=[900, 300], color=color, length=150, angle=0)
    six(start_point=[350, 500], color=color, length=120, angle=0)

    pygame.display.update()
    clock.tick(60)
