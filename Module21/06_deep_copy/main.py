import copy


def replacing_the_brand_name(copy_struct, brand):
    signboard = f'Сайт для {brand}: '
    copy_struct['html']['head']['title'] = f'Куплю/продам {brand} недорого'
    copy_struct['html']['body']['h2'] = f'У нас самая низкая цена на телефон {brand}'

    return signboard, copy_struct


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

number_of_site = int(input('Сколько сайтов: '))
result = []
for _ in range(number_of_site):
    name_brand = input('\nВведите название продукта для нового сайта: ')
    copy_site = copy.deepcopy(site)
    answer = replacing_the_brand_name(copy_site, name_brand)
    result.append(answer)
    for index_result in result:
        print(f'\n{index_result}')
