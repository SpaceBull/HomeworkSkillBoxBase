number_of_skates = int(input('Кол-во коньков: '))
skates = []

for couple in range(number_of_skates):
    pair_size = int(input(f'Размер {couple + 1}-й пары: '))
    skates.append(pair_size)

number_of_people = int(input('Кол-во людей: '))
foot_sizes = []

for people in range(number_of_people):
    size = int(input(f'Размер ноги {people + 1}-го человека: '))
    foot_sizes.append(size)

skates.sort(reverse=True)
foot_sizes.sort(reverse=True)
for i_foot in foot_sizes:
    for i_skates in skates:
        if i_skates >= i_foot:
            skates.remove(i_skates)

print(f'Наибольшее кол-во людей, которые могут взять ролики: {number_of_people - len(skates)}')
