# -*- coding: utf-8 -*-
import sys
from random import randint
import sys

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
from termcolor import cprint


class Cat():

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 10

    def __str__(self):
        return '{} сыт на {}'.format(self.name, self.fullness)

    def eat(self):
        self.fullness += 20
        self.house.cats_food -= 10
        cprint('{} весь день ел'. format(self.name), color='yellow')

    def sleep(self):
        self.fullness -= 10
        cprint('{} весь день спал'. format(self.name), color='yellow')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('{} весь день драл обои'. format(self.name), color='yellow')

    def act(self):
        if self.fullness < 0:
            cprint('{}} помер голодной смертью'.format(self.name), color='red')
            sys.exit()
        dice = randint(1, 5)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.tear_wallpaper()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

class Man():
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я {}, сытость - {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('У {} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def play(self):
        cprint('{} весь день спасал мир'.format(self.name), color='green')
        self.fullness -= 10

    def shoping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('У {} закончились деньги'.format(self.name), color='red')
            self.work()

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def take_a_cat(self, cat):
        self.cat = cat
        cat.house = self.house

    def zoo_shoping(self):
        self.house.cats_food += 50
        self.house.money -= 50
        cprint('{} сходил за едой котам'.format(self.name), color='magenta')

    def clean(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint('{} прибрался в доме за пушистыми засранцами'.format(self.name), color='blue')
        self.eat()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер ...'.format(self.name), color='red')
            sys.exit()
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.cats_food <= 10:
            self.zoo_shoping()
        elif self.house.food < 30:
            self.shoping()
        elif self.house.money < 50:
            self.work()
        elif self.house.dirt >= 100:
            self.clean()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()

class House:

    def __init__(self):
        self.food = 0
        self.money = 0
        self.cats_food = 0
        self.dirt = 0


    def __str__(self):
       return ('В доме еды осталось {}, \nДля кота осталось еды  {} \nденег осталось {} \nгрязно на {}'.format
               (self.food, self.cats_food, self.money, self.dirt))


me = Man('Стасян')
my_sweet_home = House()
me.go_to_the_house(my_sweet_home)
pelmen = Cat('Пельмень')
gelermo = Cat("Гельермо")
obengrupen = Cat('Обенгрупен')
my_cats = []
my_cats.append(pelmen)
my_cats.append(obengrupen)
my_cats.append(gelermo)
for cat in my_cats:
    me.take_a_cat(cat)
for day in range(1, 365):
    print('=========================== {} день ============================='.format(day))
    me.act()
    for cat in my_cats:
        cat.act()
    print('--- в конце дня ---')
    for cat in my_cats:
        print(cat)
    print(me)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
