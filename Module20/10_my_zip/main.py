text = 'abcd'
set_number = (10, 20, 30, 40)

answer = ((text[index], set_number[index]) for index in range(min(len(text), len(set_number))))
print(answer)
for pairs in answer:
    print(pairs)

print('Все остальные виды ')
answer = [{text[index], set_number[index]} for index in range(min(len(text), len(set_number)))]
print(answer)

answer = [{text[index]: set_number[index]} for index in range(min(len(text), len(set_number)))]
print(answer)

answer = [(text[index], set_number[index]) for index in range(min(len(text), len(set_number)))]
print(answer)

answer = [[text[index], set_number[index]] for index in range(min(len(text), len(set_number)))]
print(answer)

zipped = dict(zip(text, set_number))
print(zipped)

zipped = set(zip(text, set_number))
print(zipped)

zipped = list(zip(text, set_number))
print(zipped)
