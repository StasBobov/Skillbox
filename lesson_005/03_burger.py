# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger


import my_burger

def double_cheeseburger():
    my_burger.bun()
    my_burger.cutlets()
    my_burger.tomato()
    my_burger.cheese()
    my_burger.mayonnaise()
    print('Дабл чизбургер готов! Приятного аппетита!')

def my_favorite_burger():
    my_burger.bun()
    my_burger.ketchup()
    my_burger.cheese()
    my_burger.mayonnaise()
    print('Чиз без лука и огурца готов!')

my_favorite_burger()