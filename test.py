import os


def write_homework(address_path, homework_file, new_file):
    for elem in os.listdir(address_path):
        path = os.path.join(address_path, elem)
        if elem == homework_file:
            address_true = open(path, 'r', encoding='utf8')
            new_file.write(f'\n{path}')
            new_file.write('\n')
            for sym in address_true:
                new_file.write(f'{str(sym)}')
            new_file.write('\n')
            new_file.write('#' * 40)
        if os.path.isdir(path):
            result = write_homework(path, homework_file, new_file)
            if result:
                 break


open_new_file = os.path.abspath(os.path.join('homework_SCRIPT.txt'))
file = open(open_new_file, 'w', encoding='utf8')
search_path = os.path.abspath(os.path.join(''))
homework_name_file = ('main.py')
write_homework(search_path, homework_name_file, file)
file.close()

