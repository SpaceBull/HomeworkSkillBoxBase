line_number = {
    1: 'первая',
    2: 'вторая',
    3: 'третья'
}
data_pairs = {}
number_of_pairs = int(input('Введите количество пар слов: '))
for pairs in range(number_of_pairs):
    data = input(f'{line_number[pairs + 1]} пара: ').split()
    data.remove('-')
    data_pairs[data[0]] = data[1]

flag = True
while flag:
    word = input('Введите слово: ').title()
    for key, value in data_pairs.items():
        if key in word:
            print(f'Cиноним: {value}')
            flag = False
            break
        if value in word:
            print(f'Cиноним: {key}')
            flag = False
            break
    else:
        print('Такого слова в словаре нет.')
