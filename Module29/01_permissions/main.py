import functools
from typing import Callable, Any


def check_permission(person: str) -> Any:
    """Декоратор для проверки прав пользователя.
    Возвращает ошибку или право доступа к функции"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if person == ''.join(user_permissions):
                    return func(*args, **kwargs)
                raise PermissionError
            except PermissionError:
                print('У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return wrapper
    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
