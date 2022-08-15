def find_the_smallest_divisor(num):
    temp = 1
    for i in range(1, num + 1):
        if num % i == 0:
            temp = i
        if temp > 1:
            print(f'Наименьший делитель, отличный от единицы: {temp}')
            break


number = int(input('Введите число: '))
find_the_smallest_divisor(number)
