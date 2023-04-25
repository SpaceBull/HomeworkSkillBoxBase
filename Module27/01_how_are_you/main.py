from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор how_are_you. Спрашивает "как дела?" и отвечает.
    """
    @functools.wraps(func)
    def wrapped_question() -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func()
    return wrapped_question


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
print(how_are_you.__doc__)
