from typing import Callable, Any
import functools


def decorator_with_args_for_any_decorator(decorated_decorator: Callable) -> Callable: # оболочка Декоратора
    """
    Декорирует декоратор. Даёт возможность любому декоратору принимать произвольные аргументы.
    """
    @functools.wraps(decorated_decorator)  # Декорируемый декоратор
    def wrapped(*args, **kwargs): # Аргументы от @decorated_decorator(..,аргументы,..)
        def decorated_decorator(func): # Открывает функцию
            def wrapper(*decorated_decorator_args, **decorated_decorator_kwargs): # Cодержимое функции
                print(f'Переданные арги и кварги в декоратор: {args, kwargs}')
                result = func(*decorated_decorator_args, **decorated_decorator_kwargs) # запускает содержимое функции
                return result
            return wrapper
        return decorated_decorator
    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Any:
    """
    Декоратор функции. Вызывает(декорирует) содержимое функции
    """
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        result = func(*func_args, **func_kwargs)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
