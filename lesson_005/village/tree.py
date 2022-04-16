
import pygame
import math
import random

green = (0, 128, 0)
sienna = (160, 82, 45)

def first_tree(point_0):
    direction = (90 * math.pi) / 180
    dx = math.cos(direction) * 200
    dy = math.sin(direction) * 200
    end_point = (point_0[0] + dx, (point_0[1] - dy))
    pygame.draw.line(screen, sienna, point_0, end_point, 4)
    return end_point

def other_branches(start_point, angle, length, first_length):
    direction = (random.randint(12, 75) * math.pi) / 180
    dx = math.cos(direction) * length
    dy = math.sin(direction) * length
    end_pointr = (start_point[0] + dx, (start_point[1] - dy))
    end_pointl = (start_point[0] - dx, (start_point[1] - dy))
    pygame.draw.line(screen, green, start_point, end_pointr, 3)
    pygame.draw.line(screen, green, start_point, end_pointl, 3)
    # if angle <= -180:
    #     angle = 165
    # elif -180 < angle:
    #     angle = angle - 15
    length = first_length * (random.randint(8, 12) / 10) * 0.75
    print(length)
    return [end_pointr, end_pointl, angle, length]