roster = dict()
count = 0
number_of_protocols = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
for number in range(1, number_of_protocols + 1):
    count += 1
    result_and_name = input(f'{number}-я запись: ').split()
    for name, score in roster.items():
        if result_and_name[1] == name and int(score[0]) >= int(result_and_name[0]):
            break
    else:
        roster[result_and_name[1]] = (int(result_and_name[0]), count)
# roster = {'Jack': (95715, 6), 'qwerty': (197128, 5), 'Alex': (95715, 3), 'M': (95715, 9)}
# Вторая часть задачи решена не в самом лучше свете, это то что пришло в голову...)
if len(roster) > 2:
    count_2 = 1
    print('Итоги соревнований:')
    win = max(roster.items())
    print(f'{count_2}-e место. {win[0]} {win[1][0]}', end='\n')
    roster.pop(win[0])
    winners = sorted(roster.items(), reverse=False)
    for number, key in enumerate(winners):
        count_2 += 1
        if number == 2:
            break
        else:
            print(f'{count_2}-e место. {key[0]} {key[1][0]}', end='\n')

else:
    print('Игроков не может быть меньше 3-ех!')
