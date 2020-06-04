import math
import time

from numpy import arange


a = 0
b = math.pi/4
STEP = 0.01
FUNC = 'math.tan({})'


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}: {end-start} секунд.')
        return return_value
    return wrapper


@benchmark
def left_point_method(func:str, diapason:list):
    if not func and not diapason:
        raise Exception("no function or diapason")
    if len(diapason) > 2:
        raise Exception("diapason must consistrs of 2 int nums")

    summary =  0 
    for x in arange(diapason[0], diapason[1], STEP):
        summary += eval(func.format(x))
    
    return summary * STEP


@benchmark
def right_point_method(func:str, diapason:list):
    if not func and not diapason:
        raise Exception("no function or diapason")
    if len(diapason) > 2:
        raise Exception("diapason must consistrs of 2 int nums")

    summary = 0
    for x in arange(diapason[0] + STEP, diapason[1] + STEP, STEP):
        summary += eval(func.format(x))
    
    return summary * STEP


@benchmark
def middle_point_method(func:str, diapason:list):
    if not func and not diapason:
        raise Exception("no function or diapason")
    if len(diapason) > 2:
        raise Exception("diapason must consistrs of 2 int nums")

    summary = 0
    for x in arange(diapason[0] + STEP/2.0, diapason[1], STEP):
        summary += eval(func.format(x))
    
    return summary * STEP


@benchmark
def trapezoid_method(func:str, diapason:list):
    if not func and not diapason:
        raise Exception("no function or diapason")
    if len(diapason) > 2:
        raise Exception("diapason must consistrs of 2 int nums")

    summary = 0
    for x in arange(diapason[0]+ STEP/2.0, diapason[1], STEP):
        if (x == diapason[0]+ STEP) or (x == diapason[1]):
            summary += eval(func.format(x) + '/ 2')
        else:
            summary += eval(func.format(x))
    
    return summary * STEP


@benchmark
def simpsons_method(func:str, diapason:list):
    if not func and not diapason:
        raise Exception("no function or diapason")
    if len(diapason) > 2:
        raise Exception("diapason must consistrs of 2 int nums")

    summary = 0
    for i in range(100):
        x = diapason[0] + STEP * i
        if (i == 0) or (i == 99):
            summary += eval(func.format(x))
        elif (i % 2 == 1):
            summary += eval(func.format(x) + '* 4')
        elif (i % 2 == 0):
            summary += eval(func.format(x) + '* 2')
    
    return summary * STEP/5.0


if __name__ == "__main__":
    print('\nВремя выполнения функций:\n')
    res_1 = left_point_method(FUNC, [a,b])
    res_2 = right_point_method(FUNC, [a,b])
    res_3 = middle_point_method(FUNC, [a,b])
    res_4 = trapezoid_method(FUNC, [a,b])
    res_5 = simpsons_method(FUNC, [a,b])
    
    print(f'''
\nРезультаты работы функций:

left_point_method = {res_1},
right_point_method = {res_2},
middle_point_method = {res_3},
trapezoid_method = {res_4},
simpsons_method = {res_5}. ''')
