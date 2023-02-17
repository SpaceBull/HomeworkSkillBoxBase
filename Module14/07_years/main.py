def count_special_dates(one_number, two_number):
    for year in range(one_number, two_number + 1):
        number_one = year // 1000
        number_two = year // 100 % 10
        number_three = year // 10 % 10
        number_four = year % 10
        if number_one == number_two == number_three \
                or number_two == number_three == number_four \
                or number_three == number_four == number_one \
                or number_one == number_two == number_four:
            print(year)


first_number = int(input('Введите первый год: '))
second_number = int(input('Введите второй год: '))
print(f'Года от {first_number} до {second_number} с тремя одинаковыми цифрами:')
count_special_dates(first_number, second_number)
