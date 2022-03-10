#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# # или проще (/сложнее ?)
# lamp_code = goods['Лампа']
# lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.


lamp = goods['Лампа']
table = goods['Стол']
sofa = goods['Диван']
chear = goods['Стул']

lamps_cost = store[lamp][0]['quantity'] * store[lamp][0]['price']
table_cost = store[table][0]['quantity'] * store[table][0]['price'] + store[table][1]['quantity'] * store[table][1]['price']
sofa_cost = store[sofa][0]['quantity'] * store[sofa][0]['price'] + store[sofa][1]['quantity'] * store[sofa][1]['price']
chear_cost = store[chear][0]['quantity'] * store[chear][0]['price'] + store[chear][1]['quantity'] * store[chear][1]['price'] + store[chear][2]['quantity'] * store[chear][2]['price']

lamp_quantity = store[lamp][0]['quantity']
table_quantity = store[table][0]['quantity'] + store[table][1]['quantity']
sofa_quantity = store[sofa][0]['quantity'] + store[sofa][1]['quantity']
chear_quantity = store[chear][0]['quantity'] + store[chear][1]['quantity'] + store[chear][2]['quantity']


print('Лампа - ' + str(lamp_quantity) + ' шт, ' + 'стоимость общая: ' + str(lamps_cost) + 'руб')
print('Стол - ' + str(table_quantity) + ' шт, ' + 'стоимость общая: ' + str(table_cost) + 'руб')
print('Диван - ' + str(sofa_quantity) + ' шт, ' + 'стоимость общая: ' + str(sofa_cost) + 'руб')
print('Стул - ' + str(chear_quantity) + ' шт, ' + 'стоимость общая: ' + str(chear_cost) + 'руб')


##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






