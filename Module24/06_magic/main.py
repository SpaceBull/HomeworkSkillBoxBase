class ElementEarn:
    def __init__(self):
        self.element = 'Земля'

    def __add__(self, other):
        if other == 'Вода':
            return 'Грязь'
        if other == 'Воздух':
            return 'Пыль'
        if other == 'Огонь':
            return 'Лава'
        if other == 'Земля':
            return 'Давление'
        return other + self.element


class ElementWater:
    def __init__(self):
        self.element = 'Вода'

    def __add__(self, other):
        if other == 'Земля':
            return 'Грязь'
        if other == 'Воздух':
            return 'Шторм'
        if other == 'Огонь':
            return 'Пар'
        if other == 'Вода':
            return 'Озеро'
        return other + self.element


class ElementAir:
    def __init__(self):
        self.element = 'Воздух'

    def __add__(self, other):
        if other == 'Земля':
            return 'Пыль'
        if other == 'Вода':
            return 'Шторм'
        if other == 'Огонь':
            return 'Молния'
        if other == 'Воздух':
            return 'Ветер'
        return other + self.element


class ElementFire:
    def __init__(self):
        self.element = 'Огонь'

    def __add__(self, other):
        if other == 'Земля':
            return 'Лава'
        if other == 'Воздух':
            return 'Молния'
        if other == 'Вода':
            return 'Пар'
        return other + self.element


earn = ElementEarn()
water = ElementWater()
fire = ElementFire()
air = ElementAir()

answer = water + air
print(answer)
answer = earn + fire
print(answer)
answer = earn + earn
print(answer)
answer = fire + air
print(answer)
