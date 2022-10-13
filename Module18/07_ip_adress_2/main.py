ip_address = input('Введите IP: ')
dot = ip_address.count('.')
answer = False
if dot == 3:
    for number in ip_address.split('.'):
        if not number.isdigit():
            print(f'{number} — это не целое число.')
            break
        if int(number) > 255:
            print(f'{number} превышает 255.')
            break
        if int(number) < 0:
            print(f'{number} меньше 0.')
            break
        if number.isdigit():
            answer = True
else:
    print('Адрес — это четыре числа, разделённые точками.')

if answer:
    print('IP-адрес корректен.')
