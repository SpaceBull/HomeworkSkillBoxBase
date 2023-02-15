with open('people.txt', 'r', encoding='utf8') as file, open('errors.log', 'w', encoding='utf8') as log_file:
    count = 0

    for line, name in enumerate(file):
        try:
            name = name.rstrip()
            count += len(name)
            if len(name) < 3:
                raise BaseException(f'Ошибка: менее трёх символов в строке {line + 1}.')
        except BaseException as exc:
            print(exc)
            log_file.write(str(exc))

    print(f'Общее количество символов: {count}')

