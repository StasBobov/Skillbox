# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError as exs:
    print(f'Это не число, чувак! {exs}')
except IndexError as exs:
    print(f'Нужно ввести минимум 5 чисел, чувак! {exs}')
except Exception as exs:
    print(f'Что-то ты запорол, чувак! {exs}')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преоб1234разовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




