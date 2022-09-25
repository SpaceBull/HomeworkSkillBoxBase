text = input('Введите текст: ')
letter = input('Введите букву: ')
text_index = []
count = 0

count_letter = text.count(letter)
first_index = list(text).index(letter) + 1

if count_letter >= 2:
    for symbol in text:
        if symbol == letter:
            text_index.append(count)
        count += 1
    text = text[first_index:text_index[1]]
    print(f'Развёрнутая последовательность между первым и последним {letter} : {text[::-1]}')
else:
    print('Буква должна встречаться минимум - 2 раза')
