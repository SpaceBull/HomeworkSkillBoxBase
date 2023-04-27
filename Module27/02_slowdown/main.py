from typing import Callable, Any
import functools
import threading


def timer(my_func: Callable) -> Any:
    """
   Декоратор timer, выводит функцию header, каждые 5 секунд.
    """
    @functools.wraps(my_func)
    def wrapped_func(*args, **kwargs):
        threading.Timer(5.0, header).start()
        my_func(*args, **kwargs)
        return my_func
    return wrapped_func


@timer
def header() -> Any:
    print('Title, html')


print(timer.__doc__)
header()
