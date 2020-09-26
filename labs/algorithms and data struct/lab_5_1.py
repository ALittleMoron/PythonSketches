from math import sqrt
from timeit import default_timer

eps = 0.000001
phi = (1 + sqrt(5))/2
f = lambda x: 7*x**2 - 42*x + 66


def extremum_min(a: float, b: float, e: float):
    start = default_timer()
    x1, x2 = .0, .0
    while True:
        x1 = b - (b - a)/ phi
        x2 = a + (b - a)/ phi
        if f(x1) >= f(x2):
            a = x1
        else:
            b = x2
        if abs(b-a) < e:
            break
    return round((a + b)/2, 2), default_timer()-start


if __name__ == "__main__":
    res, time =  extremum_min(0, 4, eps)
    print(f'\nфункция 7*x*x - 42*x + 66 на отрезке от 0 до 4 имеет значение min = {res}.')
    print(f'Время работы: {time}\nТочность: {eps}')