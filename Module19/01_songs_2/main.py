violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

number_text = {
    1: 'первой',
    2: 'второй',
    3: 'третьей',
    4: 'четвертой',
    5: 'пятой',
    6: 'шестой',
    7: 'седьмой'
}
answer = 0
number_of_songs = int(input('Сколько песен выбрать? '))
for number in range(1, number_of_songs + 1):
    song = input(f'Название {number_text[number]} песни: ')
    answer += violator_songs[song]


print(f'Общее время звучания песен: {answer} минуты')
