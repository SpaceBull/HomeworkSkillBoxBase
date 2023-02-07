import os


def print_dirs(project, size_file, subdir):
    for i_elem in os.listdir(project):
        new_path = os.path.join(project, i_elem)
        if os.path.isdir(new_path):
            subdir.append(new_path)
            print_dirs(new_path, size_file, subdir)
        elif os.path.isfile(new_path):
            size = os.path.getsize(new_path)
            size_file.append(size)
    return size_file, subdir


sum_size_file = []
subdirectories = []
address = os.path.abspath(os.path.join('..', '..', 'Module14'))
print(address)
sum_size, subdir = print_dirs(address, sum_size_file, subdirectories)
print(f'Размер каталога (в Кб): {sum(sum_size) / 1024}')
# subdirectories = [directories for directories in os.listdir(address) if os.path.isdir(os.path.join('..', directories))]
# print(f'Количество подкаталогов: {len(subdirectories)}')
print(f'Количество подкаталогов: {len(subdirectories)}')
print(f'Количество файлов: {len(sum_size)}')

