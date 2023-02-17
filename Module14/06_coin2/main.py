
def check_coordinates(x, y, radius):
    coordinate_x = 0.0
    coordinate_y = 0.0
    if coordinate_x + radius >= x and coordinate_y + radius >= y:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


number_x = float(input('Введите Х: '))
number_y = float(input('Введите Y: '))
number_radius = float(input('Введите радиус: '))
check_coordinates(number_x, number_y, number_radius)
