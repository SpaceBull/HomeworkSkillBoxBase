import random
number = int(input('Количество чисел в списке:  '))
roster_numbers = [random.randint(0, 2) for _ in range(number)]
print(f'Список до сжатия: {roster_numbers}')

num_one = [num for num in roster_numbers if num > 0]
print(f'Список после сжатия: {num_one}')


# num_nol = [num for num in roster_numbers if num == 0]
# num_one.extend(num_nol)
# print(f'Отсортированный список: {num_one}')
