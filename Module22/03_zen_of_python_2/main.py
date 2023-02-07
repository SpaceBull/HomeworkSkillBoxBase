import os
path = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
file_zen = open(path, 'r', encoding='utf8')


count_of_letter = 0
count_of_word = 0
data = []


for word in file_zen:
    summ_word = len(word.split(' '))
    count_of_word += int(summ_word)
    for letter in word:
        if letter.isalpha():
            data.append(letter.lower())


count = sorted([(data.count(letter), letter) for letter in data], reverse=False)
print(f'Количество букв в файле:', len(''.join(data)))
print(f'Количество cлов в файле: {count_of_word}')
file_zen = open(path, 'r', encoding='utf8')
print(f'Количество строк в файле: {len(list(file_zen))}')
print(f'Наиболее редкая буква: {count[0][1]}')
file_zen.close()