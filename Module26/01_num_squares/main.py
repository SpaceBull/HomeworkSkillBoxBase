# 1/3 pk 13
class SquareNumbers:
    """
        Класс "Квадратное Число"
        с итератором  __iter__ и
        с последующим выводом __next__.

    :arg
        max_number (int): Максимальное число, достигнув которого сработает StopIteration
    """

    def __init__(self, max_number: int) -> None:
        self.max_number = max_number
        self.roster = []

    def __iter__(self):
        """
            Метод итератора, позволяет перебирать итерируемый объект.

        :return:
            возвращает самого себя
        """
        return self

    def __next__(self):
        """
            Метод next, позволяет показать следующую по порядку вариацию.
            Список roster заполняется квадратными числами max_number раз.

        :raise StopIteration: Если длина списка roster (с квадратными числами) равен заданному max_number,
         то вызовется исключение
        :return:
            roster (список)
        """
        if len(self.roster) == self.max_number:
            raise StopIteration
        self.roster = [number ** 2 for number in range(1, self.max_number + 1)]
        return self.roster


number_max = int(input('Введите число: '))
first_option = SquareNumbers(number_max)
for square_number in first_option:
    print(square_number)


# функция с генератором
def square_numbers(max_number: int) -> str:
    for number in range(1, max_number + 1):
        answer = number ** 2
        yield answer


number_max = int(input('Введите число: '))
for square_number in square_numbers(number_max):
    print(square_number, end=' ')


# генераторное выражение
print('\n')
max_number = int(input('Введите число: '))
result = (number ** 2 for number in range(1, max_number + 1))

for square_number in result:
    print(square_number, end=' ')
