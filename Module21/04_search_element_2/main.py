
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_value(website, key, count_depth):
    if key in website:
        return website[key]
    for branch in website.values():
        count_depth -= 1
        if isinstance(branch, dict):
            result = search_value(branch, key, count_depth)
            if result and count_depth >= 1:
                break
    else:
        result = None
    return result


def input_data():
    the_desired_value = input('Искомый ключ: ')
    question_max_depth = input('Хотите ввести максимальную глубину? Y/N:').lower()
    if question_max_depth == 'n':
        answer = search_value(site, the_desired_value, 100)
        if answer:
            print(f'Значение ключа: {answer}')
        else:
            print('Такого ключа в структуре сайта нет')

    if question_max_depth == 'y':
        max_depth = int(input('Введите максимальную глубину:'))
        answer = search_value(site, the_desired_value, max_depth)
        if answer:
            print(f'Значение ключа: {answer}')
        else:
            print('Такого ключа в структуре сайта нет')


input_data()
