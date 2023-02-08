file = open('text.txt', 'r', encoding='utf-8')
all_letters = [letter.lower() for word in file for letter in word if letter.isalpha()]


file = open('text.txt', 'r', encoding='utf-8')
sort_letters = {letter.lower() for word in file for letter in word if letter.isalpha()}


file = open('text.txt', 'r', encoding='utf-8')
result = {}
for letter in sort_letters:
    fraction = all_letters.count(letter) / len(all_letters)
    result[letter] = round(fraction, 3)


new_file = open('analysis.txt', 'w', encoding='utf-8')
sorted_rooms = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
for key_letter, value_fraction in sorted_rooms.items():
    new_file.write(key_letter + ' ' + str(value_fraction) + '\n')

new_file.close()


