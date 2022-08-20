# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
import time

# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers
#
# start_time = time.time()
# for prime in get_prime_numbers(10000):
#     print(prime)
# print(time.time() - start_time)

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#
#     def __init__(self, n):
#         self.n = n
#         self.num = 1
#
#     def __iter__(self):
#         self.num = 1
#         return self
#
#     def __next__(self):
#         while True:
#             self.num += 1
#             if self.num > self.n:
#                 raise StopIteration
#             elif self.num == 2:
#                 return self.num
#
#             r = 2
#             while r < self.num:
#                 if self.num % r == 0:
#                     break
#                 else:
#                     if r == (self.num - 1):
#                         return self.num
#                     else:
#                         r += 1
#
# start_time = time.time()
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)
# print(time.time() - start_time)
# print(13 in prime_number_iterator)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def prime_numbers_generator(n):
#     for i in range (2, n+1):
#         if i == 2:
#             yield i
#         else:
#             for j in range (2, i):
#                 if i % j == 0:
#                     break
#                 if j == (i -1):
#                     yield i
#
#
# start_time = time.time()
# for number in prime_numbers_generator(n=10000):
#     print(number)
# print(time.time() - start_time)
# print(13 in prime_numbers_generator(1000))

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
from functools import reduce


def filter_happy(number):
    l = len(str(number))
    if l % 2 == 0:
        segment = l / 2
        num1 = str(number)[:int(segment)]
        num1 = [int(char) for char in num1]
        num1 = reduce(lambda x, y: x + y, num1)
        num2 = str(number)[int(segment):]
        num2 = [int(char) for char in num2]
        num2 = reduce(lambda x, y: x + y, num2)
    else:
        print('No')

filter_happy(225667)