def slicer(number, number_2):
    answer = tuple()
    count = 0
    for num in number:
        if num == number_2:
            count += 1
        if 1 == count:
            answer += (num,)
        if count == 2:
            answer += (num,)
            break
    print(answer)


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
