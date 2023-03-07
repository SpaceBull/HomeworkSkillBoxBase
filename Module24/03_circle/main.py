import math


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_perimeter(self):
        answer_perimeter = 2 * math.pi * self.r
        print(answer_perimeter)

    def get_square(self):
        answer_square = math.pi * self.r ** 2
        print(answer_square)

    def increase_scale(self, k):
        self.r *= k
        print(self.r)

    def is_intersect(self, other):
        print((self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2)


first_data = Circle()
first_data.get_perimeter()
first_data.get_square()
first_data.increase_scale(2)
second_data = Circle(1, 3, 2)
first_data.is_intersect(second_data)


