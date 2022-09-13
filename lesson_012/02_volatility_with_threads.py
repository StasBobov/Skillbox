# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# TODO тут ваш код в многопоточном стиле

import os
import time
import threading

current_path = os.path.join(os.path.dirname(__file__), 'trades\\trades')


# def get_time_track(precision):
#     def time_track(func):
#         # практически тот же самый time_track, за исключением точности вывода времени
#         def surrogate(*args, **kwargs):
#             started_at = time.time()
#             result = func(*args, **kwargs)
#             ended_at = time.time()
#             elapsed = round(ended_at - started_at, precision)  # отличия в этой строке
#             print(f'Функция работала {elapsed} секунд(ы)')
#             return result
#         return surrogate
#     return time_track


class Trade_statistic(threading.Thread):
    zero_volatility = []
    valid_tickers = []
    tickers_data = {}

    def __init__(self, file_path, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.file_path = file_path

    def run(self):
        with open(os.path.join(self.file_path)) as f:
            headers = f.readline().split(',')
            ticker_list = f.read().strip().split('\n')  # список со всеми сделками одного тикера
            self.calc(ticker_list)
        # self.result()

    def calc(self, ticker_list):
        max_price = None
        min_price = None
        for deal in ticker_list:  # для каждой сделки в списке
            deal_inf = deal.split(',')  # создаём отдельный список значений
            compared_value = float(deal_inf[2])
            if max_price is None:
                max_price = compared_value
                min_price = compared_value
            else:
                if compared_value > max_price: max_price = compared_value
                if compared_value < min_price: min_price = compared_value
        average_price = (max_price + min_price) / 2
        volatility = ((max_price - min_price) / average_price) * 100
        self.tickers_data[deal_inf[0]] = volatility

    def result(self):
        sorted_tuple = sorted(self.tickers_data.items(),
                              key=lambda item: item[1])  # сортируем tuple по второму элементу
        sorted_dict = {k: v for k, v in sorted_tuple}  # сознаём новый словарь на основании отсортированного tuple
        for key, item in sorted_dict.items():
            if item == 0.0:
                self.zero_volatility.append(key)
        for key in self.zero_volatility:
            sorted_dict.pop(key)  # удаляем из словаря значения с нулевой волотильностью
        for key, value in sorted_dict.items():
            self.valid_tickers.append(
                (key, value))  # создаём сортированный список кортежей тикеров с волотильностью не равной нулю
        print('Максимальная волатильность:')
        for i in self.valid_tickers[-1:-4:-1]:
            print(f'\t{i[0]} - {round(i[1], 2)} %')
        print('Минимальная волатильность:')
        for i in self.valid_tickers[2::-1]:
            print(f'\t{i[0]} - {round(i[1], 2)} %')
        print('Нулевая волатильность:')
        print(end='    ')
        for i in sorted(self.zero_volatility):
            print(i, end=', ')


def main():
    statistic = [Trade_statistic(file_path=os.path.join(current_path, file)) for file in os.listdir(current_path)]

    for stat in statistic:
        stat.run()



if __name__ == "__main__":
    main()

# t_d = Trade_statistic(current_path)
# started_at = time.time()
# t_d.run()
# ended_at = time.time()
# elapsed = round(ended_at - started_at, 2)  # отличия в этой строке
# print(f'\n Функция работала {elapsed} секунд(ы)')
