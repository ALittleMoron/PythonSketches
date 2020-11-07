import math


# begin1
def square_Perimeter(side:int) -> int:
    """ Периметр квадрата из его стороны. """
    return side*4


# begin2
def square_Area(side:int) -> int:
    """ Площадь квадрата из его стороны. """
    return side**2


# begin3
def rectangle_Area_and_Perimeter(side_a:int, side_b:int) -> (int, int):
    """ Площадь и периметр прямоугольника из его сторон a и b. """
    return side_a*side_b, (side_a+side_b)*2


# begin4
def circumference(diameter:int) -> float:
    """ Длина окружности. """
    return diameter*3.14


# begin5
def cube_Volume_And_Area(side:int) -> (int, int):
    """ Объем куба и площадь его поверхности. """
    return side**3, side*6


# begin6
def rectangle_Volume_And_Area(side_a:int, side_b:int, side_c:int) -> (int, int):
    """ Объем параллелепипеда и площадь его поверхности. """
    return side_a*side_b*side_c, (side_a*side_b + side_b*side_c + side_a*side_c)*2


# begin7
