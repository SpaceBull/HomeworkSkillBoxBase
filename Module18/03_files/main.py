name_file = input('Название файла: ')
bad_symbol = '@  №  $  %  ^  &  *  ( )'.split()
begin_word = True
for symbol in bad_symbol:
    if name_file.startswith(symbol):
        begin_word = False
        print('Ошибка: название начинается на один из специальных символов.')

if name_file.endswith('.txt') or name_file.endswith('.docx') and begin_word:
    print('Файл назван верно.')
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
