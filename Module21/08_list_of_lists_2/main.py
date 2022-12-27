roster = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
          [[11, 12, 13], [14, 15], [16, 17, 18]]]


def advanced_sum_function_2(numbers_list, answer):
    if isinstance(numbers_list, list):
        for number in numbers_list:
            if not isinstance(number, list):
                answer.append(number)
            advanced_sum_function_2(number, answer)
    return answer


list_numbers = advanced_sum_function_2(roster, answer=[])
print(list_numbers)
