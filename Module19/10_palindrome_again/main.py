def get_input_parameters():
    text = input('Введите строку: ')
    return text


def display_result(text_palindrome):
    if text_palindrome:
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')


def check_palindrome(old_word):
    temp_old_word = list(old_word)
    for _ in range(len(temp_old_word)):
        letter = temp_old_word.pop()
        temp_old_word.insert(0, letter)
        word_palindrome = temp_old_word[::-1]
        if word_palindrome == temp_old_word:
            word_palindrome = True
            return word_palindrome


if __name__ == '__main__':
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
