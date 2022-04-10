# -*- coding: utf-8 -*-




# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок (x, y)
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

import pygame
import sys
import time

white = (255, 255, 255)
navy = (0, 0, 128)

def snowflake(center, length, color=white, factor_a=0.6, factor_b=0.35, factor_c=60):
    # Основные лучики
    pygame.draw.line(screen, color, (center[0] - length, center[1]), (center[0] + length, center[1]), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.792), center[1] - (length * 0.792)), (center[0] + (length * 0.792), center[1] + (length * 0.792)), 1)
    pygame.draw.line(screen, color, (center[0] + (length * 0.792), center[1] - (length * 0.792)), (center[0] - (length * 0.792), center[1] + (length * 0.792)), 1)
    # дополнительные лучики
    pygame.draw.line(screen, color, (center[0] + (length * 0.7), center[1]), (center[0] + (length * 0.9), center[1] - (length * 0.15)), 1)
    pygame.draw.line(screen, color, (center[0] + (length * 0.7), center[1]), (center[0] + (length * 0.9), center[1] + (length * 0.15)), 1)

    pygame.draw.line(screen, color, (center[0] - (length * 0.7), center[1]), (center[0] - (length * 0.9), center[1] - (length * 0.15)), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.7), center[1]), (center[0] - (length * 0.9), center[1] + (length * 0.15)), 1)

    pygame.draw.line(screen, color, (center[0] - (length * 0.7), center[1]), (center[0] - (length * 0.9), center[1] - (length * 0.15)), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.7), center[1]), (center[0] - (length * 0.9), center[1] + (length * 0.15)), 1)

    pygame.draw.line(screen, color, (center[0] - (length * 0.6), center[1] - (length * 0.6)), (center[0] - (length * 0.6), center[1] - (length * 0.83)), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.6), center[1] - (length * 0.6)), (center[0] - (length * 0.85), center[1] - (length * 0.6)), 1)

    pygame.draw.line(screen, color, (center[0] + (length * 0.6), center[1] - (length * 0.6)), (center[0] + (length * 0.6), center[1] - (length * 0.83)), 1)
    pygame.draw.line(screen, color, (center[0] + (length * 0.6), center[1] - (length * 0.6)), (center[0] + (length * 0.85), center[1] - (length * 0.6)), 1)

    pygame.draw.line(screen, color, (center[0] - (length * 0.6), center[1] + (length * 0.6)), (center[0] - (length * 0.6), center[1] + (length * 0.83)), 1)
    pygame.draw.line(screen, color, (center[0] - (length * 0.6), center[1] + (length * 0.6)), (center[0] - (length * 0.85), center[1] + (length * 0.6)), 1)

    pygame.draw.line(screen, color, (center[0] + (length * 0.6), center[1] + (length * 0.6)), (center[0] + (length * 0.6), center[1] + (length * 0.83)), 1)
    pygame.draw.line(screen, color, (center[0] + (length * 0.6), center[1] + (length * 0.6)), (center[0] + (length * 0.85), center[1] + (length * 0.6)), 1)


pygame.init()

screen = pygame.display.set_mode((1200, 600))
screen.fill(navy)
clock = pygame.time.Clock()

y = 0
x = 100
length = 50

while True:
    screen.fill(navy)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if y >= 600 - length:
        y = 600 - length
    if x >= 1200 - length:
        x = 1200 - length
    snowflake(center=(x, y), length=length)
    y += 10
    x = x * 1.1
    time.sleep(0.1)
    pygame.display.update()
    clock.tick(60)


# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


