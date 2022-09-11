numbers = int(input('Кол-во чисел: '))
roster = []
new_roster = []
for _ in range(numbers):
    number = int(input('Введите число: '))
    roster.append(number)
if roster == roster[::-1]:
    print('Цифры симметричны')
if roster != roster[::-1]:
    if roster[-1] == roster[-2]:
        for i in range(len(roster), 2, -1):
            new_roster.append(roster[-i])
    else:
        for i in range(len(roster), 1, -1):
            new_roster.append(roster[-i])
    print(f'Последовательность {roster}')
    print(f'Нужно приписать чисел: {len(new_roster)}')
    print(f'Сами числа: {new_roster[::-1]}')

