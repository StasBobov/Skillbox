# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):

    def __str__(self):
        return 'поле имени содержит НЕ только буквы \n'

class NotEmailError(Exception):

    def __str__(self):
        return 'поле емейл НЕ содержит @ и/или .(точку) \n'

def valid_chek(line):
    line = line[:-1]
    bad_log = open('registrations_bad.log', 'a')
    try:
        name, email, age = line.split(' ')
    except ValueError as exs:
        bad_log.write(f'{line} / {exs} \n')
        bad_log.close()
        return
    if not name.isalpha():
        try:
            raise NotNameError
        except NotNameError as exs:
            bad_log.write(f'{line} / {exs}')
            bad_log.close()
            return
    if '@' not in email or '.' not in email:
        try:
            raise NotEmailError
        except NotEmailError as exs:
            bad_log.write(f'{line} / {exs}')
            bad_log.close()
            return
    try:
        if not 9 < int(age) < 100:
            try:
                raise ValueError
            except ValueError as exs:
                bad_log.write(f'{line} / поле возраст НЕ является числом от 10 до 99 \n')
                bad_log.close()
                return
    except ValueError as exs:
                bad_log.write(f'{line} / в поле возраст необходимо указать ЧИСЛО \n')
                bad_log.close()
                return
    with open('registrations_good.log.txt', 'a') as good_log:
        good_log.write(f'{line} \n')


with open ('registrations.txt', 'r', encoding='utf-8') as file:
    for line in file:
        valid_chek(line)
