def do_zip_two(first_data, second_data):
    result = ((first_data[index], second_data[index]) for index in range(min(len(first_data), len(second_data))))
    return result


answer = do_zip_two(first_data=[{'h': 9}, 'b', 'v', 'u'], second_data=(30, {40, }, [90], 'p'))
print(answer) # Если раскрыть генератор, то-> [({'h': 9}, 30), ('b', {40}), ('v', [90]), ('u', 'p')]
