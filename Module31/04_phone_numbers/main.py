import re

roster = ['9999999999', '999999-999', '99999x9999']
word_number = ['первый', 'второй', 'третий', 'четвертый', 'пятый', 'шестой']

for index_word, number in enumerate(roster):
    if re.findall(r'[8-9]\d{9}', number):
        print(f'{word_number[index_word]} номер: всё в порядке')
    else:
        print(f'{word_number[index_word]} номер: не подходит')
