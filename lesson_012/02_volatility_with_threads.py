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

import os
import time
import threading

current_path = os.path.join(os.path.dirname(__file__), 'trades\\trades')


def get_time_track(precision):
    def time_track(func):
        # практически тот же самый time_track, за исключением точности вывода времени
        def surrogate(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)  # отличия в этой строке
            print(f'\nФункция работала {elapsed} секунд(ы)', flush=True)
            return result
        return surrogate
    return time_track

def result(my_class):
    valid_tickers = []
    zero_volatility = []
    sorted_tuple = sorted(my_class.tickers_data.items(),
                          key=lambda item: item[1])  # сортируем tuple по второму элементу
    sorted_dict = {k: v for k, v in sorted_tuple}  # сознаём новый словарь на основании отсортированного tuple
    for key, item in sorted_dict.items():
        if item == 0.0:
            zero_volatility.append(key)
    for key in zero_volatility:
        sorted_dict.pop(key)  # удаляем из словаря значения с нулевой волотильностью
    for key, value in sorted_dict.items():
        valid_tickers.append(
            (key, value))  # создаём сортированный список кортежей тикеров с волотильностью не равной нулю
    print('Максимальная волатильность:', flush=True)
    for i in valid_tickers[-1:-4:-1]:
        print(f'\t{i[0]} - {round(i[1], 2)} %')
    print('Минимальная волатильность:', flush=True)
    for i in valid_tickers[2::-1]:
        print(f'\t{i[0]} - {round(i[1], 2)} %')
    print('Нулевая волатильность:', flush=True)
    print(end='    ')
    for i in sorted(zero_volatility):
        print(i, end=', ')

class Trade_statistic(threading.Thread):
    tickers_data = {}

    def __init__(self, name, file_path, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.file_path = file_path
        self.name = name

    def run(self):
        print(f'{self.name} создан', flush=True)
        with open(self.file_path, 'r') as f:
            headers = f.readline().split(',')
            ticker_list = f.read().strip().split('\n')  # список со всеми сделками одного тикера
            self.calc(ticker_list)

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
        Trade_statistic.tickers_data[deal_inf[0]] = volatility
        print(f'{self.name} посчитан', flush=True)


@get_time_track(precision=2)
def main():
    statistic = [Trade_statistic(name=file, file_path=os.path.join(current_path, file)) for file in os.listdir(current_path)]

    for stat in statistic:
        stat.start()
    for stat in statistic:
        stat.join()

    result(Trade_statistic)


if __name__ == "__main__":
    main()


