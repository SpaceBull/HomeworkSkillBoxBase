text = input('Введите строку: ')
text = [letter for letter in text]
copy_text = text[:]
copy_text += '!'
index = -1
roster_letters = []
result_letters = []
answer = []
result = []

for letter in text:
    roster_letters.append(letter)
    index += 1
    if copy_text[index] != copy_text[index + 1]:
        result_letters.append(roster_letters)
        roster_letters = []

for letter in result_letters:
    str_letter = letter[0]
    count_letter = str(len(letter))
    answer = str_letter + count_letter
    result += answer
    result = ''.join(result)

print(f'Закодированная строка: {result}')
