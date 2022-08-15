def separate_the_number(number):
  temp = str(number)
  order = ''
  number_mantissa = int(number)
  for symbol in temp:
    order += symbol
    if symbol == '.':
      order = ' '
  fliped_number = flip_the_number(number_mantissa, order)
  return fliped_number


def flip_the_number(mantissa, order_number):
  answer_1 = int(str(mantissa)[::-1])
  answer_2 = int(str(order_number)[::-1])
  answer_temp = answer_2
  count = 0
  while answer_temp != 0:
    answer_temp //= 10
    count += 1
  result = answer_1 + (answer_2 / 10 ** count)
  print(f'Число наоборот: {result}')
  return result


one_number = float(input('Введите первое число: '))
two_number = float(input('Введите второе число: '))
answer_one_number = separate_the_number(one_number)
answer_two_number = separate_the_number(two_number)
answer = answer_one_number + answer_two_number
print(f'Cумма:  {answer}')
