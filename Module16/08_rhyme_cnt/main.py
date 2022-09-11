number_of_people = int(input('Введите кол-во людей: '))
count_people = int(input('Какое число в считалке? '))
roster_people = list(range(1, number_of_people + 1))

print(f'Значит, выбывает каждый {count_people}-й человек')

while len(roster_people) != 1:
    print(f'Текущий круг людей: {roster_people}')
    start_num = int(input(f'Начало счёта с номера '))
    start_index = roster_people.index(start_num)
    answer = roster_people[(count_people + start_index - 1) % len(roster_people)]
    print(f'Выбывает человек под номером {answer}')
    roster_people.remove(answer)
    print(' ')

print(f'Остался человек под номером {roster_people[0]}')

