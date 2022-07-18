# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class Analiz:

    def __init__(self, file_name):
        self.file_name = file_name
        self.pos = None
        self.rep = 0

    def read(self, span):
        if span == 'minet':
            x = 17
        elif span == 'hour':
            x = 14
        elif span == 'month':
            x = 8
        elif span == 'year':
            x = 5
        with open(self.file_name, 'r') as file:
            for line in file:
                if (line[-4] + line[-3] + line[-2]) == 'NOK':
                    self.count(line[0:x]+']')
        self.write_results(self.pos, self.rep)

    def count(self, line):
        if self.pos != line:
            if self.pos != None:
                self.write_results(self.pos, self.rep)
                self.pos = line
                self.rep = 1
            else:
                self.pos = line
                self.rep = 1
        else:
            self.rep += 1


    def write_results(self, string, rep):
        with open('result.txt', mode='a') as newfile:
            newfile.write(string + ' ' + str(rep) + '\n')


events = Analiz('events.txt')
events.read('year')



# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
