
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


# x_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# y_list = [629, 576, 595, 611, 629, 568, 572, 579, 600, 603]
# l_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Координаты и размеры снежинок в воздухе
x_list = []
y_list = []
l_list = []
# Координаты и размеры снежинок на полу
snowdriftx = []
snowdrifty = []
snowdriftl = []
falling_snowflakes = [] # Список номеров снежинок на полу
a = 0 # Счётчик для запуска действий когда снежинка(и) на полу
b = 0 # Счётчик для первого запуска создания снежинок
new = 0


def let_it_snow(screen, N, color):
    screen.fill(lightskyblue)
    global x_list, y_list, l_list, snowdriftx, snowdrifty, snowdriftl, b, new
    if b == 0:
        x_list = [randint(0, 1200) for i in range(N)]
        y_list = [randint(0, 100) for j in range(N)]
        l_list = [randint(10, 30) for k in range(N)]
        b = 1
    elif b == 2:
        for i in range(new):
            x_list.append(randint(0, 1200))
            y_list.append(randint(0, 100))
            l_list.append(randint(10, 30))
        new = 0
        b = 1
    # рисуем снежинки, которые в воздухе
    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        l = l_list[i]
        snowflake(screen, color, center=(x, y), length=l)
    if snowdriftx != []:
        for i in range(len(snowdriftx)):
            x = snowdriftx[i]
            y = snowdrifty[i]
            l = snowdriftl[i]
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
    '''Проверка на нахождение снежинки на полу'''
    global y_list, falling_snowflakes, a, snowdriftx, snowdrifty, snowdriftl
    for i in range(len(y_list)):
        if y_list[i] >= 600:
            # Добавляем в отдельные списки упавшие снежинки
            if i+1 not in falling_snowflakes:
                snowdriftx.append(x_list[i])
                snowdrifty.append(y_list[i])
                snowdriftl.append(l_list[i])
                # Список с номерами снежинок на земле
                falling_snowflakes.append(i+1)
                a = 1
    if snowdriftx != []:
        for i in snowdriftx:
            x_list.remove(i)
        for j in snowdrifty:
            y_list.remove(j)
        for k in snowdriftl:
            l_list.remove(k)
    if a == 1:
        action()

def action():
    '''Действия с упавшими снежниками'''
    global x_list,y_list, l_list, falling_snowflakes, a, b, new
    cprint("У нас есть упавшие снежинки {0}".format(falling_snowflakes), color=blue)
    act = input(colored(' Что будем делать? \n 1 - удалить снежинки \n '
                        '2 - добавить ещё снежинок \n 3 - и так сойдёт...\n ', color=blue))
    if act == '1':
        snowdriftx.clear(), snowdrifty.clear(), snowdriftl.clear(), falling_snowflakes.clear()
    elif act == '2':
        b = 2
        new = len(falling_snowflakes)
    a = 0


#
# under()








