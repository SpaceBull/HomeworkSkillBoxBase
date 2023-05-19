import time
from datetime import datetime
import functools


def timer(func, cls, date_time):
    """
    Функция timer обёртка от log_methods,
    которая преобразует дату и фиксирует затраченное время на выполнение методов класса.
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        new_date = ['%' + letter if letter.isalpha() else letter for letter in date_time]
        new_date_symbol = ''.join(new_date)
        now = datetime.now()
        print(f'Запускается {cls.__name__}.{func.__name__}. Дата и время запуска: {now.strftime(new_date_symbol)}.')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Завершение {cls.__name__}.{func.__name__}, время работы = {round(end - start, 3)} s. ')
        return result
    return wrapper


def log_methods(date_time: str):
    """
    Декоратор класса.
    Получает параметры даты и фиксирует время с помощью функции timer применяет его ко всем методам класса.
    """
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = timer(cur_method, cls, date_time)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@log_methods('b d Y - H:M:S')
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods('b d Y - H:M:S')
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("Наследник test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
