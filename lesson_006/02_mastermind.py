import sys
import urllib.request
from termcolor import cprint, colored
from mastermind_engine import make_number, test_number
import time

cprint('ДОБРО ПОЖАЛОВАТЬ, ЖЕЛЕЗЯКА!\n', color='red')
time.sleep(1)
cprint('ЗАВОДИ ИГРУЛЮ, ДВОИЧНЫЙ!\n', color='green')


counter = 0
program_color = 'blue'

def new_game(again):
    if again == 1:
        make_number()
        time.sleep(1)
        cprint('      ИГРА НАЧАЛАСЬ!!!\n', color='red')
        time.sleep(1)
        cprint('Я загадал четырёхзначное число, попробуй отгадать его\n', color=program_color)
        time.sleep(1)
    elif again == 0:
        sys.exit()

new_game(1)


while True:
    if_number = input(colored('Введите четырёхзначное число с неповторяющимися цифрами: ', color=program_color))
    if not if_number.isdigit():
        cprint('Вы не ввели число, попробуйте ещё раз', color=program_color)
        continue
    if len(if_number) != 4:
        print('Надо ввести 4 неповторяющиеся цифры, попробуйте ещё раз', color=program_color)
        continue
    number_set = set(if_number)
    if len(number_set) != 4:
        print('Цифры не должны повторяться, попробуйте ещё раз', color=program_color)
        continue
    counter += 1
    res = test_number(if_number)
    if res['bulls'] == 4:
        cprint('ПОЗДРАВЛЯЮ, ПОБЕДА ЗА {0} ХОДОВ!'.format(counter), color='red')
        counter = 0
        again = 'I will ask'
        while True:
            again = input(colored('Хотите ещё партию? Да - 1, нет - 0 ',  color=program_color))
            if again == '1':
                new_game(int(again))
                break
            elif again == '0':
                new_game(int(again))
    else:
        print('быки - {0}, коровы - {1}'.format(res['bulls'], res['cows']))