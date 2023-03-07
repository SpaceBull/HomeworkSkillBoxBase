class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]} ')


class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')

        else:
            print('Вся картошка созрела. Можно собирать\n')
            return True


class Gardener:

    def __init__(self, name_gardener, count):
        self.name_gardener = name_gardener
        self.count_potato = count
        self.bed_potatoes = Garden(count)
        self.harvested_potatoes = []

    def care_of_the_garden(self):
        print('Садовник начинает ухаживать за картошкой')
        self.bed_potatoes.grow_all()

    def harvest(self):
        if self.bed_potatoes.are_all_ripe():
            self.harvested_potatoes.append(self.count_potato)
            print(f'Садовник {self.name_gardener} сегодня собрал урожай Картошки! Целых {self.count_potato} шт.')
        else:
            print(f'Еще рано Садовнику {self.name_gardener} собирать урожай! Расти Картошку')


gardener_1 = Gardener('Коля', 5)
for _ in range(3):
    gardener_1.care_of_the_garden()

gardener_1.harvest()
