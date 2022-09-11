first_rank = list(range(160, 176 + 1, 2))
second_rank = list(range(162, 180 + 1, 3))

new_rank = []
new_rank.extend(first_rank)
new_rank.extend(second_rank)
new_rank.sort(reverse=False)
print(f'Отсортированный список учеников: {new_rank}')

