first_line = input('Первая строка: ')
second_line = input('Вторая строка: ')
count_letter = len(first_line)
shift = 0

first_roster = [letter for letter in first_line]
second_roster = [letter for letter in second_line]

while count_letter != 0:
    shift += 1
    letter = second_roster[len(second_roster) - 1]
    copy_letter = letter
    second_roster.remove(letter)
    second_roster.insert(0, copy_letter)
    count_letter -= 1
    if second_roster == first_roster:
        print(f'Первая строка получается из второй со сдвигом {shift}.')
        break
    if count_letter == 0:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
