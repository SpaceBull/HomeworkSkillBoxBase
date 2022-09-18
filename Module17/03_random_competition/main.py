import random

first_command = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_command = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [first_command[index]
           if first_command[index] > second_command[index]
           else second_command[index]
           for index in range(20)]

print(f'first command: {first_command}')
print(f'second command: {second_command}')
print(f'Tour Winners:{winners}')
