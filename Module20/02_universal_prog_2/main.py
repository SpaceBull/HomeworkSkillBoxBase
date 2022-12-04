def data_processing(entering):
    return [symbol for prime_numbers, symbol in enumerate(entering)
            if prime_numbers in filters_for_prime_numbers(entering)]


def filters_for_prime_numbers(enter):
    number_of_characters = len(enter)
    index_letters = []
    for digit_letters in range(2, number_of_characters):
        for number_index in index_letters:
            if digit_letters % number_index == 0:
                break
        else:
            index_letters.append(digit_letters)
    return index_letters


print(data_processing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(data_processing((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(data_processing('О Дивный Новый мир!'))
