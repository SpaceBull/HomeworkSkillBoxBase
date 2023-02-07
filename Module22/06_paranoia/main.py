import os


def start():
    current_folder = os.path.abspath(os.path.join('cipher_text.txt.'))
    new_entry = open(current_folder, 'w', encoding='utf8')
    alphabet_england = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_england = list(alphabet_england)
    file = open('text.txt', 'r', encoding='utf8')
    print('Содержимое файла text.txt: ')
    for number_word, word in enumerate(file):
        new_text = []
        print(word, end='')
        for letter in word:
            if letter.lower() in alphabet_england:
                number_index_letter = alphabet_england.index(letter.lower())
                number_index_letter += number_word + 1  #А если это 30 буква?расписать
                new_text.append(alphabet_england[number_index_letter])
        new_text_str = ''.join(new_text)
        new_entry.write(str(new_text_str) + '\n')
    new_entry.close()
    print('\n')
    print('\nСодержимое файла cipher_text.txt.: ')
    read_file = open('cipher_text.txt.', 'r', encoding='utf8')
    for word in read_file:
        print(word.title(), end='')


start()

