import random
max_number = int(input('Введите максимальное число: '))
intended_number_artem = random.randint(1, max_number)
print(f'--Задуманное число Артема-- {intended_number_artem}')

data_false = set()
data_true = set()
while True:
    option = input('Нужное число есть среди вот этих чисел: ').lower().split(' ')
    if option == ['помогите!']:
        data_true.difference_update(data_false)
        print(f'Артём мог загадать следующие числа: {data_true}')
        break
    if str(intended_number_artem) in option:
        data_true = {symbol for symbol in option}
        print('Ответ Артёма: Да', data_true)
    if str(intended_number_artem) not in option:
        data_false = {symbol for symbol in option}
        print('Ответ Артёма: Нет')
