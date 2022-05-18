
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


x_list = []
y_list = [629, 576, 595, 611, 629, 568, 572, 579, 600, 603]
l_list = []
snowdriftx = []
snowdrifty = []
snowdriftl = []
falling_snowflakes = []


def let_it_snow(screen, N, color):
    screen.fill(lightskyblue)
    global x_list, y_list, l_list, snowdriftx, snowdrifty, snowdriftl
    if len(x_list) == 0:
        if len(l_list) == 0:
            x_list = [randint(0, 1200) for i in range(N)]
            y_list = [randint(0, 100) for j in range(N)]
            l_list = [randint(10, 30) for k in range(N)]
    for i in range(N):
        x = x_list[i]
        y = y_list[i]
        l = l_list[i]
        snowflake(screen, color, center=(x, y), length=l)

    # for i in range(N):
    #     if y_list[i] >= 600 - l_list[i]:
    #         if 0 + l_list[i] <= x_list[i] <= 1200 - l_list[i]:
    #             # добавляем в списки снежинки которые на земле, убирая их из основного списка
    #             snowdriftx.append(x_list.pop(i))
    #             snowdrifty.append(y_list.pop(i))
    #             snowdriftl.append(l_list.pop(i))
    #             # добавляем в основной список новые снежинки, вместо тех, что на земле
    #             x_list.append(randint(0, 1200))
    #             y_list.append(randint(0, 100))
    #             l_list.append(randint(10, 30))
    #     else:
    #         # те, что в воздухе - продолжают кружиться
    #         x_list[i] = x_list[i] * randint(9, 11) / 10
    #         y_list[i] = y_list[i] + 10
    #
    #
    #     for j in range(len(snowdriftx)):
    #         snowflake(screen, color, center=(snowdriftx[j], snowdrifty[j]), length=snowdriftl[j])

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
    global y_list, falling_snowflakes
    for i in range(len(y_list)):
        if y_list[i] >= 600:
            if i not in falling_snowflakes:
                falling_snowflakes.append(i)
    action()

def action():
    global y_list, falling_snowflakes
    act = input(colored('У нас есть упавшие снежинки, что будем делать? \n 1 - удалить снежинки \n '
                        '2 - добавить ещё снежинок \n 3 - и так сойдёт...\n ', color=blue))
    if act == '1':
        # TODO Как-то удалить снежинки
        for i in falling_snowflakes:
            y_list.pop(i)
        falling_snowflakes.clear()
    elif act == '2':
        # TODO Как-то добавить снежинки
        pass


under()








