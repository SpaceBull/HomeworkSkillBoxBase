number_of_friends = int(input('Кол-во друзей: '))
debt_receipts = int(input('Долговых расписок: '))
friend_summ = []


for i in range(1, number_of_friends + 1):
    friend_summ.append(i)
    summ = friend_summ.index(i)
    friend_summ.insert(summ + 1, 0)


for i_debt in range(debt_receipts):
    print(f'{i_debt + 1}-я расписка')
    whom = int(input('Кому? '))
    from_whom = int(input('От кого? '))
    if whom == from_whom:
        print('Ты не можешь взять в долг сам у себя')
        break
    how_many = int(input('Сколько? '))
    index_debt = friend_summ.index(whom)
    friend_summ[index_debt + 1] -= how_many
    index_beneficiary = friend_summ.index(from_whom)
    friend_summ[index_beneficiary + 1] += how_many

print('Баланс друзей: ')
count = 1
for i_many in range(1, len(friend_summ) + 1, 2):
    print(f'{count}: {friend_summ[i_many]}')
    count += 1
