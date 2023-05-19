import functools
from typing import Callable, Any


def callback(url: str) -> Any:
    """
    Функция, которая вызывается при срабатывании определённого события:
    переходе на страницу, получении сообщения или окончании обработки процессором.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Вызвана функция {func.__name__} по url-адресу {url}')
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {'//': example}
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')