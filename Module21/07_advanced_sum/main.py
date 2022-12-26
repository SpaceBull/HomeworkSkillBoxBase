def advanced_sum_function(numbers_list, answer):
    if isinstance(numbers_list, tuple):
        answer = [number for number in numbers_list]
        return sum(answer)
    if isinstance(numbers_list, list):
        for number in numbers_list:
            if not isinstance(number, list):
                answer.append(number)
            advanced_sum_function(number, answer)
    return sum(answer)


tuple_numbers = advanced_sum_function((1, 2, 3, 4, 5), answer=[])
list_numbers = advanced_sum_function(([[1, 2, [3]], [1], 3]), answer=[])
print(tuple_numbers)
print(list_numbers)
