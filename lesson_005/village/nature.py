
import pygame
import math
import random
import time

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (128, 0, 128)
white = (255, 255, 255)
navy = (0, 0, 128)
green = (0, 128, 0)
sienna = (160, 82, 45)

N = 20
x_list = [random.randint(0, 1200) for i in range(N)]
y_list = [random.randint(0, 100) for j in range(N)]
l_list = [random.randint(10, 30) for k in range(N)]

def rainbow_line(screen):
    rainbow = (red, orange, yellow, green, cyan, blue, purple)
    x1 = 50
    y1 = 50
    x2 = 350
    y2 = 450
    screen.fill((255, 255, 255))

    for i in rainbow:
        x1 += 5
        x2 += 5
        pygame.draw.line(screen, i, [x1, y1], [x2, y2], 4)

def rainbow_oval(screen):
    rainbow = (red, orange, yellow, green, cyan, blue, purple)
    screen.fill((255, 255, 255))

    xr = 600
    yr = 1250

    for i in rainbow:
        yr -= 5
        pygame.draw.circle(screen, i, [xr, yr], 900, 4)

def first_tree(screen, point_0):
    direction = (90 * math.pi) / 180
    dx = math.cos(direction) * 200
    dy = math.sin(direction) * 200
    end_point = (point_0[0] + dx, (point_0[1] - dy))
    pygame.draw.line(screen, sienna, point_0, end_point, 4)
    return end_point

def other_branches(screen, start_point, angle, length):
    direction = (angle * math.pi) / 180
    dx = math.cos(direction) * length
    dy = math.sin(direction) * length
    end_pointr = (start_point[0] + dx, (start_point[1] - dy))
    end_pointl = (start_point[0] - dx, (start_point[1] - dy))
    pygame.draw.line(screen, green, start_point, end_pointr, 3)
    pygame.draw.line(screen, green, start_point, end_pointl, 3)
    if angle <= -180:
        angle = 165
    elif -180 < angle:
        angle = angle - 15
    length = length * 0.75
    return [end_pointr, end_pointl, angle, length]

def draw_branches(screen, point_0, angle, length, trunk=0, start_point=[0, 0]):
    if length < 10:
        return
    if trunk == 0:
        start_point = first_tree(screen, point_0)
        trunk = 1
    results = other_branches(screen, start_point, angle, length)
    start_pointr = results[0]
    start_pointl = results[1]
    angle = results[2]
    length = results[3]
    draw_branches(screen, start_pointr, angle, length, trunk, start_pointr)
    draw_branches(screen, start_pointl, angle, length, trunk, start_pointl)

def snowflake(screen, center, length, color=white):
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

def snowfall(screen, x_list=x_list, y_list=y_list, l_list=l_list, snowdriftx = [], snowdrifty = [], snowdriftl = []):
    screen.fill(navy)
    for i in range(N):
        x = x_list[i]
        y = y_list[i]
        l = l_list[i]
        snowflake(screen, center=(x, y), length=l)

    for i in range(N):
        if y_list[i] >= 600 - l_list[i]:
            if 0 + l_list[i] <= x_list[i] <= 1200 - l_list[i]:
                snowdriftx.append(x_list.pop(i))
                snowdrifty.append(y_list.pop(i))
                snowdriftl.append(l_list.pop(i))
                x_list.append(random.randint(0, 1200))
                y_list.append(random.randint(0, 100))
                l_list.append(random.randint(10, 30))
        else:
            x_list[i] = x_list[i] * random.randint(9, 11) / 10
            y_list[i] = y_list[i] + 10


        for j in range(len(snowdriftx)):
            snowflake(screen, center=(snowdriftx[j], snowdrifty[j]), length=snowdriftl[j])

        if x_list == True:
            snowfall(screen, x_list, y_list, l_list, snowdriftx, snowdrifty, snowdriftl)


