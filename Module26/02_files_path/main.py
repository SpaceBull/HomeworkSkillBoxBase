import os


def gen_files_path(adress: str) -> str:
    for root, dirs, files in os.walk(adress):
        result = f'Директория: \t{root}, -- папка: {dirs}, -- файлы: {files} '
        yield result


for elem in gen_files_path(adress='C:\Skillbox\Basic'):
    print(elem)
