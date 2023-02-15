def records_and_displays_the_message():
    print('╔=================================================================╗')
    print('║                          CryptoChat                             ║')
    print('║                                                                 ║')
    print('║                         ГЛАВНОЕ МЕНЮ.                           ║')
    print('║                                                                 ║')
    print('╚=================================================================╝')

    while True:
        try:
            username = input('Введите имя пользователя: ')
            file_username = username + '.txt'
            print('Выберите одно из действии: \n   1.Посмотреть текущий текст чата. \n   2.Отправить сообщение.')
            action = int(input())
            if action == 1:
                file_message = open(file_username, encoding='utf-8').read().split('\n')
                print('Ваш чат')
                for message in file_message:
                    print('-', message)
            if action == 2:
                with open(file_username, 'a', encoding='utf-8') as username_file:
                    message = input('Пиши: ')
                    username_file.write(message)
                    username_file.write('\n')
        except Exception as exc:
            print('Ваш Чат пустой, напиши сначала ему')
            with open('Error.txt', 'w', encoding='utf-8') as log_file:
                log_file.write(str(exc))


records_and_displays_the_message()
