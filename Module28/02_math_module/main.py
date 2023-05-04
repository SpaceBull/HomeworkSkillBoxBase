class MyMath:
    """
    Класс MyMath с различными математическими вычислениями.
    __pi: число пи
    """
    __pi = 3.1415926535

    @classmethod
    def circle_len(cls, radius: int) -> float:
        """
        Метод вычисления длины окружности (answer=2πR)
        :param radius: (int) радиус
        :return: (float) ответ
        """
        answer = 2 * cls.__pi * radius
        return answer

    @classmethod
    def area_circle(cls, radius: int) -> float:
        """
        Метод вычисления площади окружности (answer=πR²).
        :param radius: (int) радиус
        :return: (float) ответ
        """
        answer = cls.__pi * (radius ** 2)
        return answer

    @classmethod
    def cube_volume(cls, edge: int) -> int:
        """
        Метод вычисления объёма куба (answer=a³).
        :param edge: (int) радиус
        :return: (int) ответ
        """
        answer = edge ** 3
        return answer

    @classmethod
    def surface_area_sphere(cls, radius: int) -> float:
        """
        Метод площадь поверхности сферы (answer= 4πR²).
        :param radius: (int) радиус
        :return: (float) ответ
        """
        answer = (4 * cls.__pi) * (radius ** 2)
        return answer


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.area_circle(radius=6)
res_3 = MyMath.cube_volume(edge=3)
res_4 = MyMath.surface_area_sphere(radius=9)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
