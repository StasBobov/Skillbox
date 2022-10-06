# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru



# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
from pprint import pprint

from PIL import Image
import os
from PIL import ImageDraw, ImageFont, ImageColor
import argparse

path = os.path.join(os.path.dirname(__file__), 'images\\ticket_template.png')
font_path = os.path.join(os.path.dirname(__file__), 'ofont_ru_Manrope.ttf')


def make_ticket(fio, from_, to, date, save_to):
    with Image.open(path) as image:
        font_size = 20
        font = ImageFont.truetype(font_path, size=font_size)
        draw_text = ImageDraw.Draw(image)
        draw_text.text((48, 140-font_size), fio, font=font, fill=ImageColor.colormap['black'])
        draw_text.text((48, 206-font_size), from_, font=font, fill=ImageColor.colormap['black'])
        draw_text.text((48, 274-font_size), to, font=font, fill=ImageColor.colormap['black'])
        draw_text.text((288, 274-font_size), date, font=font, fill=ImageColor.colormap['black'])
        if save_to == None:
            image.save(os.path.join(os.path.dirname(__file__), 'my_lucky_ticket.png'))
        else:
            image.save(save_to)
        image.show()


parser = argparse.ArgumentParser(description='Here it is... your fly ticket!')
parser.add_argument('fio', type=str, help='Enter your name')
parser.add_argument('_from', type=str, help='Where will you fly from')
parser.add_argument('to', type=str, help='Where will you fly?')
parser.add_argument('date', type=str, help='When will you fly?')
parser.add_argument('--save_to', type=str, help='Where do you want to save your ticket?')
args = parser.parse_args()

make_ticket(fio=args.fio, from_=args._from, to=args.to, date=args.date, save_to=args.save_to)
