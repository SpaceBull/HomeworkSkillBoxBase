def calculating_math_func(data, second_data, base=dict()):
    if second_data not in base:
        if data < second_data:
            for index in range(data, second_data + 1):
                data *= index
                base.update({index: (data / second_data ** 3) ** 10})
            data = second_data
            return base, data
    else:
        return [base[i] for i in range(data, second_data + 1)]


while True:
    first_number = int(input('Введите начальное число: '))
    finish_number = int(input('Введите конечное число: '))
    answer = calculating_math_func(first_number, finish_number)
    print(answer)
    