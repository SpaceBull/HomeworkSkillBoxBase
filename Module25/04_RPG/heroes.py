import random


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние
    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и str базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage),
              ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию,
        # чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        self.magic_power = self.get_power() * 3
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:

    def attack(self, target):
        target.take_damage(self.get_power() / 2)
        # - атака - может атаковать врага, но атакует только в половину силы self.__power

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (1.2 * damage))
        super().take_damage(damage)
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)

    def healing(self, target):
        target.set_hp(target.get_hp() + self.magic_power)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        target_of_potion = friends[0]
        min_health = target_of_potion.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_potion = friend
                min_health = target_of_potion.get_hp()
        if min_health < 130 and self.magic_power > 0:
            print("Исцеляю", target_of_potion.name)
            self.healing(target_of_potion)
        else:
            if not enemies:
                return
            print("Атакую ближнего -", enemies[0].name)
            self.attack(enemies[0])
            print('\n')
        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии
        # выполняет ОДНО из действий (атака,    # исцеление) на выбранную им цель


class Tank(Hero):
    # Танк:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.shield = False
        # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
        # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:

    def attack(self, target):
        target.take_damage(self.get_power() / 2)
        # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage / self.defense))
        super().take_damage(damage)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и
    # только потом отнимается от здоровья

    def shield_up(self):
        self.shield = True
        print('Поднимаю щит')
        self.defense *= 2
        self.set_power(self.get_power() / 2)

    def shield_down(self):
        self.shield = False
        print('Опускаю щит')
        self.defense /= 2
        self.set_power(self.get_power() * 2)
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но
    # уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает
    # показатель силы в 2 раза.

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        if not enemies:
            return
        if self.defense > 2:
            self.shield_down()
        else:
            print("Атакую без щита -", enemies[0].name)
            self.attack(enemies[0])
            self.shield_up()
        print('\n')
        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет
        # ОДНО из действий (атака,
        # поднять щит/опустить щит) на выбранную им цель


class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1
    # - коэффициент усиления урона (входящего и исходящего)

    def get_power_multiply(self):
        return round(self.power_multiply, 2)

    def set_power_multiply(self, new_power):
        self.power_multiply = round(new_power, 2)

    # Методы:
    def attack(self, target):
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_down()
        # - атака - наносит урон равный показателю силы (self.__power)
        # умноженному на коэффициент усиления урона (self.power_multiply)
        # после нанесения урона - вызывается метод ослабления power_down.

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage * self.power_multiply / 2))
        super().take_damage(damage)
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона -
    # damage * (self.power_multiply / 2)

    def power_up(self):
        self.set_power_multiply(self.power_multiply * 2)
        # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза

    def power_down(self):
        self.set_power_multiply(self.power_multiply / 2)
        # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        target = random.choice(enemies)
        if self.get_power_multiply() < 2:
            print('Баф на усиление Атаки')
            self.power_up()
        else:
            print("Атака!!! Уровень урона - " + str(self.get_power()) + " Случайно атакую -", target.name)
            print()
            self.attack(target)
        if not enemies:
            return
        print('\n')
        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей
        # стратегии выполняет ОДНО из действий (атака,
        # усиление, ослабление) на выбранную им цель

