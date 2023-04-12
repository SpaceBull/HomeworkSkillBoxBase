import os.path


def gen_files_path(address: str, count=0) -> str:
    for root, dirs, files in os.walk(address):
        for file in files:
            if file.endswith('.py'):
                with open(file, 'r', encoding='utf-8') as data_file:
                    for line in data_file.readlines():
                        if '\n' in list(line) and len(list(line)) > 3:
                            count += 1
                    yield count


my_cwd = os.getcwd()
for elem in gen_files_path(address='C:\Skillbox\Basic\Module26'):
    print(elem)
