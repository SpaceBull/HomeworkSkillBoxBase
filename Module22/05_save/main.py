import os


def saving_in_a_text_document():
    text = input('Введите строку: ')
    new_path = input('\nКуда хотите сохранить документ?'
                     ' Введите последовательность папок (через пробел): ').split(' ')
    # Users bykovap Skillbox Module22 06_paranoia
    disk_root = os.path.abspath('.').split("\\")[0]
    new_path.insert(0, disk_root)

    new_file = input('\nВведите имя файла: ')
    new_path = '\\'.join(new_path)
    new_address = os.path.join(new_path, new_file)

    if not os.path.exists(new_address):
        open_file = open(new_address, 'w', encoding='utf8')
        open_file.write(text)
        open_file.close()
        print('Файл успешно сохранён!')
    else:
        overwrite = input('Вы действительно хотите перезаписать файл? ').lower()
        if overwrite == 'да':
            open_file = open(new_address, 'w', encoding='utf8')
            open_file.write(text)
            open_file.close()
            print('Файл успешно перезаписан!')
        else:
            pass
    return new_address


result = saving_in_a_text_document()
result = open(result, 'r', encoding='utf8')
print(f'\nСодержимое файла: ')
for text in result:
    print(text)
result.close()