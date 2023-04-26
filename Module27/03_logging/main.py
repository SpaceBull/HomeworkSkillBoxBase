from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> Any:
    """
    Декоратор logging, отвечает за логирование функций.
    """
    print(func.__doc__)

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        file = open('function_errors.log', 'a', encoding='utf-8')
        temp = func(*args, **kwargs)
        datetime_now = datetime.datetime.now()
        file.write('\nФункция - {func}, Ошибка! - {temp}, Время: {datetime_now}\n'.format(func=func.__name__,
                                                                                          temp=str(temp),
                                                                                          datetime_now=datetime_now))
        file.close()
        return file
    return wrapped_func


@logging
def division() -> Any:
    """
    Функция division, делит 2 числа
    """
    try:
        answer = 8 / 0
    except BaseException as answer:
        return answer


@logging
def folding() -> Any:
    """
    Функция folding, складывает 2 числа
    """
    try:
        answer = 5 + '4'
    except BaseException as answer:
        return answer


division()
folding()
