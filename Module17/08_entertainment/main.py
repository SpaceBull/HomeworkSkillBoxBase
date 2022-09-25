import random

number_of_sticks = int(input('Количество палок: '))
sticks = ['|' for _ in range(number_of_sticks)]
number_of_throws = int(input('Количество бросков: '))
initial_number = 1

for cast in range(number_of_throws):
    left_border = random.randint(initial_number, number_of_sticks)
    right_border = random.randint(left_border, number_of_sticks)
    difference = right_border + 1 - left_border
    sticks[left_border - 1: right_border] = '.' * difference
    if right_border < number_of_sticks:
        initial_number = right_border
    elif right_border == number_of_sticks:
        initial_number = 1
        left_border = right_border
    print(f'Бросок {cast + 1}. Сбиты палки с номера {left_border} по номер {right_border}.')

print(f'Результат: {sticks}')








