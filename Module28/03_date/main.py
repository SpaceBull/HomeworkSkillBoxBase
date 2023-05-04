from typing import Any


class Date:
    """
    Класс Date, проверяет числа даты на корректность.
    Attributes:
        day(int) - день
        month(int) - месяц
        year(int) - год
    """
    day = 0
    month = 0
    year = 0

    @classmethod
    def from_string(cls, new_date: str) -> Any:
        """
        Метод преобразует из str в int присваивая атрибутам значения.
        :param new_date: входящая строка типового значения "14-08-2022" через дефис
        :return: полную информацию о дате.
        """
        cls.day = int(new_date[:2])
        cls.month = int(new_date[3:5])
        cls.year = int(new_date[6:])
        return f'День: {cls.day}    Месяц: {cls.month}    Год: {cls.year}'

    @classmethod
    def is_date_valid(cls, new_date: str) -> bool:
        """
        Метод проверяет на логические ошибки в дате.
        :param new_date: входящая строка типового значения "14-08-2022" через дефис
        :return: True или False.
        """
        flag = True
        Date.from_string(new_date)
        if cls.day > 31 or cls.month > 12:
            flag = False
        return flag


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
