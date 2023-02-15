import random

result = 0
try:
    with open('out_file.txt', 'w', encoding='utf-8') as out_file:
        while True:
            number = input('Введите число: ')
            if number.isdigit():
                fortuna = random.randint(1, 13)
                if fortuna == 1:
                    raise BaseException('Вас постигла неудача!')
                out_file.write(number)
                out_file.write('\n')
                result += int(number)
                if result >= 777:
                    raise BaseException('Вы успешно выполнили условие для выхода из порочного цикла!')
            else:
                raise TypeError('Вводите цифры!')
except TypeError as exc:
    print(exc)
except BaseException as exc:
    print(exc)
finally:
    print('Содержимое файла out_file.txt:')
    file = open('out_file.txt').read().split('\n')
    for number in file:
        print(number)





