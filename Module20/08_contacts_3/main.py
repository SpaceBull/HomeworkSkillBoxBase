def displays_the_main_menu():
    print(
        'Введите номер действия: \
       \n1. Добавить контакт\
       \n2. Найти человека '
    )
    action_number = int(input())
    if action_number == 1:
        adds_a_contact()
    if action_number == 2:
        finds_a_person()


def adds_a_contact():
    sur_name = input('Введите имя и фамилию нового контакта (через пробел): ').title().split()
    surname, name = sur_name
    if (surname, name) in roster:
        print('Такой человек уже есть в контактах.')
    else:
        number_phone = int(input('Введите номер телефона: '))
        roster[(surname, name)] = number_phone
    print(f'Текущий словарь контактов: {roster}')
    displays_the_main_menu()


def finds_a_person():
    search_surname = input('Введите фамилию для поиска: ').title()
    for surname, number_phone in roster.items():
        if search_surname == surname[1]:
            print(f'{surname[0]} {surname[1]} {number_phone}')
            break
    else:
        print('Такого человека у нас нет')
        displays_the_main_menu()


roster = {}
displays_the_main_menu()