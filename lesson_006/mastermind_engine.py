
from random import randint

correct_number = ''

def make_number():
    global correct_number
    all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    correct_number = all_numbers.pop(randint(1, 9))
    for i in range(3):
        next_number = all_numbers.pop(randint(0, len(all_numbers)-1))
        correct_number = str(correct_number) + str(next_number)


def test_number(if_number):
    pass

make_number()
print(correct_number)