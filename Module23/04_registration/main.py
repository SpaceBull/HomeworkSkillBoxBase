data_file = open('registrations.txt', encoding='utf-8').read().split('\n')
with open('registrations_good.log', 'w', encoding='utf-8') as registrations_good_file,\
        open('registrations_bad.log', 'w', encoding='utf-8') as registrations_bad_file:
    for line in data_file:
        split_line = line.split(' ')
        try:
            if len(split_line) == 3:
                if split_line[0].isalpha():
                    if '.' and '@' in split_line[1]:
                        if 99 > int(split_line[2]) > 10:
                            registrations_good_file.write(' '.join(split_line))
                            registrations_good_file.write('\n')
                        else:
                            raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
                    else:
                        raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
                else:
                    raise NameError('Поле имени содержит НЕ только буквы')
            else:
                raise IndexError('НЕ присутствуют все три поля')
        except Exception as exc:
            registrations_bad_file.write(str(' '.join(split_line)) + ' -- ' + str(exc))
            registrations_bad_file.write('\n')
        else:
            pass




