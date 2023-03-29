import random


# Создаем классы исключений
class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


# Создаем функцию, которая возвращает количество кармы от 1 до 7 и может выкинуть исключение с вероятностью 1 к 10
def analyzes_the_day():
    # Генерируем случайное число от 1 до 10
    exception_probability_number = random.randint(1, 10)
    # Если число равно 1, то выбрасываем одно из исключений
    if exception_probability_number == 1:
        # Создаем список из классов исключений
        errors = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
        # Выбираем случайный класс из списка
        error = random.choice(errors)
        # Выбрасываем исключение этого класса
        raise error()
    # Иначе возвращаем случайное число от 1 до 7 как количество кармы
    else:
        return random.randint(1, 7)


# Создаем константу для уровня кармы, необходимого для просветления
ENLIGHTENMENT = 500
# Создаем переменную для хранения текущего уровня кармы
karma = 0
# Открываем файл для записи логов об исключениях
log_file = open('karma.log', 'w')

# Создаем бесконечный цикл по набору кармы
while True:
    # Пытаемся вызвать функцию analyzes_the_day() и прибавить ее результат к текущему уровню кармы
    try:
        karma += analyzes_the_day()
        print(f'Текущий уровень кармы: {karma}')
    # Ловим исключения разных классов и записываем их в файл с помощью метода write()
    except KillError:
        log_file.write('KillError\n')
        print('Вы убили живое существо!')
    except DrunkError:
        log_file.write('DrunkError\n')
        print('Вы напились!')
    except CarCrashError:
        log_file.write('CarCrashError\n')
        print('Вы попали в аварию!')
    except GluttonyError:
        log_file.write('GluttonyError\n')
        print('Вы объелись!')
    except DepressionError:
        log_file.write('DepressionError\n')
        print('Вы впали в депрессию!')

    # Проверяем, достиг ли текущий уровень кармы необходимого для просветления значения константы ENLIGHTENMENT
    if karma >= ENLIGHTENMENT:
        # Если да, то выводим сообщение о просветлении и выходим из цикла с помощью оператора break
        print(f'Поздравляем! Вы достигли просветления с уровнем кармы {karma}!')
        break

# Закрываем файл после выхода из цикла с помощью метода close()
log_file.close()
