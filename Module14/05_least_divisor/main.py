
def find_the_smallest_divisor(num):
    temp = 1
    for iteration in range(1, num + 1):
        if num % iteration == 0:
            temp = iteration
        if temp > 1:
            print(f'Наименьший делитель, отличный от единицы: {temp}')
            break


number = int(input('Введите число: '))
find_the_smallest_divisor(number)
