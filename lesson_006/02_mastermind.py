import sys
import urllib.request
from termcolor import cprint, colored
from mastermind_engine import make_number, test_number
from i_i import guess_number, get_result
import time

counter = 0
program_color = 'blue'
i_i_color = 'green'


cprint('ДОБРО ПОЖАЛОВАТЬ, ЖЕЛЕЗЯКА!\n', color='red')
time.sleep(1)
cprint('ЗАВОДИ ИГРУЛЮ, ДВОИЧНЫЙ!\n', color=i_i_color)
time.sleep(1)
cprint('      ИГРА НАЧАЛАСЬ!!!\n', color='red')
time.sleep(1)
cprint('Я загадал четырёхзначное число, попробуй отгадать его\n', color=program_color)
time.sleep(1)


while True:
    if_number = guess_number()
    cprint('Попробуй ка число: {0}'.format(if_number), color=i_i_color)
    counter += 1
    res = test_number(if_number)
    if res['bulls'] == 4:
        cprint('ПОЗДРАВЛЯЮ, ПОБЕДА ЗА {0} ХОДОВ!'.format(counter), color='red')
        sys.exit()
    else:
        get_result(res, if_number)
        cprint('быки - {0}, коровы - {1}'.format(res['bulls'], res['cows']), color=program_color)