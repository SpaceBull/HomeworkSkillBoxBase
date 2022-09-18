import random
number = int(input('Enter the number: '))
answer = [random.randint(1, 20) for random_number in range(number)]
new_answer = [1 if x % 2 == 0 else answer[x] % 5 for x in range(len(answer))]

print('Result: ', answer)
print('New Result: ', new_answer)



