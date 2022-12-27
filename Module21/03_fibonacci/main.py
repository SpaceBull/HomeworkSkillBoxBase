def counts_the_fibonacci_number(figure):
    if figure < 2:
        return figure
    else:
        return counts_the_fibonacci_number(figure - 1) + counts_the_fibonacci_number(figure - 2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))
result = counts_the_fibonacci_number(number)
print(f'Число: {result}')
