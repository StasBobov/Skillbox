# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код

import pygame
import sys
from village import nature, house
import time

x = 360
y = 380

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    nature.snowfall(screen)
    house.wall(screen, x, y)
    house.window(screen, x, y)
    house.smile_see(screen, (x+310, y+115))
    nature.draw_branches(screen, (1000, 600), 35, 40)
    nature.draw_branches(screen, (100, 600), 35, 40)
    nature.draw_branches(screen, (350, 600), 35, 40)
    nature.rainbow_oval(screen, 745, 645, 800)
    nature.sun(screen)
    print('оборот')




    time.sleep(0.2)
    pygame.display.update()
    clock.tick(60)




# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
