# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234





def analiz(file):
    pos = None
    rep = 0
    with open(file, 'r') as f:
        for line in f:
            if (line[-4] + line[-3] + line[-2]) == 'NOK':
                line = line[0:17] + ']'
                if pos != line:  # Если новый временной отрезок
                    if pos != None:
                        yield line, rep
                        pos = line
                        rep = 1
                    else:
                       pos = line
                       rep = 1
                else:
                    rep += 1


grouped_events = analiz('events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')



class Analiz:

    def __init__(self, file_name):
        self.file_name = file_name
        self.pos = None
        self.rep = 0

    def __iter__(self):
        self.file = open(self.file_name, 'r')
        return self

    def __next__(self):
        for line in self.file:
            if (line[-4] + line[-3] + line[-2]) == 'NOK':
                line = line[0:17] + ']'
                if self.pos != line: # Если новый временной отрезок
                    if self.pos != None:
                        ret = (line, self.rep)
                        self.pos = line
                        self.rep = 1
                        return ret
                    else:
                        self.pos = line
                        self.rep = 1
                else:
                    self.rep += 1
        self.file.close()
        raise StopIteration


grouped_events = Analiz('events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
