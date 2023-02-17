first_numbers = []
second_numbers = []
new_roster = []
index = 0

for i_number in range(1, 4):
    number_one = int(input(f'Введите {i_number}-е число для первого списка: '))
    first_numbers.append(number_one)

for i_number in range(1, 8):
    number_two = int(input(f'Введите {i_number}-е число для первого списка: '))
    second_numbers.append(number_two)

print(f'Первый список {first_numbers}')
print(f'Второй список {second_numbers}')

new_roster.extend(first_numbers)
new_roster.extend(second_numbers)

for number in first_numbers:
    copy = new_roster.count(number)
    for _ in range(copy - 1):
        new_roster.remove(first_numbers[index])
    index += 1

print(f'Новый первый список с уникальными элементами: {new_roster}')
