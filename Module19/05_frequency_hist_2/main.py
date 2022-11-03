text = input('Введите текст: ').lower()
result = dict()
data = {}

for symbol in text:
    if symbol in result:
        result[symbol] += 1
    else:
        result[symbol] = 1

for i in sorted(result.keys()):
    data[i] = result[i]

for key, value in data.items():
    print(f'{key}:{value}')

one_symbol = {symbol for symbol in data.keys() if data[symbol] == 1}

two_symbol = {symbol for symbol in data.keys() if data[symbol] == 2}
three_symbol = {symbol for symbol in data.keys() if data[symbol] == 3}
print(f'\nИнвертированный словарь частот: \n{one_symbol} \n{two_symbol} \n{three_symbol}')


#Не стал ставить скобки, от списков (так как ПР - на словари)