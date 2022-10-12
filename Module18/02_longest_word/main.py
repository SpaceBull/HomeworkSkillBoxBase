word = input('Введите строку: ').split()
number_of_letters = 1
long_word = ''
for text in word:
    if number_of_letters <= len(text):
        number_of_letters = len(text)
        long_word = text

print(f'Самое длинное слово: {long_word}')
print(f'Длина этого слова: {len(long_word)}')