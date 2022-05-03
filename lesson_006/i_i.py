

from random import randint


all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
non_number_list = []
number_list = []

def make_number():
    if number_list == []:
        correct_number = all_numbers.pop(randint(1, 9))
    for i in range(3):
        next_number = all_numbers.pop(randint(0, len(all_numbers)-1))
        correct_number = str(correct_number) + str(next_number)
    return correct_number

def get_result():
    pass


print(make_number())