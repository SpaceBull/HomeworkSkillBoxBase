count = 0
main_registry = [1, 5, 3]
one_roster = [1, 5, 1, 5]
two_roster = [1, 3, 1, 5, 3, 3]

main_registry.extend(one_roster)
number_five = main_registry.count(5)
print(f'Кол-во цифр 5 при первом объединении: {number_five}')

for i_main_registry in main_registry:
    if i_main_registry == 5:
        main_registry.pop(count)
    count += 1

main_registry.extend(two_roster)
number_three = main_registry.count(3)
print(f'Кол-во цифр 3 при втором объединении: {number_three}')
print(f'Итоговый список: {main_registry}')

