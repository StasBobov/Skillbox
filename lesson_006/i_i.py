

from random import randint


all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
non_number_list = []
number_list = []

def guess_number():
    global all_numbers
    i_guess_number = all_numbers.pop(randint(1, len(all_numbers)-1))
    for i in range(3):
        next_number = all_numbers.pop(randint(0, len(all_numbers)-1))
        i_guess_number = str(i_guess_number) + str(next_number)
    return i_guess_number

def get_result(result, last_try):
    global all_numbers
    if (result['bulls'] + result['cows']) !=  0:
        for i in last_try:
            all_numbers.append(int(i))
    all_numbers.sort()
