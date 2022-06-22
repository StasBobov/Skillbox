# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

class Water:

    def __init__(self):
        pass

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        new_obj = None
        print(type(other))
        if other == 'Воздух':
            new_obj = Storm()
        elif other == 'Огонь':
            new_obj = Steam()
        elif other == 'Земля':
            new_obj = Dirt()
        return new_obj

class Air:

    def __init__(self):
        pass

    def __add__(self, other):
        new_obj = None
        if other == 'Вода':
            new_obj = Storm()
        elif other == 'Огонь':
            new_obj = Lightning()
        elif other == 'Земля':
            new_obj = Dust()
        return new_obj

    def __str__(self):
        return 'Воздух'


class Fire:

    def __init__(self):
        pass

    def __add__(self, other):
        new_obj = None
        if other == 'Воздух':
            new_obj = Lightning()
        elif other == 'Вода':
            new_obj = Steam()
        elif other == 'Земля':
            new_obj = Lava()
        return new_obj

    def __str__(self):
        return 'Огонь'

class Earth:

    def __init__(self):
        pass

    def __add__(self, other):
        new_obj = None
        if other == 'Вода':
            new_obj = Dirt()
        elif other == 'Огонь':
            new_obj = Lava()
        elif other == 'Воздух':
            new_obj = Dust()
        return new_obj

    def __str__(self):
        return 'Земля'


class Storm:

    def __init__(self):
        pass

    def __str__(self):
        return 'Шторм'


class Steam:

    def __init__(self):
        pass

    def __str__(self):
        return 'Пар'

class Dirt:

    def __init__(self):
        pass

    def __str__(self):
        return 'Грязь'


class Lightning:

    def __init__(self):
        pass

    def __str__(self):
        return 'Молния'


class Dust:

    def __init__(self):
        pass

    def __str__(self):
        return 'Пыль'


class Lava:

    def __init__(self):
        pass

    def __str__(self):
        return 'Лава'

print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
