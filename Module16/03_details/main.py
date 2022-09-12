shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

summ_details = 0
part_search = input('Название детали: ')
count_details = 0

for i_shop in shop:
    if i_shop[0] == part_search:
        count_details += 1
        summ_details += i_shop[1]

print(f'Кол-во деталей — {count_details}')
print(f'Общая стоимость — {summ_details}')

