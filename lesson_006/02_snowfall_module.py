# -*- coding: utf-8 -*-



# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)

import pygame
import snowfall
import sys
import time
from termcolor import cprint, colored


colors = {1: (255, 0, 0), 2: (255, 165, 0), 3: (255, 255, 0), 4: (0, 128, 0), 5: (0, 255, 255), 6: (0, 0, 255),
          7: (128, 0, 128), 8: (255, 255, 255), 9: (255, 215, 0), 10: (0, 0, 0)}


white = (255, 255, 255)

gold = (255, 215, 0)
black = (0, 0, 0)


program_color = 'blue'



cprint('ДАВАЙ НАРИСУЕМ СНЕГОПАД! \n', color=program_color)
time.sleep(1)
count = input(colored('Сколько снежинок будем рисовать? \n ', color=program_color))
time.sleep(1)
snow_color = input(colored('Какого цвета будут снежинки? \n 1 - Красный \n 2 - Оранжевый \n 3 - Жёлтый \n 4 - Зелёный \n 5 - Голубой \n'
       '6 - Синий \n 7 - Фиолетовый \n 8 - Белый \n 9 - Золотой \n 10 - Чёрный \n', color=program_color))


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snowfall.move('left', screen, color=colors[int(snow_color)])
            if event.key == pygame.K_RIGHT:
                snowfall.move('right', screen, color=colors[int(snow_color)])
            if event.key == pygame.K_DOWN:
                snowfall.move('down', screen, color=colors[int(snow_color)])


    snowfall.let_it_snow(screen, int(count), color=colors[int(snow_color)])
    snowfall.under()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    time.sleep(0.1)
    pygame.display.update()
    clock.tick(60)


