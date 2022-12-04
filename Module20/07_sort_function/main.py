def sorts_the_tuple(numbers):
    answer = tuple()
    flag = False
    for number in numbers:
        if type(number) == int:
            answer = sorted(numbers)
            flag = True
        else:
            return numbers
    if flag:
        answer = tuple(answer)
        return answer


print(sorts_the_tuple((6, 3, -1, 8, 4, 10, -5)))
