# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>


import os
from collections import defaultdict

current_path = os.path.join(os.path.dirname(__file__), 'trades\\trades')


class Trade_statistic:

    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.tickers_data = {}
        self.zero_volatility = []
        self.valid_tickers = []

    def run(self):
        for file in os.listdir(self.directory_path):
            with open(os.path.join(current_path, file)) as f:
                headers = f.readline().split(',')
                ticker_list = f.read().strip().split('\n') # список со всеми сделками одного тикера
                self.calc(ticker_list)
        self.result()



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
        sorted_tuple = sorted(self.tickers_data.items(), key=lambda item: item[1]) # сортируем tuple по второму элементу
        sorted_dict = {k: v for k, v in sorted_tuple} # сознаём новый словарь на основании отсортированного tuple
        for key, item in sorted_dict.items():
            if item == 0.0:
                self.zero_volatility.append(key)
        for key in self.zero_volatility:
            sorted_dict.pop(key) # удаляем из словаря значения с нулевой волотильностью
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



t_d = Trade_statistic(current_path)
t_d.run()