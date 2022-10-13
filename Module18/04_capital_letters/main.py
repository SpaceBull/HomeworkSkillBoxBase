text = input('Введите строку: ').split()
result = [word.title() for word in text]
result = ' '.join(result)
print(f'Результат: {result}')
