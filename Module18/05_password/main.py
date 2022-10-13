while True:
    password = input('Придумайте пароль: ')
    digits_in_the_password = len([number for number in password if number.isdigit()])
    if len(password) > 8 and password.islower() != True and digits_in_the_password >= 3:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
