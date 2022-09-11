guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    print('Гость пришёл или ушёл?')
    action = input('')
    if action == 'пришёл':
        name_new_guest = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(name_new_guest)
            print(f'Привет, {name_new_guest}!')
        else:
            print(f'Прости, {name_new_guest}, но мест нет.')
    if action == 'ушёл':
        name_guest = input('Имя гостя: ')
        if name_guest not in guests:
            print('Такого гостя нет!')
        else:
            guests.remove(name_guest)
            print(f'Пока, {name_guest}')
    if action == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
