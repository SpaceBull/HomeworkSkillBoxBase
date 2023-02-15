import random


def adding_numbers_to_coordinates(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return x / y


def subtract_the_numbers(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return y / x


try:
    with open('coordinates.txt', 'r') as file_coordinates, open('result.txt', 'w') as file_answer:
        for line in file_coordinates:
            nums_list = line.split()
            result_adding = adding_numbers_to_coordinates(int(nums_list[0]), int(nums_list[1]))
            result_subtract = subtract_the_numbers(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([result_adding, result_subtract, number])
            file_answer.write(''.join(str(my_list)))
            file_answer.write('\n')
except ZeroDivisionError as exc:
    print(exc, type(exc))

