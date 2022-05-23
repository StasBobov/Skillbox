
from random import randint
import pygame
from termcolor import cprint, colored

lightskyblue = (135, 206, 250)
white = (255, 255, 255)
blue = 'blue'

def snowflake(screen, color, center, length):
    '''Отрисовка снежинки'''
    # Основные лучики
    pygame.draw.line(screen, color, (center[0] - length, center[1]), (center[0] + length, center[1]), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.792), center[1] - (length * 0.792)),
                     (center[0] + (length * 0.792), center[1] + (length * 0.792)), 1)
    pygame.draw.line(screen, color, (center[0] + (length * 0.792), center[1] - (length * 0.792)),
                     (center[0] - (length * 0.792), center[1] + (length * 0.792)), 1)
    # дополнительные лучики
    pygame.draw.line(screen, color, (center[0] + (length * 0.7), center[1]),
                     (center[0] + (length * 0.9), center[1] - (length * 0.15)), 1)
    pygame.draw.line(screen, color, (center[0] + (length * 0.7), center[1]),
                     (center[0] + (length * 0.9), center[1] + (length * 0.15)), 1)

    pygame.draw.line(screen, color, (center[0] - (length * 0.7), center[1]),
                     (center[0] - (length * 0.9), center[1] - (length * 0.15)), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.7), center[1]),
                     (center[0] - (length * 0.9), center[1] + (length * 0.15)), 1)

    pygame.draw.line(screen, color, (center[0] - (length * 0.7), center[1]),
                     (center[0] - (length * 0.9), center[1] - (length * 0.15)), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.7), center[1]),
                     (center[0] - (length * 0.9), center[1] + (length * 0.15)), 1)

    pygame.draw.line(screen, color, (center[0] - (length * 0.6), center[1] - (length * 0.6)),
                     (center[0] - (length * 0.6), center[1] - (length * 0.83)), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.6), center[1] - (length * 0.6)),
                     (center[0] - (length * 0.85), center[1] - (length * 0.6)), 1)

    pygame.draw.line(screen, color, (center[0] + (length * 0.6), center[1] - (length * 0.6)),
                     (center[0] + (length * 0.6), center[1] - (length * 0.83)), 1)
    pygame.draw.line(screen, color, (center[0] + (length * 0.6), center[1] - (length * 0.6)),
                     (center[0] + (length * 0.85), center[1] - (length * 0.6)), 1)

    pygame.draw.line(screen, color, (center[0] - (length * 0.6), center[1] + (length * 0.6)),
                     (center[0] - (length * 0.6), center[1] + (length * 0.83)), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.6), center[1] + (length * 0.6)),
                     (center[0] - (length * 0.85), center[1] + (length * 0.6)), 1)

    pygame.draw.line(screen, color, (center[0] + (length * 0.6), center[1] + (length * 0.6)),
                     (center[0] + (length * 0.6), center[1] + (length * 0.83)), 1)
    pygame.draw.line(screen, color, (center[0] + (length * 0.6), center[1] + (length * 0.6)),
                     (center[0] + (length * 0.85), center[1] + (length * 0.6)), 1)


# Координаты и размеры снежинок в воздухе
x_list = []
y_list = []
l_list = []
falling_snowflakes = {} # Список номеров снежинок на полу
a = 0 # Счётчик для запуска действий когда снежинка(и) на полу
b = 0 # Счётчик для первого запуска создания снежинок

def let_it_snow(screen, N, color):
    screen.fill(lightskyblue)
    global x_list, y_list, l_list, falling_snowflakes, b, new
    if b == 0:
        x_list = [randint(0, 1200) for i in range(N)]
        y_list = [randint(0, 100) for j in range(N)]
        l_list = [randint(10, 30) for k in range(N)]
        b = 1
    # рисуем снежинки, которые в воздухе
    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        l = l_list[i]
        snowflake(screen, color, center=(x, y), length=l)
    # рисуем снежинки, которые на полу
    if falling_snowflakes != {}:
        for i in falling_snowflakes.values():
            snowflake(screen, color, center=(i[0], i[1]), length=i[2])


def move(direction, screen, color):
    '''Движение снежинки'''
    global x_list, y_list, l_list, snowdriftx, snowdrifty, snowdriftl
    if direction == 'left':
        for i in range(len(x_list)):
            x_list[i] = x_list[i] - 10
            snowflake(screen, color, center=(x_list[i], y_list[i]), length=l_list[i])
    if direction == 'right':
        for i in range(len(x_list)):
            x_list[i] = x_list[i] + 10
            snowflake(screen, color, center=(x_list[i], y_list[i]), length=l_list[i])
    if direction == 'down':
        for i in range(len(y_list)):
            y_list[i] = y_list[i] + 10
            snowflake(screen, color, center=(x_list[i], y_list[i]), length=l_list[i])

def under():
    '''Проверка на нахождение снежинки на полу'''
    global y_list, falling_snowflakes, a
    for i in range(len(y_list)):
        if y_list[i] >= 600:
                # Словарь с координатами снежинок на земле
                falling_snowflakes[i] = [x_list[i], y_list[i], l_list[i]]
                a = 1

    if a == 1:
        action()

def action():
    '''Действия с упавшими снежниками'''
    global x_list,y_list, l_list, falling_snowflakes, a, b, new
    f_s = list(falling_snowflakes.keys())
    cprint("У нас есть упавшие снежинки {0}".format(f_s), color=blue)
    act = input(colored(' Что будем делать? \n 1 - удалить снежинки \n '
                        '2 - добавить ещё снежинок \n 3 - и так сойдёт...\n ', color=blue))
    if act == '1':
        for i in falling_snowflakes.values():
            if i[0] in x_list:
                x_list.remove(i[0])
                y_list.remove(i[1])
                l_list.remove(i[2])
        falling_snowflakes.clear()
    elif act == '2':
        new = input(colored("Сколько снежинок добавим? ", color=blue))
        for i in range (int(new)):
            x_list.append(randint(0, 1200))
            y_list.append(randint(0, 100))
            l_list.append(randint(10, 30))
        for i in falling_snowflakes.values():
            if i[0] in x_list:
                x_list.remove(i[0])
                y_list.remove(i[1])
                l_list.remove(i[2])
        new = 0
    else:
        for i in falling_snowflakes.values():
            if i[0] in x_list:
                x_list.remove(i[0])
                y_list.remove(i[1])
                l_list.remove(i[2])
    a = 0









