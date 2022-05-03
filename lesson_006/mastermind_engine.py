
from random import randint


correct_number = '6715'

def make_number():
    global correct_number
    all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    correct_number = all_numbers.pop(randint(1, 9))
    for i in range(3):
        next_number = all_numbers.pop(randint(0, len(all_numbers)-1))
        correct_number = str(correct_number) + str(next_number)


def test_number(if_number):
    number = if_number
    result = dict(bulls=0, cows=0)
    for i in range(4): # проходим по строке через индексы
        is_in = correct_number.find(number[i]) # индекс первого вхождения буквы в строке current_number
        if is_in == i:
            result['bulls'] += 1
        elif is_in != -1:
            result['cows'] += 1
        else:
            pass
    return result



