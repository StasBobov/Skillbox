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


class Water:

    def __init__(self):
        pass

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        new_obj = None
        if str(other) == 'Воздух':
            new_obj = Storm()
        elif str(other) == 'Огонь':
            new_obj = Steam()
        elif str(other) == 'Земля':
            new_obj = Dirt()
        return new_obj

class Air:

    def __init__(self):
        pass

    def __add__(self, other):
        new_obj = None
        if str(other) == 'Вода':
            new_obj = Storm()
        elif str(other) == 'Огонь':
            new_obj = Lightning()
        elif str(other) == 'Земля':
            new_obj = Dust()
        return new_obj

    def __str__(self):
        return 'Воздух'


class Fire:

    def __init__(self):
        pass

    def __add__(self, other):
        new_obj = None
        if str(other) == 'Воздух':
            new_obj = Lightning()
        elif str(other) == 'Вода':
            new_obj = Steam()
        elif str(other) == 'Земля':
            new_obj = Lava()
        return new_obj

    def __str__(self):
        return 'Огонь'

class Earth:

    def __init__(self):
        pass

    def __add__(self, other):
        new_obj = None
        if str(other) == 'Вода':
            new_obj = Dirt()
        elif str(other) == 'Огонь':
            new_obj = Lava()
        elif str(other) == 'Воздух':
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

    def __add__(self, other):
        new_obj = None
        if str(other) == 'Дерево':
            new_obj = Fire()
        return new_obj

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

class Boom:

    def __init__(self):
        pass

    def __str__(self):
        return 'Бум!'

class Wood:

    def __init__(self):
        pass

    def __add__(self, other):
        new_obj = None
        if str(other) == 'Мыло':
            new_obj = Boom()
        elif str(other) == 'Молния':
            new_obj = Boom()
        return new_obj

    def __str__(self):
        return 'Дерево'

class Soap:

    def __init__(self):
        pass

    def __add__(self, other):
        new_obj = None
        if str(other) == 'Дерево':
            new_obj = Boom()
        return new_obj

    def __str__(self):
        return 'Мыло'

print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Water(), '=', Fire() + Water())
print(Wood(), '+', Soap(), '=', Soap() + Wood())
print(Wood(), '+', Lightning(), '=', Lightning() + Wood())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
