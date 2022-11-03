couple = {
    1: 'Первая пара',
    2: 'Вторая пара',
    3: 'Третья пара',
    4: 'Четвертая пара',
    5: 'Пятая пара',
    6: 'Шестая пара',
    7: 'Седьмая пара',
    8: 'Восьмая пара',
}
number_people = int(input('Введите количество человек: '))
family_roster = {}
heir_and_parent = {}
roster = dict()
for number in range(1, number_people):
    heir_and_parent = input(f'{couple[number]}: ').split(' ')
    flag = True
    for parent, generation in family_roster.items():
        if parent == heir_and_parent[1] and parent != 'Peter_I':
            roster = {heir_and_parent[0]: generation + 1}
            family_roster.update(roster)
            flag = False
            break
    if flag:
        roster = {heir_and_parent[0]: 1, heir_and_parent[1]: 0}
        family_roster.update(roster)


for parent, generation in sorted(family_roster.items()):
    print(parent, generation)


# Первая пара: Alexei Peter_I
# Вторая пара: Anna Peter_I
# Третья пара: Elizabeth Peter_I
# Четвёртая пара: Peter_II Alexei
# Пятая пара: Peter_III Anna
# Шестая пара: Paul_I Peter_III
# Седьмая пара: Alexander_I Paul_I
# Восьмая пара: Nicholaus_I Paul_I
