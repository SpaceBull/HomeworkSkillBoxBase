numbers_file = open('numbers.txt', 'r')
summ_numbers = 0
print('Содержимое файла numbers.txt')

for symbol in numbers_file:
    print(symbol)
    for i_element in symbol:
        if i_element.isdigit():
            summ_numbers += int(i_element)

numbers_file.close()
answer = open('answer.txt', 'w')
answer.write(str(summ_numbers))
answer.close()
print('Содержимое файла answer.txt')
answer = open('answer.txt', 'r')
for result in answer:
    print(result)
