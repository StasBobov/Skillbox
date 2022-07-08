# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
import zipfile
import os


class Word_Docs_Statistic():

    def __init__(self, file):
        self.file = file

    def unzip(self):
        zfile = zipfile.ZipFile(self.file, 'r') # создали объект zipfile.ZipFile
        for file in zfile.namelist(): # для каждого файла в zfile производим распаковку
            zfile.extract(file)
        self.file = file
        print(self.file)

    def read(self):
        if self.file.endwith('.zip'):
            self.unzip()



for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for name in filenames:
        if name == 'voyna-i-mir.txt.zip':
            current_path = os.path.join(dirpath, name)

war_and_peace = Word_Docs_Statistic(current_path)
war_and_peace.read()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
