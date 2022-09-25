alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet = list(alphabet)
new_text = []
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

for symbol in text:
    if symbol not in list(alphabet):
        new_text.append(symbol)
        continue
    index = alphabet.index(symbol)
    index_symbol = index + shift
    if index_symbol >= 32:
        index_symbol = 32 - index_symbol + 1
        new_symbol = alphabet[index_symbol]
        new_text.append(new_symbol)
    else:
        new_symbol = alphabet[index_symbol]
        new_text.append(new_symbol)

result = ''.join(new_text)
print(result)

