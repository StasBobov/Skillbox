# -*- coding: utf-8 -*-
import random

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.total_eat = 0
        self.royal_cannin = 30

    def act(self):
        self.dirt += 5

    def __str__(self):
        return super().__str__() + ' дома денег {}, еды {}, грязи {}'.format(self.money, self. food, self.dirt)

class Man:

    def __init__(self, name):
        self.satiety = 30
        self.happiness = 100
        self.name = name
        self.house = None
        self.live = True
        self.total_income = 0

    def __str__(self):
        if self.live == True:
            return super().__str__() + ' это {}, он(она) сыт(а) на {}, и счастлив(а) на {}'.format(self.name, self.satiety, self. happiness)
        elif self.live == False:
            return '{} DEAD'.format(self.name)

    def eat(self, meal):
        self.satiety += round(meal)
        self.house.food -= round(meal)
        self.house.total_eat += round(meal)
        # cprint('{} вкусненько поел(а)'.format(self.name), color='green')

    def tisk_the_cat(self):
        self.satiety -= 10
        self.happiness += 5
        # cprint('{} гладит сладкого пирожочка'.format(self.name), color='green')

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.satiety < 0 or self.happiness < 10:
            cprint('{} помер(ла)'.format(self.name), color='red')
            self.live = False
            Simulation.all_alive = False
            return False
        if self.satiety <= 30:
            if self.house.food >= 60:
                self.eat(30)
            else:
                self.eat(self.house.food / 3)
            return False
        else:
            return True


class Husband(Man):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def act(self):
        if self.live:
            if super().act():
                if self.happiness < 20:
                    self.gaming()
                elif self.house.money <= 1000:
                    self.work()
                else:
                    what_would_i_do = random.randint(1, 4)
                    if what_would_i_do == 1:
                        self.work()
                    elif what_would_i_do == 2:
                        if self.house.food >= 50:
                            self.eat(10)
                    elif what_would_i_do == 3:
                        self.tisk_the_cat()
                    else:
                        self.gaming()


    def work(self):
        self.house.money += self.salary
        self.satiety -= 10
        self.total_income += self.salary
        # cprint('{} пошёл на работу'.format(self.name), color='blue')

    def gaming(self):
        self.happiness += 20
        self.satiety -= 10
        # cprint('{} наконец-то играет'.format(self.name), color='green')


class Wife(Man):
    coat = 0

    def __init__(self, name):
        super().__init__(name)


    def act(self):
        if self.live == True:
            if super().act():
                if self.happiness < 20:
                    if self.house.money >= 350:
                        self.buy_fur_coat()
                elif self.house.food <= 200:
                    if self.house.money >= 200:
                        self.shopping(200)
                    else:
                        self.shopping(self.house.money)
                elif self.house.royal_cannin <= 200:
                    if self.house.money >= 200:
                        self.pet_shopping(100)
                    else:
                        self.pet_shopping(self.house.money/2)
                elif self.house.dirt >= 50:
                    self.clean_house()
                elif self.house.money >= 1200:
                    self.buy_fur_coat()
                else:
                    what_would_i_do = random.randint(1, 5)
                    if what_would_i_do == 1:
                        self.clean_house()
                    elif what_would_i_do == 2:
                        if self.house.food >= 50:
                            self.eat(10)
                    elif what_would_i_do == 3:
                        self.tisk_the_cat()
                    elif what_would_i_do == 4:
                        if self.house.money >= 100:
                            self.pet_shopping(30)
                    else:
                        if self.house.money >= 100:
                            self.shopping(30)

    def pet_shopping(self, purchase):
        self.house.royal_cannin += purchase
        self.house.money -= purchase
        self.satiety -= 10
        # cprint('{} купила котику вкусняшки'.format(self.name), color='blue')

    def shopping(self, purchase):
        self.house.food += purchase
        self.house.money -= purchase
        self.satiety -= 10
        # cprint('{} пошла по магазинам'.format(self.name), color='blue')


    def buy_fur_coat(self):
        Wife.coat += 1
        self.house.money -= 350
        self.happiness += 60
        self.satiety -= 10
        # cprint('Обзавидуйтесь все у {} новая шубка'.format(self.name), color='green')

    def clean_house(self):
        self.house.dirt -= 100
        self.satiety -= 10
        # cprint('{} прибирается по дому'.format(self.name), color='blue')








######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.satiety = 30
        self.name = name
        self.house = None
        self.live = True

    def __str__(self):
        return super().__str__() + ' {} сыт на {}, молодец {}'.format(self.name, self.satiety, self.name)

    def act(self):
        if self.live == True:
            if self.satiety < 0:
                cprint('{} помер, довели, кожанные мешки!'.format(self.name), color='red')
                self.live = False
                Simulation.all_alive = False
                return
            if self.satiety < 30:
                if self.house.royal_cannin >= 5:
                    self.eat(5)
                else:
                    self.eat(self.house.royal_cannin)
            else:
                what_would_i_do = random.randint(1, 3)
                if what_would_i_do == 1:
                    self.sleep()
                elif what_would_i_do == 2:
                    if self.house.royal_cannin >= 5:
                        self.eat(5)
                    else:
                        self.eat(self.house.royal_cannin)
                else:
                    self.soil()



    def eat(self, meal):
        self.satiety += meal*2
        self.house.royal_cannin -= meal
        self.house.total_eat += meal
        # cprint('{} покушал, молодец...'.format(self.name), color='green')

    def sleep(self):
        self.satiety -= 10
        # cprint('{} поспал, молодец...'.format(self.name), color='green')

    def soil(self):
        self.satiety -= 10
        self.house.dirt += 5
        # cprint('{} нельзя драть обои!...'.format(self.name), color='green')



######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def __init__(self, name):
        super().__init__(name)


    def act(self):
        if self.live == True:
            if self.satiety < 0:
                cprint('{} помер писдюк'.format(self.name), color='red')
                self.live = False
                Simulation.all_alive = False
                return
            if self.satiety <= 20:
                if self.house.food >= 30:
                    self.eat(10)
                else:
                    self.eat(self.house.food / 3)
            else:
                what_would_i_do = random.randint(1, 2)
                if what_would_i_do == 1:
                    if self.house.food >= 30:
                        self.eat(10)
                    else:
                        self.eat(self.house.food / 3)
                else:
                    self.sleep()

    def eat(self, meal):
        super().eat(meal)


    def sleep(self):
        self.satiety -= 10
        # cprint('{} поспал...опять...'.format(self.name), color='green')


class Simulation:
    all_alive = True

    def __init__(self, m_i, f_i):
        self.money_incidents = m_i
        self.food_incedents = f_i

    def experiment(self, salary):
        home = House()
        serge = Husband(name='Сережа', salary=salary)
        masha = Wife(name='Маша')
        serge.house = home
        masha.house = home
        dazdranagon = Child('Даздранагон')
        dazdranagon.house = home
        bad_money_day = set()
        bad_food_day = set()
        while len(bad_money_day) != (money_incidents):
            bad_money_day.add(random.randint(0, 364))
        while len(bad_food_day) != (food_incidents):
            bad_food_day.add(random.randint(0, 364))
        cats = []
        while Simulation.all_alive == True:
            cats.append(Cat('Кот'))
            for cat in cats:
                cat.house = home
            for day in range(365):
                # cprint('================== День {} =================='.format(day), color='red')
                serge.act()
                masha.act()
                dazdranagon.act()
                for cat in cats:
                    cat.act()
                home.act()
                if day in bad_money_day:
                    home.money = round(home.money/2)
                if day in bad_food_day:
                    home.money = round(home.food/2)
                # cprint(serge, color='cyan')
                # cprint(masha, color='cyan')
                # cprint(dazdranagon, color='cyan')
                # cprint(home, color='cyan')
        return len(cats)
        # cprint('За год Серёга заработал {} $, молодец Серёга!'.format(serge.total_income), color='red')
        # cprint('За год Серёга с Машей поели {} еды, и совсем не поправились!'.format(home.total_eat), color='red')
        # cprint('За Маша купила {} шуб, потому-что шуб много не бывает!'.format(Wife.coat), color='red')



for food_incidents in range(6):
   for money_incidents in range(6):
       life = Simulation(money_incidents, food_incidents)
       for salary in range(50, 401, 50):
           max_cats = life.experiment(salary)
           print('{} спиздили раз деньги, {} раз спиздили еду'.format(money_incidents, food_incidents))
           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
           Simulation.all_alive = True

# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     for cat in cats:
#         cat.act()
#     dazdranagon.act()
#     food_sleal = random.randint(1, 10)
#     if food_sleal == 5:
#         home.food = round(home.food/2)
#         cprint('Где моя еда???!!', color='red')
#     home.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     for cat in cats:
#         cprint(cat, color='cyan')
#     cprint(dazdranagon, color='cyan')
#     cprint(home, color='cyan')
# cprint('За год Серёга заработал {} $, молодец Серёга!'.format(serge.total_income), color='red')
# cprint('За год Серёга с Машей поели {} еды, и совсем не поправились!'.format(home.total_eat), color='red')
# cprint('За Маша купила {} шуб, потому-что шуб много не бывает!'.format(Wife.coat), color='red')


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

