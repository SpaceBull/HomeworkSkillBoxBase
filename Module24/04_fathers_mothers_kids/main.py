import random


def check_age(parent_age, age_kid):
    if age_kid > parent_age - 16:
        print('Возраст не похож на действительный')
        return False
    else:
        return True


class Parent:

    def __init__(self, name_parent, age_parent, roster_of_kids):
        self.name_parent = name_parent
        self.age_parent = age_parent
        self.roster_of_kids = []

    def info_about_parent(self):
        print(f'Меня зовут {self.name_parent}!, возраст мой - {self.age_parent}'
              f' и у меня {len(self.roster_of_kids)} детей')

    def soothe_the_child(self, children):
        if child.state_calm == 1:
            print(f'{self.name_parent}!  {children.name_child} кричит! ')
            child.state_calm = 0
        else:
            print(f'{self.name_parent}! Твоё милое дитя, {children.name_child} в состоянии спокойствия! ')

    def feed_the_child(self, children):
        if child.state_feed == 1:
            print(f'{self.name_parent}!  Твоё милое дитя, {children.name_child} хочет кушать! ')
            child.state_feed = 0
        else:
            print(f'Чудесно, {self.name_parent}! Крошка {children.name_child} кушать не хочет! ')


class Children:
    calmness = {0: 'Спокоен', 1: 'Кричит'}
    hunger = {0: 'Сыт', 1: 'Голоден'}

    def __init__(self, name_child, age_child):
        self.name_child = name_child
        self.age_child = age_child
        self.calmness = 0
        self.hunger = 0

    def info_about_child(self, calm, feed):
        print(f'Дитя {self.name_child} сейчас {Children.calmness[calm]}')
        print(f'Дитя {self.name_child} сейчас {Children.hunger[feed]}')


name_parent = input('Как зовут Вас? ').title()
age_parent = int(input(f'{name_parent} сколько лет? '))
family = Parent(name_parent, age_parent, roster_of_kids=[])

child_name_1 = input('\nКак зовут ребёнка? ').title()
child_age_1 = int(input('Сколько лет ребёнку? '))
if check_age(age_parent, child_age_1):
    data_child = Children(child_name_1, child_age_1)
    family.roster_of_kids.append(data_child)

child_name_2 = input('\nКак зовут ребёнка? ')
child_age_2 = int(input('Сколько лет ребёнку? '))
if check_age(age_parent, child_age_2):
    data_child = Children(child_name_2, child_age_2)
    family.roster_of_kids.append(data_child)

for child in family.roster_of_kids:
    child.state_calm = random.randint(0, 1)
    child.state_feed = random.randint(0, 1)
    child.info_about_child(child.state_calm, child.state_feed)
    family.soothe_the_child(child)
    family.feed_the_child(child)
