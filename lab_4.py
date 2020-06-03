import math
from numpy import arange

a = 0
b = math.pi/4
STEP = 0.01
FUNC = 'math.tan(x)'


def left_point_method(func:str, diapason:list):
    if not func and not diapason:
        raise Exception("no function or diapason")
    if len(diapason) > 2:
        raise Exception("diapason must consistrs of 2 int nums")

    summary =  0 
    for x in arange(diapason[0], diapason[1], STEP):
        summary += eval(f'math.tan({x})')
    return summary * STEP

if __name__ == "__main__":
    res = left_point_method(FUNC, [a,b])
    print(res)