import random

roster = [random.randint(0, 10) for _ in range(10)]
print(f'Оригинальный список: {roster}')

new_roster = [(roster[index - 1], number) for index, number in enumerate(roster) if index % 2 == 1]
print(f'Новый список (1): {new_roster}')

new_roster_2 = [(roster[number], roster[number + 1]) for number in range(0, len(roster), 2)]
print(f'Новый список (2): {new_roster_2}')