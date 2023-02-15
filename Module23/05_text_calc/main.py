calculate_file = open('calc.txt', encoding='utf-8').read().split('\n')
arithmetic_symbols = ['+', '-', '/', '//', '*', '%']
result = 0
for operation in calculate_file:
    try:
        split_operation = operation.split(' ')
        if split_operation[1] in arithmetic_symbols:
            number = ''.join(split_operation)
            answer = eval(number)
            result += answer
        else:
            mathematical_example = ''.join(split_operation)
            raise BaseException(f'Обнаружена ошибка в строке: {mathematical_example}')
    except BaseException as exc:
        print(exc)
        correction = input('Хотите исправить?').lower()
        if correction == 'да':
            corrected_version = input('Введите исправленную строку: ')
            answer = eval(corrected_version)
            result += answer
        else:
            continue

print(f'Сумма результатов: {result}')
