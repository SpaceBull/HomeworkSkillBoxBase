number_text = {
    0: 'Первая',
    1: 'Вторая',
    2: 'Третья',
    3: 'Четвертая',
    4: 'Пятая',
}
number_text_2 = {
    0: 'Первый',
    1: 'Второй',
    2: 'Третий',
}

roster_city = {}
number_of_countries = int(input('Количество стран: '))
for number in range(number_of_countries):
    country = input(f'{number_text[number]} страна: ').split()
    for city in country[1:]:
        roster_city[city] = country[0]

for number in range(3):
    search_city = input(f'{number_text_2[number]} город: ')
    country = roster_city.get(search_city)
    if country:
        print(f'Город {search_city} расположен в стране {country}.')
    else:
        print(f'По городу {search_city} данных нет.')
