
def the_sum_of_all_the_digits_in_the_number(summ_number):
    answer_summ_number = 0
    while summ_number != 0:
        result = summ_number % 10
        summ_number //= 10
        answer_summ_number += result
    print(f'Сумма чисел: {answer_summ_number}')
    counts_the_number_of_digits_in_a_number(number, answer_summ_number)


def counts_the_number_of_digits_in_a_number(number_of_digits, answer_summ_number):
    count = 0
    while number_of_digits != 0:
        number_of_digits //= 10
        count += 1
    print(f'Количество цифр: {count}')
    result = answer_summ_number - count
    print(f'Разность суммы и количества цифр: {result}')


number = int(input('Введите число: '))
answer_summ_number = the_sum_of_all_the_digits_in_the_number(number)






