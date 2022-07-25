# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777

# TODO здесь ваш код

from random import randint

class IamGodError(Exception):

    def __str__(self):
        return 'IamGodError, Take it easy? maan...'


class DrunkError(Exception):

    def __str__(self):
        return 'DrunkError, Опять нажрался, алкаш...'

class CarCrashError(Exception):

    def __str__(self):
        return 'CarCrashError, Это уже перебор, чувак...'

class GluttonyError(Exception):

    def __str__(self):
        return 'GluttonyError, Приятного аппетита...'

class DepressionError(Exception):

    def __str__(self):
        return 'DepressionError, Чёт приуныл?'

class SuicideError(Exception):

    def __str__(self):
        return 'SuicideError, А почему бы и да...'


CARMA = 0


def one_day(day):
    global CARMA, faith
    ecs_risk = randint(1, 13)
    if ecs_risk == 13:
        madness = randint(1, 6)
        if madness == 1:
            raise IamGodError
        elif madness == 2:
            raise DrunkError
        elif madness == 3:
            raise CarCrashError
        elif madness == 4:
            raise GluttonyError
        elif madness == 5:
            raise DepressionError
        elif madness == 6:
            raise SuicideError
    else:
        get_carma = randint(1, 7)
        CARMA += get_carma
        if CARMA >= ENLIGHTENMENT_CARMA_LEVEL:
            faith = True

def logging(exs=None):
    global day
    if exs != None:
        with open('log.txt', 'a') as file:
            file.write(f'день {day} {exs.__str__()} \n')


day = 0
faith = False

while faith == False:
    day += 1
    try:
        one_day(day)
    except IamGodError as exs:
        logging(exs)
    except DrunkError as exs:
        logging(exs)
    except CarCrashError as exs:
        logging(exs)
    except GluttonyError as exs:
        logging(exs)
    except DepressionError as exs:
        logging(exs)
    except SuicideError as exs:
        logging(exs)


print(f'День {day}. Ура!!! Я выбрался!')

# https://goo.gl/JnsDqu
