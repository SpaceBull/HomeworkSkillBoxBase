from typing import Callable, Any
import functools


def counter(func: Callable) -> Any:
    """
    Декоратор counter, считает кол-во вызовов обёртки (декоратора).
   """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        counter.count += 1
        temp = func(*args, **kwargs)
        print(f'Функция {func.__name__} вызвана: {counter.count} раз')
        return temp
    counter.count = 0
    return wrapped_func


@counter
def test() -> Any:
    print('test')


test()
test()
