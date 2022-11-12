number_of_orders = int(input('Введите количество заказов: '))
number_text = {
    1: 'Первый',
    2: 'Второй',
    3: 'Третий',
    4: 'Четвертый',
    5: 'Пятый',
    6: 'Шестой'
}
roster = {}
for number_order in range(number_of_orders):
    order = input(f'{number_text[number_order + 1]} заказ: ').split()
    flag = True
    if order[0] in roster:
        for key_surname, value_pizza in roster.items():
            if order[1] in value_pizza and order[0] == key_surname:
                for num in value_pizza.values():
                    summ_pizza = int(num) + int(order[2])
                    roster[order[0]].update({order[1]: summ_pizza})
                    flag = False
                    break
            else:
                if flag:
                    roster[order[0]].update({order[1]: order[2]})
                    break
    else:
        roster[order[0]] = {order[1]: order[2]}

for surname, order_value in sorted(roster.items()):
    print(surname)
    for pizza, number in sorted(order_value.items()):
        print(f'     {pizza}: {number}')
