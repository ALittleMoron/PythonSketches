import math


# Буду пропускать повторяющиеся задания или очень похожие.


# begin1
def square_Perimeter(side: int) -> int:
    """ Периметр квадрата из его стороны. """
    return side*4


# begin2
def square_Area(side: int) -> int:
    """ Площадь квадрата из его стороны. """
    return side**2


# begin3
def rectangle_Area_and_Perimeter(side_a: int, side_b: int) -> (int, int):
    """ Площадь и периметр прямоугольника из его сторон a и b. """
    return side_a*side_b, (side_a+side_b)*2


# begin4
def circle_diameter(diameter: int) -> float:
    """ Диаметр окружности. """
    return diameter*math.pi


# begin5
def cube_Volume_And_Area(side: int) -> (int, int):
    """ Объем куба и площадь его поверхности. """
    return side**3, side*6


# begin6
def rectangle_Volume_And_Area(side_a: int, side_b: int, side_c: int) -> (int, int):
    """ Объем параллелепипеда и площадь его поверхности. """
    return side_a*side_b*side_c, (side_a*side_b + side_b*side_c + side_a*side_c)*2


# begin7
def circumference_and_cyrcle_area(radius: int) -> (float, float):
    """ Длина окружности и площадь. """
    return 2*math.pi*radius, math.pi*(radius**2)


# begin8
def average(a: int, b: int) -> float:
    """ Среднее арифметическое двух чисел. """
    return (a+b)/2


# begin9
def geometric_mean(a: int, b: int) -> float:
    """ Среднее геометрическое двух чисел. """
    return (abs(a)*abs(b))**0.5


# begin10
def sum_sub_mult_div_of_square_numbers(a: int, b: int) -> (int, int, int, float):
    """ Сумма, разность, произведение и частное квадратов двух чисел. """
    return a**2+b**2, a**2-b**2, (a**2)*(b**2), (a**2)/(b**2)


# begin11
def sum_sub_mult_div_of_absolute_numbers(a: int, b: int) -> (int, int, int, float):
    """ Сумма, разность, произведение и частное модулей двух чисел. """
    return abs(a)+abs(b), abs(a)-abs(b), abs(a)*abs(b), abs(a)/abs(b)


# begin12
def hypotenuse_and_perimeter(leg_a: int, leg_b: int) -> (float, float):
    """ Гипотенуза и периметр треугольника. """
    hypotenuse = (leg_a**2+leg_b**2)**0.5
    return hypotenuse, leg_a+leg_b+hypotenuse


# begin13
def asgas(R_1: int, R_2: int) -> (float, float, float):
    """ Площадь двух кругов и кольцо-разницу двух площадей. """
    return math.pi*(R_1**2), math.pi*(R_2**2), math.pi*(R_2**2 - R_1**2)


# begin14
def radius_and_area_of_cyrcle(L: int) -> (float, float):
    """ Радиус и площадь круга из длины окружности. """
    R = 2*math.pi/L
    return R, math.pi*(R**2)


# begin15
def diameter_and_circumference_of_cyrcle(S: int) -> (float, float):
    """ Диаметр и длину окружности из площади. """
    D = ((4*S)/math.pi)**0.5
    return D, math.pi*D


# begin16
def distance_between_two_points(x1: int, x2: int) -> int:
    """ Расстояние между двумя точками (без y1, y2). """
    return abs(x2-x1)


# begin17
def three_points_and_sum(A: int, B: int, C: int) -> (int, int, int):
    """ Расстояние АС, BC и их сумма. """
    return abs(C-A), abs(C-B), abs(C-A) + abs(C-B)


# ...


if __name__ == "__main__":
    pass
