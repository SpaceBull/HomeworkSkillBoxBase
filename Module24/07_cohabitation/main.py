import random


class Human:

    def __init__(self, name):
        self.satiety = 50
        self.house = House()
        self.name = name

    def to_eat(self):
        self.house.refrigerator_with_food -= 5
        self.satiety += 5

    def work(self):
        self.satiety -= 5
        self.house.money += 10

    def play(self):
        self.satiety -= 5

    def visit_the_store(self):
        self.house.refrigerator_with_food += 10
        self.house.money -= 5

    def info(self):
        print(f'Человек по имени {self.name} имеет: \n'
              f'Сытость: {self.satiety}\n'
              f'Еды: {self.house.refrigerator_with_food}\n'
              f'Денег: {self.house.money}')


class House:

    def __init__(self):
        self.refrigerator_with_food = 50
        self.money = 0


man_vasya = Human('Вася')
man_nastya = Human('Настя')


def life(man):
    day = 0
    for day in range(366):
        number = random.randint(1, 6)
        if man.satiety < 20:
            if man.satiety < 0:
                print('\nЧеловек умер(\n')
                break
            man.to_eat()
        elif man.house.refrigerator_with_food < 20:
            man.visit_the_store()
        elif man.house.money < 50:
            man.work()
        elif number == 1:
            man.work()
        elif number == 2:
            man.to_eat()
        else:
            man.play()
    man.info()
    print(f'Прожил этот человек {day}\n')


life(man_vasya)
life(man_nastya)
