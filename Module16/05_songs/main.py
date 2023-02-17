violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

time_song = 0
number_of_songs = int(input('Введите кол-во песен: '))
for number in range(1, number_of_songs + 1):
    print(f'Название {number}-й песни: ')
    song = input('')
    for i_song in violator_songs:
        if i_song[0] == song:
            time_song += i_song[1]


time_song = (round(time_song, 2))
print(f'Общее время звучания песен: {time_song} минуты')

