# -*- coding: utf-8 -*-

import os, time, shutil, zipfile, imghdr

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# path = os.getcwd()
# print(path)
# os.mkdir(path + '\icons_by_year')



class Catalog:

    def __init__(self, dir):
        self.dir = dir
        self.image_list = ['JPG', 'jpg', 'png', 'PNG', 'JPEG', 'jpeg']

    def easy_start(self):
        if zipfile.is_zipfile(self.dir):
            zfile = zipfile.ZipFile(self.dir)
            current_path = os.path.join(os.path.dirname(self.dir), 'Фотографии')
            if not os.path.isdir(current_path):
                os.mkdir(current_path)
            for file in zfile.namelist():
                name = zfile.getinfo(file).filename
                for i in self.image_list:
                    if name.endswith(i):
                        zfile.extract(file, current_path)
            self.dir = current_path
            self.pick()
        else:
            self.pick()


    def pick(self):
        tree = os.walk(self.dir)
        for dirpath, dirname, filename in tree:
            for i in filename:
                file_path = os.path.join(dirpath, i)
                stat_info = os.stat(file_path)
                sec = stat_info.st_mtime
                file_time = time.gmtime(sec)
                self.select(file_path, file_time[:2])

    def select(self, file_path, file_time):
        current_month = str(file_time[1])
        if len(current_month) < 2:
            current_month = '0' + current_month
        yer_dir = os.path.join(self.dir, str(file_time[0]))
        month_dir = os.path.join(self.dir, str(file_time[0]), current_month)
        if os.path.exists(yer_dir):
            if os.path.exists(month_dir):
                if not os.path.exists(file_path):
                    shutil.copy2(file_path, month_dir)
            else:
                os.makedirs(month_dir)
                if not os.path.exists(file_path):
                    shutil.copy2(file_path, month_dir)
        else:
            os.makedirs(month_dir)
            if not os.path.exists(file_path):
                shutil.copy2(file_path, month_dir)


# photos = Catalog('icons')
photos_path = 'D:\Фото и видео\Фотки\Качайся БЛЕАТЬ.zip'
photos = Catalog(photos_path)
photos.easy_start()



# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
