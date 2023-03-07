import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.damage = 20

    def fight(self, person):
        if person.hp > 0:
            person.hp -= self.damage
            person.print_info()

    def print_info(self):
        if self.hp != 0:
            print(f'У Персонажа {self.name} осталось {self.hp}хп')
        else:
            print(f'КОНЕЦ {self.name}')


class Battle:
    def __init__(self):
        self.war_1 = Warrior(warriors[0])
        self.war_2 = Warrior(warriors[1])

    def fight_final(self):
        for _ in range(20):
            if self.war_1.hp == 0 or self.war_2.hp == 0:
                break
            else:
                index_random = random.randint(0, 1)
                if index_random == 0:
                    print(f'\n{warriors[index_random]} наносит удар')
                    self.war_1.fight(self.war_2)
                else:
                    print(f'\n{warriors[index_random]} наносит удар')
                    self.war_2.fight(self.war_1)


warriors = ['Чебурашка', 'Шапокляк']
war_fight = Battle()
war_fight.fight_final()
















