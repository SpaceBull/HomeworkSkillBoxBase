file = open('first_tour.txt').read().split('\n')
temp_scores = 0
data = []

print('Содержимое файла first_tour.txt: ')
for index, elem in enumerate(file):
    roster_str = elem.split(' ')
    print(elem, end='\n')
    if index == 0:
        temp_scores = roster_str
    else:
        if int(roster_str[2]) > int(temp_scores[0]):
            abbreviated_name = ''.join(list(roster_str[1][0] + '.'))
            word = abbreviated_name, roster_str[0], roster_str[2]
            data.append(word)


new_file = open('second_tour.txt', 'w', encoding='utf8')
data = sorted(data, reverse=True)
new_file.write(str(len(data)))
new_file.write('\n')
for index, card_person in enumerate(data):
    new_file.write(str(f'{index + 1}) '))
    new_file.write(str(' '.join(card_person)))
    new_file.write('\n')
new_file.close()


print('\nСодержимое файла second_tour.txt: ')
read_new_file = open('second_tour.txt', 'r', encoding='utf8')
for person in read_new_file:
    print(person, end='')

read_new_file.close()
