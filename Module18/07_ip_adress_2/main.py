text = input('Сообщение: ').split()
new_text = []
for word in text:
    if not word.isalpha():
        symbol = word[len(word) - 1]
        copy_symbol = symbol
        temp_word = [letter for letter in word]
        temp_word.remove(symbol)
        temp_word = temp_word[::-1]
        temp_word.insert(len(word) - 1, copy_symbol)
        word = ''.join(temp_word)
        new_text.append(word)
    else:
        new_text.append(word[::-1])

answer = ' '.join(new_text)
print(f'Новое сообщение: {answer}')
