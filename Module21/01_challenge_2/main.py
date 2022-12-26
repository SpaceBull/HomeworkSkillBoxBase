def outputs_the_numbers_in_order(first_number):
    if first_number == 0:
        return first_number
    else:
        outputs_the_numbers_in_order(first_number - 1)
        print(first_number)


number = int(input('Введите число:'))
outputs_the_numbers_in_order(number)
