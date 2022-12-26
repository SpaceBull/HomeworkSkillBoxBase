def the_hanoi_towers_algorithm(disks, start, finish):
    if disks <= 0:
        return
    temp = 6 - start - finish
    the_hanoi_towers_algorithm(disks - 1, start, temp)
    print(f'Переложить диск {disks} со стержня номер {start} на стержень номер {finish}')
    the_hanoi_towers_algorithm(disks - 1, temp, finish)


number_of_disks = int(input('Введите количество дисков: '))
the_hanoi_towers_algorithm(number_of_disks, 1, 3)
