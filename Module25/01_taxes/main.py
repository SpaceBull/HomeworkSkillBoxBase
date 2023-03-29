class Property:
    """
    Базовый класс - характеризующий собственность,

    __worth: собственный капитал
    """
    __worth = 0

    def designer(self, price):
        """
        Конструктор для высчитывания налога с собственного капитала.

        :param price: приходящий подсчитанный налог.
        :type price: int
        """
        print(f'\nБаланс вашего счёта: {Property.__worth} руб')
        print(f'Налог составит: {price} руб.')
        Property.__worth -= price
        if Property.__worth < 0:
            print(f'!!Вам необходимо набрать {abs(Property.__worth)} руб. для оплаты налога!!')

    def set_worth(self, capital):
        """
        Сеттер для установления собственного капитала

        :param capital: собственный капитал
        :type capital: int
        :raise Exception: Если собственного капитала меньше ноля, то вызывается исключение
        """
        if capital > 0:
            Property.__worth = capital
        else:
            raise Exception('На вашем счету недостаточно средств, для оплаты налога!')


class Apartment(Property):
    """
    Класс Квартира. Родитель Property

    :arg
        tax_calculation(int) - передаётся стоимость квартиры
    """
    def __init__(self, price_apartament):
        self.tax_calculation(price_apartament)
    """
    метод tax_calculation() - Считает налог на квартиру
    и передает значение в designer(Конструктор) родительского класса
    :arg
        :type price_apartament : int
    :return: передает подсчитанный налог в designer(Конструктор) родительского класса 
    """
    def tax_calculation(self, price_apartament):
        price_apartament /= 1000
        return super().designer(price_apartament)


class Car(Property):
    """
    Класс Машина. Родитель Property

    :arg
        tax_calculation(int) - передаётся стоимость машины
    """
    def __init__(self, price_car):
        self.tax_calculation(price_car)
    """
    метод tax_calculation() - Считает налог на машину
    и передает значение в designer(Конструктор) родительского класса
    :arg
        :type price_car : int
    :return: передает подсчитанный налог в designer(Конструктор) родительского класса 
    """
    def tax_calculation(self, price_car):
        price_car /= 200
        return super().designer(price_car)


class CountryHouse(Property):
    """
    Класс Дача. Родитель Property

    :arg
        tax_calculation(int) - передаётся стоимость дачи
    """
    def __init__(self, price_country_house):
        self.tax_calculation(price_country_house)

    """
    метод tax_calculation() - Считает налог на дачу
    и передает значение в designer(Конструктор) родительского класса
    :arg
        :type price_country_house : int
    :return: передает подсчитанный налог в designer(Конструктор) родительского класса 
    """
    def tax_calculation(self, price_country_house):
        price_country_house /= 500
        return super().designer(price_country_house)


money = int(input('Введите количество ваших денег: '))
value_apartament = int(input('Введите стоимость вашей квартиры: '))
value_car = int(input('Введите стоимость вашего автомобиля: '))
value_country_house = int(input('Введите стоимость вашей дачи: '))


my_money = Property()
my_money.set_worth(money)
my_first_property = Apartment(price_apartament=value_apartament)
my_second_property = Car(price_car=value_car)
my_third_property = CountryHouse(price_country_house=value_country_house)
