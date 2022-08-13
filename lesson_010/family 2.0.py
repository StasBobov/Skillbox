# -*- coding: utf-8 -*-
import random

from termcolor import cprint

class NoFoodError(Exception):

    def __str__(self):
        return 'Не осталось еды!'


class NoMoneyError(Exception):

    def __str__(self):
        return 'Не осталось денег!'

class HeroDiedError(Exception):

    def __str__(self):
        return 'Кирдык герою!'


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.total_eat = 0
        self.royal_cannin = 30

    def act(self):
        if self.dirt < 0:
            self.dirt = 0
        self.dirt += 5



    def __str__(self):
        return super().__str__() + f' дома денег {self.money}, еды {self. food}, грязи {self.dirt}, еды для котов {self.royal_cannin}'

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
        if self.house.food >= meal:
            self.satiety += round(meal)
            self.house.food -= round(meal)
            self.house.total_eat += round(meal)
            cprint('{} вкусненько поел(а)'.format(self.name), color='green')
        else:
            raise NoFoodError


    def tisk_the_cat(self):
        self.satiety -= 10
        self.happiness += 5
        cprint('{} гладит сладкого пирожочка'.format(self.name), color='green')

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.satiety < 0 or self.happiness < 10:
            raise HeroDiedError
        if self.satiety <= 20:
            try:
                self.eat(30)
                return False
            except NoFoodError as exs:
                print(f'{exs}')
                self.tisk_the_cat()
        return True


class Husband(Man):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


    def act(self):
        # if self.live == True:
        if super().act():
            if self.happiness < 20:
                self.gaming()
            elif self.house.money <= 100:
                self.work()
            else:
                what_would_i_do = random.randint(1, 4)
                if what_would_i_do == 1:
                    self.work()
                elif what_would_i_do == 2:
                    try:
                        self.eat(10)
                    except NoFoodError as exs:
                        print(f'{exs}')
                        self.satiety -= 10
                elif what_would_i_do == 3:
                    self.tisk_the_cat()
                else:
                    self.gaming()


    def work(self):
        self.house.money += self.salary
        self.satiety -= 10
        self.total_income += self.salary
        cprint('{} пошёл на работу'.format(self.name), color='blue')

    def gaming(self):
        self.happiness += 20
        self.satiety -= 10
        cprint('{} наконец-то играет'.format(self.name), color='green')


class Wife(Man):
    coat = 0

    def __init__(self, name):
        super().__init__(name)


    def act(self):
        # if self.live == True:
        if super().act():
            if self.happiness < 20:
                try:
                    self.buy_fur_coat()
                except NoMoneyError as exs:
                    print(f'{exs} на новую шубу(((')
                    self.tisk_the_cat()
            elif self.house.food <= 30:
                    try:
                        self.shopping(100)
                    except NoMoneyError as exs:
                        print(f'{exs}')
                        self.tisk_the_cat()
            elif self.house.royal_cannin <= 100:
                try:
                    self.pet_shopping(100)
                except NoFoodError as exs:
                        print(f'{exs} у пирожочка сладенького!!!')
                        self.tisk_the_cat()
            elif self.house.dirt >= 50:
                self.clean_house()
            else:
                what_would_i_do = random.randint(1, 6)
                if what_would_i_do == 1:
                    self.clean_house()
                elif what_would_i_do == 2:
                    try:
                        self.eat(10)
                    except NoFoodError as exs:
                        print(f'{exs}')
                        self.tisk_the_cat()
                        self.satiety -= 10
                elif what_would_i_do == 3:
                    self.tisk_the_cat()
                elif what_would_i_do == 4:
                    try:
                        self.pet_shopping(50)
                    except NoMoneyError as exs:
                        print(f'{exs}')
                        self.tisk_the_cat()
                elif what_would_i_do == 5:
                    try:
                        self.buy_fur_coat()
                    except NoMoneyError as exs:
                        print(f'{exs} на новую шубу(((')
                        self.clean_house()

    def pet_shopping(self, purchase):
        if self.house.money >= purchase:
            self.house.royal_cannin += purchase
            self.house.money -= purchase
            self.satiety -= 10
            cprint('{} купила котику вкусняшки'.format(self.name), color='blue')
        else:
            raise NoFoodError

    def shopping(self, purchase):
        if self.house.money >= purchase:
            self.house.food += purchase
            self.house.money -= purchase
            self.satiety -= 10
            cprint('{} пошла по магазинам'.format(self.name), color='blue')
        else:
            raise NoMoneyError


    def buy_fur_coat(self):
        if self.house.money >= 350:
            Wife.coat += 1
            self.house.money -= 350
            self.happiness += 60
            self.satiety -= 10
            cprint('Обзавидуйтесь все у {} новая шубка'.format(self.name), color='green')
        else:
            raise NoMoneyError


    def clean_house(self):
        self.house.dirt -= 100
        self.satiety -= 10
        cprint('{} прибирается по дому'.format(self.name), color='blue')


class Cat:

    def __init__(self, name):
        self.satiety = 30
        self.name = name
        self.house = None
        # self.live = True

    def __str__(self):
        return super().__str__() + ' {} сыт на {}, молодец {}'.format(self.name, self.satiety, self.name)

    def act(self):
        if self.satiety < 0:
            cprint('{} помер, довели, кожанные мешки!'.format(self.name), color='red')
            life.cats.remove(self)
            return
        if self.satiety < 30:
            try:
                self.eat(5)
            except NoFoodError as exs:
                print('МЯЯЯЯУУУУ!!!!')
                self.satiety -= 10
        else:
            what_would_i_do = random.randint(1, 3)
            if what_would_i_do == 1:
                self.sleep()
            elif what_would_i_do == 2:
                try:
                    self.eat(5)
                except NoFoodError as exs:
                    print('МЯЯЯЯУУУУ!!!!')
            else:
                self.soil()



    def eat(self, meal):
        if self.house.royal_cannin >= meal:
            self.satiety += meal*2
            self.house.royal_cannin -= meal
            self.house.total_eat += meal
            cprint('{} покушал, молодец...'.format(self.name), color='green')
        else:
            raise NoFoodError

    def sleep(self):
        self.satiety -= 10
        cprint('{} поспал, молодец...'.format(self.name), color='green')

    def soil(self):
        self.satiety -= 10
        self.house.dirt += 5
        cprint('{} нельзя драть обои!...'.format(self.name), color='green')



class Child(Man):

    def __init__(self, name):
        super().__init__(name)


    def act(self):
        # if self.live == True:
        if self.satiety < 0:
            raise HeroDiedError
            # cprint('{} помер писдюк'.format(self.name), color='red')
            # self.live = False
            # Simulation.all_alive = False
            # return
        if self.satiety <= 20:
            try:
                self.eat(10)
            except NoFoodError as exs:
                print('УУУУAAAAAAA!!!!!!!!!')
        else:
            what_would_i_do = random.randint(1, 2)
            if what_would_i_do == 1:
                try:
                    self.eat(10)
                except NoFoodError as exs:
                    print('УУУУAAAAAAA!!!!!!!!!')
            else:
                self.sleep()

    def eat(self, meal):
        if self.house.food >= meal:
            super().eat(meal)
        else:
            raise NoFoodError

    def sleep(self):
        self.satiety -= 10
        cprint('{} поспал...опять...'.format(self.name), color='green')


class Simulation:
    all_alive = True

    def experiment(self, salary, count_cats):
        home = House()
        serge = Husband(name='Сережа', salary=salary)
        masha = Wife(name='Маша')
        serge.house = home
        masha.house = home
        dazdranagon = Child('Даздранагон')
        dazdranagon.house = home
        self.cats = []
        for i in range(count_cats):
            self.cats.append(Cat(f'Кот {i}'))
            for cat in self.cats:
                cat.house = home
        for day in range(365):
            cprint('================== День {} =================='.format(day), color='red')
            try:
                serge.act()
            except HeroDiedError as exs:
                print(f'{exs.__str__()}, бедный Серёга... Не уследили...')
                return
            try:
                masha.act()
            except HeroDiedError as exs:
                print(f'{exs.__str__()}, как жеж Машку то не уберегли???...')
                return
            try:
                dazdranagon.act()
            except HeroDiedError as exs:
                print(f'{exs.__str__()}, неудобняк получился с писдюком...')
                return
            for cat in self.cats:
                cat.act()
                cprint(cat, color='cyan')
            home.act()
            cprint(serge, color='cyan')
            cprint(masha, color='cyan')
            cprint(dazdranagon, color='cyan')
            cprint(home, color='cyan')
        cprint('За год Серёга заработал {} $, молодец Серёга!'.format(serge.total_income), color='red')
        cprint('За год Серёга с Машей поели {} еды, и совсем не поправились!'.format(home.total_eat), color='red')
        cprint('За Маша купила {} шуб, потому-что шуб много не бывает!'.format(Wife.coat), color='red')

life = Simulation()
max_cats = life.experiment(150, 10)


# for food_incidents in range(6):
#    for money_incidents in range(6):
#        life = Simulation(money_incidents, food_incidents)
#        for salary in range(50, 401, 50):
#            max_cats = life.experiment(salary)
#            print('{} спиздили раз деньги, {} раз спиздили еду'.format(money_incidents, food_incidents))
#            print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#            Simulation.all_alive = True


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

